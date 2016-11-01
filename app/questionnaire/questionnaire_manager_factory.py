import logging

from app.questionnaire.questionnaire_manager import QuestionnaireManager

from app.utilities.schema import get_schema


logger = logging.getLogger(__name__)


class QuestionnaireManagerFactory(object):

    @staticmethod
    def get_instance():
        logger.debug("QuestionManagerFactory - get instance")
        json, schema = get_schema()

        logger.debug("QuestionnaireManagerFactory - constructing new instance")
        return QuestionnaireManager(schema, json=json)
