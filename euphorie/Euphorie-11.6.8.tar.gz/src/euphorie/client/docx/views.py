# coding=utf-8
from euphorie.client import model
from euphorie.client import utils
from euphorie.client.docx.compiler import _sanitize_html
from euphorie.client.docx.compiler import DocxCompiler
from euphorie.client.docx.compiler import DocxCompilerFrance
from euphorie.client.docx.compiler import DocxCompilerItaly
from euphorie.client.docx.compiler import DocxCompilerItalyOriginal
from euphorie.client.docx.compiler import IdentificationReportCompiler
from euphorie.client.utils import get_translated_custom_risks_title
from euphorie.content import MessageFactory as _
from euphorie.content.survey import get_tool_type
from plone import api
from plone.memoize.view import memoize
from Products.Five import BrowserView
from sqlalchemy import sql
from StringIO import StringIO
from urllib import quote
from z3c.saconfig import Session
from zope.i18n import translate


class OfficeDocumentView(BrowserView):
    """Base view that generates an office document and returns it"""

    _compiler = None
    _content_type = ""

    def get_data(self, for_download=False):
        """Return the data for the compiler"""
        return {}

    @property
    @memoize
    def webhelpers(self):
        return api.content.get_view("webhelpers", self.context, self.request)

    def get_payload(self):
        """Compile the template and return the file as a string"""
        output = StringIO()
        compiler = self._compiler(self.context, self.request)
        compiler.compile(self.get_data(for_download=True))
        compiler.template.save(output)
        output.seek(0)
        return output.read()

    def t(self, txt):
        return translate(txt, context=self.request)

    def get_session_nodes(self):
        """Return an ordered list of all relevant tree items for the current
        survey.
        """
        query = (
            Session.query(model.SurveyTreeItem)
            .filter(model.SurveyTreeItem.session == self.context.session)
            .filter(sql.not_(model.SKIPPED_PARENTS))
            .filter(
                sql.or_(
                    model.MODULE_WITH_RISK_OR_TOP5_FILTER,
                    model.RISK_PRESENT_OR_TOP5_FILTER,
                )
            )
            .order_by(model.SurveyTreeItem.path)
        )

        return query.all()

    def get_modules(self):
        """Returns the modules for this session"""
        sql_modules = (
            Session.query(model.Module)
            .filter(
                model.SurveyTreeItem.session == self.context.session,
            )
            .order_by(model.SurveyTreeItem.path)
        )
        modules = []
        for sql_module in sql_modules:
            if sql_module.skip_children:
                continue
            if sql_module.zodb_path.find("custom-risks") != -1:
                module_title = get_translated_custom_risks_title(self.request)
            else:
                module_title = sql_module.title
            risks = self.get_risks_for(sql_module)
            modules.append(
                {
                    u"title": module_title,
                    u"checked": bool(risks),
                    u"risks": risks,
                }
            )
        return modules

    def get_risks_for(self, sql_module):
        sql_risks = (
            Session.query(model.Risk)
            .filter(model.Risk.parent_id == sql_module.id)
            .order_by(model.SurveyTreeItem.path)
        )
        risks = []
        for sql_risk in sql_risks:
            if not sql_risk.is_custom_risk:
                risk = self.context.aq_parent.restrictedTraverse(
                    sql_risk.zodb_path.split("/")
                )
                risk_description = risk.description
            else:
                risk = None
                risk_description = ""
            risk_description = _sanitize_html(risk_description)

            measures = [
                measure.action
                for measure in (
                    sql_risk.in_place_standard_measures
                    + sql_risk.in_place_custom_measures
                )
            ]

            if sql_risk.identification == "no" or (
                risk and getattr(risk, "type", None) == "top5"
            ):
                actions = [
                    _get_action_plan(action)
                    for action in (
                        sql_risk.standard_measures + sql_risk.custom_measures
                    )
                ]
            else:
                actions = []
            risks.append(
                {
                    u"title": sql_risk.title.strip(),
                    u"description": risk_description,
                    u"comment": _escape_text(sql_risk.comment),
                    u"actions": actions,
                    u"measures": measures,
                    u"epilogue": u"",
                    u"justifiable": sql_risk.identification,
                    u"number": sql_risk.number,
                    u"priority": sql_risk.priority,
                }
            )
        return risks

    def __call__(self):
        if not self.webhelpers.can_view_session:
            return self.request.response.redirect(self.webhelpers.client_url)
        self.request.response.setHeader(
            "Content-Disposition",
            "attachment; filename*=UTF-8''{}".format(quote(self._filename)),
        )
        self.request.response.setHeader(
            "Content-Type",
            self._content_type,
        )
        return self.get_payload()


def _escape_text(txt):
    txt = txt or ""
    txt = txt.replace("<", "&lt;")
    # vertical tab / ASCII 11 / SHIFT + RETURN in Word is unprintable
    txt = txt.replace("\x0b", " ")
    # Also this character can make trouble
    txt = txt.replace("\x01", " ")
    return txt


