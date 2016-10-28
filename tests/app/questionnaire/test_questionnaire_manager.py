import json
from unittest.mock import MagicMock, Mock

import os

from app import settings
from app.parser.schema_parser_factory import SchemaParserFactory
from app.questionnaire.questionnaire_manager import QuestionnaireManager
from app.questionnaire_state.node import Node
from app.schema.block import Block
from app.schema.group import Group
from app.schema.questionnaire import Questionnaire
from tests.app.framework.sr_unittest import SurveyRunnerTestCase


class TestQuestionnaireManager(SurveyRunnerTestCase):
    def setUp(self):
        super().setUp()
        schema_file = open(os.path.join(settings.EQ_SCHEMA_DIRECTORY, "0_star_wars.json"))
        schema = schema_file.read()
        # create a parser
        self.json = json.loads(schema)
        parser = SchemaParserFactory.create_parser(self.json)
        self.questionnaire = parser.parse()
        settings.EQ_SERVER_SIDE_STORAGE_TYPE = "IN_MEMORY"
