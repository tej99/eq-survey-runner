from app.schema.question import Question
from app.schema.answers.date_answer import DateAnswer


class DateRangeQuestion(Question):
    def __init__(self, name=None):
        super().__init__()
        if name:
            self.answers = [
                DateAnswer(name + '-from'),
                DateAnswer(name + '-to')
            ]
        else:
            self.answers = []