def _get_action_plan(action):
    action_plan = {}
    action_plan["text"] = _escape_text(action.action)
    requirements = getattr(action, "requirements") or ""
    action_plan["requirements"] = _escape_text(requirements)
    if action.responsible:
        action_plan["responsible"] = _escape_text(action.responsible)
    if action.planning_start:
        action_plan["planning_start"] = action.planning_start.strftime("%d.%m.%Y")
    if action.planning_end:
        action_plan["planning_end"] = action.planning_end.strftime("%d.%m.%Y")
    return action_plan


class ActionPlanDocxView(OfficeDocumentView):
    """Generate a report based on a basic docx template"""

    _compiler = DocxCompiler
    _content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"  # noqa: E 501

    def __init__(self, context, request):
        super(ActionPlanDocxView, self).__init__(context, request)
        country = self.webhelpers.country
        tool_type = get_tool_type(self.webhelpers._survey)
        if country == "it":
            if tool_type == "existing_measures":
                self._compiler = DocxCompilerItaly
            else:
                self._compiler = DocxCompilerItalyOriginal
        elif country == "fr":
            if tool_type == "existing_measures":
                self._compiler = DocxCompilerFrance

    def get_heading(self, title):
        heading = self.t(
            _(
                "header_oira_report_download",
                default=u"OiRA Report: “${title}”",
                mapping=dict(title=title),
            ),
        )
        return heading

    def get_section_headings(self):
        headings = [
            self.t(
                _(
                    "header_present_risks",
                    default=u"Risks that have been identified, "
                    u"evaluated and have an Action Plan",
                )
            ),
            self.t(
                _(
                    "header_unevaluated_risks",
                    default=u"Risks that have been identified but "
                    u"do NOT have an Action Plan",
                )
            ),
            self.t(
                _(
                    "header_unanswered_risks",
                    default=u'Hazards/problems that have been "parked" '
                    u"and are still to be dealt with",
                )
            ),
            self.t(
                _(
                    "header_risks_not_present",
                    default=u"Hazards/problems that have been managed "
                    u"or are not present in your organisation",
                )
            ),
        ]
        return headings

    def get_sorted_nodes(self):
        nodes = self.get_session_nodes()
        session = self.context.session

        actioned_nodes = utils.get_actioned_nodes(nodes)
        unactioned_nodes = utils.get_unactioned_nodes(nodes)
        unanswered_nodes = utils.get_unanswered_nodes(session)
        risk_not_present_nodes = utils.get_risk_not_present_nodes(session)
        # From the non-present risks, filter out risks from the (un-)/actioned
        # categories. A "priority" risk will always appear in the action plan,
        # even if it has been answered with "Yes"
        risk_not_present_nodes = [
            n
            for n in risk_not_present_nodes
            if n not in actioned_nodes and n not in unactioned_nodes
        ]
        nodes = [
            actioned_nodes,
            unactioned_nodes,
            unanswered_nodes,
            risk_not_present_nodes,
        ]
        return nodes

    def get_data(self, for_download=False):
        """Gets the data structure in a format suitable for `DocxCompiler`"""
        session = self.context.session
        data = {
            "title": session.title,
            "comment": session.report_comment,
            "heading": self.get_heading(session.title),
            "section_headings": self.get_section_headings(),
            "nodes": self.get_sorted_nodes(),
            "survey_title": self.context.aq_parent.title,
            "modules": self.get_modules(),
        }

        return data

    @property
    def _filename(self):
        """Return the document filename"""
        filename = _(
            "filename_report_actionplan",
            default=u"Action plan ${title}",
            mapping={"title": self.context.session.title},
        )
        filename = translate(filename, context=self.request)
        return filename.encode("utf8") + ".docx"


class IdentificationReportDocxView(OfficeDocumentView):
    """Generate a report based on a basic docx template"""

    _compiler = IdentificationReportCompiler
    _content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"  # noqa: E 501

    def get_session_nodes(self):
        """Return an ordered list of all tree items for the current
        survey. By OSHA's request, optional submodules are always included.
        """
        query = (
            Session.query(model.SurveyTreeItem)
            .filter(model.SurveyTreeItem.session == self.context.session)
            .order_by(model.SurveyTreeItem.path)
        )
        return query.all()

    def get_data(self, for_download=False):
        """Gets the data structure in a format suitable for `DocxCompiler`"""

        data = {
            "title": self.context.session.title,
            "heading": "",
            "section_headings": [self.context.session.title],
            "nodes": [self.get_session_nodes()],
        }
        return data

    @property
    def _filename(self):
        """Return the document filename"""
        filename = _(
            "filename_report_identification",
            default=u"Identification report ${title}",
            mapping=dict(title=self.context.session.title),
        )
        filename = translate(filename, context=self.request)
        return filename.encode("utf8") + ".docx"
