from app.model.display import Display
from app.libs.utils import eq_helper_lists_equivalent


class Block(object):
    def __init__(self):
        self.id = None
        self.title = None
        self.sections = []
        self.children = self.sections
        self.container = None
        self.questionnaire = None
        self.validation = None
        self.questionnaire = None
        self.templatable_properties = []
        self.display = Display()

    def add_section(self, section):
        if section not in self.sections:
            self.sections.append(section)
            section.container = self

    def to_json(self):
        json_dict = {
            "id": self.id,
            "title": self.title,
            "sections": [],
            "validation": [],
            "display": {}
        }

        for section in self.sections:
            json_dict['sections'].append(section.to_json())

        if self.validation is not None:
            for validation in self.validation:
                json_dict['validation'].append(validation.to_json())

        if self.display is not None:
            json_dict['display'] = self.display.to_json()

        return json_dict

    def __eq__(self, other):
        if id(self) == id(other):
            return True

        if isinstance(other, Block):
            properties_match = self.id == other.id and \
                               self.title == other.title

            sections_match = eq_helper_lists_equivalent(self.sections, other.sections)
            validations_match = eq_helper_lists_equivalent(self.validation, other.validation)
            templatable_properties_match = eq_helper_lists_equivalent(self.templatable_properties, other.templatable_properties)

            return properties_match and sections_match and validations_match and templatable_properties_match

        else:
            return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((self.id, self.title))
