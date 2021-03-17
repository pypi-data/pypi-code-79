import json
import traceback
from typing import Sequence
from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
from django.urls import ResolverMatch, reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from jutil.admin import ModelAdminBase
from jsanctions.models import (
    SubjectType,
    Regulation,
    RegulationSummary,
    Remark,
    NameAlias,
    SanctionEntity,
    BirthDate,
    Identification,
    Citizenship,
    Address,
    SanctionsListFile,
)


class SanctionsListAdminBase(ModelAdminBase):
    exclude = ()
    save_on_top = False


class SubjectTypeAdmin(SanctionsListAdminBase):
    exclude = ()
    list_display = (
        "classification_code",
        "code",
    )


class SanctionsListFileAdmin(ModelAdminBase):
    save_on_top = False

    list_display = [
        "created",
        "generation_date",
        "imported",
        "file",
        "list_type",
        "entities",
    ]

    fields = [
        "created",
        "generation_date",
        "imported",
        "file",
        "list_type",
        "entities",
    ]

    readonly_fields = [
        "created",
        "generation_date",
        "imported",
        "entities",
    ]

    raw_id_fields = ()

    list_filter = [
        "list_type",
    ]

    date_hierarchy = "created"

    def entities(self, obj):
        assert isinstance(obj, SanctionsListFile)
        if not obj.id:
            return ""
        return format_html(
            '<a href="{}">{}</a>',
            reverse("admin:jsanctions_sanctionentity_source_changelist", args=[obj.id]),
            obj.sanctionentity_set.count(),
        )

    entities.short_description = _("sanction entities")  # type: ignore


class RemarkAdmin(SanctionsListAdminBase):
    raw_id_fields = ("container",)
    list_display = (
        "id",
        "text_brief",
    )


class RemarkInlineAdmin(admin.TabularInline):
    model = Remark
    fk_name = "container"
    extra = 0
    fields = ("text",)


class SanctionEntitySubFieldAdminBase(SanctionsListAdminBase):
    raw_id_fields: Sequence[str] = ("sanction",)


class SanctionEntityInlineAdmin(admin.StackedInline):
    fk_name = "sanction"
    extra = 0


class NameAliasAdmin(SanctionEntitySubFieldAdminBase):
    raw_id_fields = (
        "sanction",
        "regulation_summary",
    )


class NameAliasInlineAdmin(SanctionEntityInlineAdmin):
    model = NameAlias
    fields = (
        "first_name",
        "middle_name",
        "last_name",
        "whole_name",
        "name_language",
        "function",
        "title",
        "regulation_language",
        "logical_id",
        "regulation_summary",
    )
    raw_id_fields = (
        "sanction",
        "regulation_summary",
    )


class BirthDateAdmin(SanctionEntitySubFieldAdminBase):
    list_display = (
        "id",
        "sanction",
        "birth_date",
    )
    search_fields = ("birth_date",)


class BirthDateInlineAdmin(SanctionEntityInlineAdmin):
    model = BirthDate
    fields = (
        "circa",
        "calendar_type",
        "city",
        "zip_code",
        "birth_date",
        "day_of_month",
        "month_of_year",
        "year",
        "region",
        "place",
        "country_iso2_code",
        "country_description",
        "regulation_language",
        "logical_id",
    )


class AddressAdmin(SanctionEntitySubFieldAdminBase):
    list_display = (
        "id",
        "sanction",
        "street",
        "city",
        "region",
        "country_iso2_code",
    )
    search_fields = (
        "street",
        "city",
        "region",
        "country_iso2_code",
    )
    list_filter = ("country_iso2_code",)


class AddressInlineAdmin(SanctionEntityInlineAdmin):
    model = Address
    fields = (
        "city",
        "street",
        "po_box",
        "zip_code",
        "as_at_listing_time",
        "place",
        "region",
        "country_iso2_code",
        "country_description",
        "regulation_language",
        "logical_id",
        "regulation_summary",
    )
    raw_id_fields = ("regulation_summary",)


class IdentificationAdmin(SanctionEntitySubFieldAdminBase):
    raw_id_fields = (
        "sanction",
        "regulation_summary",
    )


class IdentificationInlineAdmin(SanctionEntityInlineAdmin):
    model = Identification
    fields = (
        "diplomatic",
        "known_expired",
        "known_false",
        "reported_lost",
        "revoked_by_issuer",
        "issued_by",
        "latin_number",
        "name_on_document",
        "number",
        "region",
        "country_iso2_code",
        "country_description",
        "identification_type_code",
        "identification_type_description",
        "regulation_language",
        "logical_id",
        "regulation_summary",
    )
    raw_id_fields = ("regulation_summary",)


class CitizenshipAdmin(SanctionEntitySubFieldAdminBase):
    raw_id_fields = (
        "sanction",
        "regulation_summary",
    )


class CitizenshipInlineAdmin(SanctionEntityInlineAdmin):
    model = Citizenship
    fields = (
        "region",
        "country_iso2_code",
        "country_description",
        "regulation_language",
        "logical_id",
        "regulation_summary",
    )
    raw_id_fields = (
        "sanction",
        "regulation_summary",
    )


class RegulationInlineAdmin(SanctionEntityInlineAdmin):
    model = Regulation
    fields = (
        "regulation_type",
        "organisation_type",
        "publication_date",
        "publication_url",
        "entry_into_force_date",
        "number_title",
        "programme",
        "logical_id",
    )


