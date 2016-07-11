from app.schema.display import Display
from app.schema.item import Item
from app.questionnaire_state.question import Question as State


class Question(Item):
    def __init__(self):
        self.id = None
        self.title = None
        self.description = ""
        self.answers = []
        self.children = self.answers
        self.container = None
        self.questionnaire = None
        self.validation = None
        self.questionnaire = None
        self.templatable_properties = ['title', 'description']
        self.display = Display()
        self.type = None

    @staticmethod
    def get_instance(question_type):
        # Import subclasses, avoid circular dependencies
        from app.schema.questions.custom_question import CustomQuestion
        from app.schema.questions.date_range_question import DateRangeQuestion
        from app.schema.questions.textarea_question import TextareaQuestion
        from app.schema.questions.currency_question import CurrencyQuestion
        from app.schema.questions.integer_question import IntegerQuestion

        question_type = str(question_type).upper()
        if question_type == 'CUSTOM':
            return CustomQuestion()
        elif question_type == "DATERANGE":
            return DateRangeQuestion()
        elif question_type == "CURRENCY":
            return CurrencyQuestion()
        elif question_type == "TEXTAREA":
            return TextareaQuestion()
        elif question_type == "INTEGER":
            return IntegerQuestion()

    def add_answer(self, answer):
        if answer not in self.answers:
            self.answers.append(answer)
            answer.container = self

    def get_state_class(self):
        return State
