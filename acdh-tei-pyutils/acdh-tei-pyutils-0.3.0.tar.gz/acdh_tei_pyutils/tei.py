import re
from acdh_xml_pyutils.xml import XMLReader

NER_TAG_MAP = {
    "persName": "PER",
    "person": "PER",
    "placeName": "LOC",
    "place": "LOC",
    "orgName": "ORG",
    "org": "ORG",
    "work": "WORK",
    "workName": "WORK",
    "bibl": "WORK",
    "name": "NAME",
    "date": "DATE",
    "time": "TIME"
}


class TeiReader(XMLReader):

    """ a class to read an process tei-documents"""

    def any_xpath(self, any_xpath='//tei:rs'):

        """ Runs any xpath expressions against the parsed document
        :param any_xpath: Any XPath expression.
        :return: The result of the xpath
        """
        return self.tree.xpath(any_xpath, namespaces=self.ns_tei)

    def extract_ne_elements(self, parent_node, ne_xpath='//tei:rs'):

        """ extract elements tagged as named entities
        :param ne_xpath: An XPath expression pointing to elements used to tagged NEs.
        :return: A list of elements
        """

        ne_elements = parent_node.xpath(ne_xpath, namespaces=self.ns_tei)
        return ne_elements

    def extract_ne_dicts(self, parent_node, ne_xpath='//tei:rs', NER_TAG_MAP=NER_TAG_MAP):

        """ extract strings tagged as named entities
        :param ne_xpath: An XPath expression pointing to elements used to tagged NEs.
        :param NER_TAG_MAP: A dictionary providing mapping from TEI tags used to tag NEs to\
        spacy-tags
        :return: A list of NE-dicts containing the 'text' and the 'ne_type'
        """

        ne_elements = self.extract_ne_elements(parent_node, ne_xpath)
        ne_dicts = []
        for x in ne_elements:
            item = {}
            text = "".join(x.xpath('.//text()'))
            item['text'] = re.sub('\s+', ' ', text).strip()
            try:
                ne_type = NER_TAG_MAP.get("{}".format(x.xpath('./@type')[0]), 'MISC')
            except IndexError:
                ne_type = NER_TAG_MAP.get("{}".format(x.xpath("name()")), 'MISC')
            item['ne_type'] = ne_type
            ne_dicts.append(item)

        return ne_dicts

    def create_plain_text(self, node):

        """ extracts all text nodes from given element
        :param start_node: An XPath expressione pointing to\
        an element which text nodes should be extracted
        :return: A normalized, cleaned plain text
        """
        result = re.sub('\s+', ' ', "".join(node.xpath(".//text()"))).strip()

        return result

    def get_text_nes_list(
            self,
            parent_nodes='.//tei:body//tei:p',
            ne_xpath='.//tei:rs',
            NER_TAG_MAP=NER_TAG_MAP
    ):

        """ extracts all text nodes from given elements and their NE
        :param parent_nodes: An XPath expressione pointing to\
        those elements which text nodes should be extracted
        :param ne_xpath:  An XPath expression pointing to elements used to tagged NEs.\
        Takes the parent node(s) as context
        :param NER_TAG_MAP: A dictionary providing mapping from TEI tags used to tag NEs to\
        spacy-tags
        :return: A list of dicts like [{"text": "Wien ist schön", "ner_dicts": [{"text": "Wien",\
        "ne_type": "LOC"}]}]
        """

        parents = self.tree.xpath(parent_nodes, namespaces=self.ns_tei)
        result = []
        for node in parents:
            text = self.create_plain_text(node)
            ner_dicts = self.extract_ne_dicts(node, ne_xpath, NER_TAG_MAP)
            result.append({'text': text, 'ner_dicts': ner_dicts})
        return result

    def extract_ne_offsets(
        self,
        parent_nodes='.//tei:body//tei:p',
        ne_xpath='.//tei:rs',
        NER_TAG_MAP=NER_TAG_MAP
    ):

        """ extracts offsets of NEs and the NE-type
        :param parent_nodes: An XPath expressione pointing to\
        those element which text nodes should be extracted
        :param ne_xpath: An XPath expression pointing to elements used to tagged NEs.\
        Takes the parent node(s) as context
        :param NER_TAG_MAP: A dictionary providing mapping from TEI tags used to tag NEs to\
        spacy-tags
        :return: A list of spacy-like NER Tuples [('some text'), {'entities': [(15, 19, 'place')]}]
        """

        text_nes_dict = self.get_text_nes_list(parent_nodes, ne_xpath, NER_TAG_MAP)
        result = []
        for x in text_nes_dict:
            plain_text = x['text']
            ner_dicts = x['ner_dicts']
            entities = []
            for x in ner_dicts:
                if x['text'] != "":
                    for m in re.finditer(x['text'], plain_text):
                        entities.append([m.start(), m.end(), x['ne_type']])
            entities = [item for item in set(tuple(row) for row in entities)]
            entities = sorted(entities, key=lambda x: x[0])
            ents = []
            next_item_index = 1
            # remove entities with the same start offset
            for x in entities:
                cur_start = x[0]
                try:
                    next_start = entities[next_item_index][0]
                except IndexError:
                    next_start = 9999999999999999999999
                if cur_start == next_start:
                    pass
                else:
                    ents.append(x)
                next_item_index = next_item_index + 1

            train_data = (
                plain_text,
                {
                    "entities": ents
                }
            )
            result.append(train_data)
        return result