class RegulationSummaryAdmin(SanctionsListAdminBase):
    exclude = ()
    date_hierarchy = "publication_date"
    search_fields = (
        "number_title",
        "publication_date__year",
    )
    list_display = (
        "id",
        "regulation_type",
        "number_title",
        "publication_date",
        "publication_url",
    )


class DecadeBornListFilter(admin.SimpleListFilter):
    title = _("decade born")
    parameter_name = "born"

    def lookups(self, request, model_admin):
        opts = [
            ("-1919", "-1919"),
        ]
        begin = 1920
        this_year = now().year
        while begin <= this_year:
            end = begin + 9
            if BirthDate.objects.filter(year__gte=begin, year__lte=end).first():
                value = "{}-{}".format(begin, end)
                label = "{} - {}".format(begin, end)
                opts.append((value, label))
            begin += 10
        return opts

    def queryset(self, request, queryset):
        try:
            if self.value():
                begin, end = self.value().split("-")
                if begin:
                    queryset = queryset.filter(birthdate__year__gte=int(begin))
                if end:
                    queryset = queryset.filter(birthdate__year__lte=int(end))
        except Exception as e:
            messages.error(request, str(e))
            queryset = SanctionEntity.objects.none()
        return queryset


class AddressCountryFilter(admin.SimpleListFilter):
    title = _("residence country")
    parameter_name = "rcountry"

    def lookups(self, request, model_admin):
        opts = []
        for obj in Address.objects.distinct("country_iso2_code"):
            assert isinstance(obj, Address)
            opts.append((obj.country_iso2_code, obj.country_description))
        return opts

    def queryset(self, request, queryset):
        try:
            country = self.value()
            if country:
                queryset = SanctionEntity.objects.filter(address__country_iso2_code=country)
        except Exception as e:
            messages.error(request, str(e))
            queryset = SanctionEntity.objects.none()
        return queryset


class CitizenshipCountryFilter(admin.SimpleListFilter):
    title = _("citizenship country")
    parameter_name = "ccountry"

    def lookups(self, request, model_admin):
        opts = []
        for obj in Citizenship.objects.distinct("country_iso2_code"):
            assert isinstance(obj, Citizenship)
            opts.append((obj.country_iso2_code, obj.country_description))
        return opts

    def queryset(self, request, queryset):
        try:
            country = self.value()
            if country:
                queryset = SanctionEntity.objects.filter(citizenship__country_iso2_code=country)
        except Exception as e:
            messages.error(request, str(e))
            queryset = SanctionEntity.objects.none()
        return queryset


class SanctionEntityAdmin(SanctionsListAdminBase):
    search_fields = (
        "namealias__whole_name__icontains",
        "eu_reference_number__iexact",
        "birthdate__year__iexact",
        "birthdate__birth_date__iexact",
    )
    inlines = (
        NameAliasInlineAdmin,
        AddressInlineAdmin,
        IdentificationInlineAdmin,
        CitizenshipInlineAdmin,
        BirthDateInlineAdmin,
        RemarkInlineAdmin,
        RegulationInlineAdmin,
    )
    raw_id_fields = (
        "source",
        "subject_type",
    )
    list_display = (
        "id",
        "source",
        "designation_details",
        "name_aliases",
        "birth_year",
        "united_nation_id",
        "eu_reference_number",
        "logical_id",
        "subject_type",
    )
    list_filter = (
        "subject_type",
        DecadeBornListFilter,
        AddressCountryFilter,
        CitizenshipCountryFilter,
    )
    fields = [
        "source",
        "designation_details",
        "united_nation_id",
        "eu_reference_number",
        "logical_id",
        "subject_type",
        "data_fmt",
    ]
    readonly_fields = [
        "data_fmt",
    ]

    def data_fmt(self, obj) -> str:
        try:
            return mark_safe("<pre>" + json.dumps(obj.data, indent=4, sort_keys=True) + "</pre>")
        except Exception:
            return mark_safe("<pre>" + traceback.format_exc() + "</pre>")

    data_fmt.short_description = _("data")  # type: ignore

    def name_aliases(self, obj) -> str:
        assert isinstance(obj, SanctionEntity)
        all_names = ", ".join([e.whole_name for e in obj.namealias_set.all()])
        return all_names if len(all_names) < 64 else all_names[:64] + "..."

    name_aliases.short_description = _("name aliases")  # type: ignore

    def birth_year(self, obj) -> str:
        assert isinstance(obj, SanctionEntity)
        return ", ".join([str(e.year) for e in obj.birthdate_set.all().distinct("year")])

    birth_year.short_description = _("birth year")  # type: ignore

    def get_queryset(self, request):
        rm = request.resolver_match
        assert isinstance(rm, ResolverMatch)
        qs = super().get_queryset(request)
        source_id = rm.kwargs.get("source_id", None)
        if source_id:
            qs = qs.filter(source_id=source_id)
        return qs

    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.model_name  # type: ignore  # noqa
        return [
            url(
                r"^by-source/(?P<source_id>\d+)/$",
                self.admin_site.admin_view(self.kw_changelist_view),
                name="%s_%s_source_changelist" % info,
            ),
        ] + super().get_urls()


admin.site.register(SanctionsListFile, SanctionsListFileAdmin)
admin.site.register(SubjectType, SubjectTypeAdmin)
admin.site.register(RegulationSummary, RegulationSummaryAdmin)
admin.site.register(SanctionEntity, SanctionEntityAdmin)
