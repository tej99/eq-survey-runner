from app.validation.date_type_check import DateTypeCheck
from datetime import datetime
from app.schema.answer import Answer as SchemaAnswer
from app.libs.utils import ObjectFromDict
from app.schema.widgets.dropdown_widget import DropdownWidget
from app.schema.widgets.text_widget import TextWidget


class DateAnswer(SchemaAnswer):
    def __init__(self, name='', config={}):

        super().__init__()
        self.defaults = {
            'collect_day': True,
            'collect_month': True,
            'collect_year': True,
            'default_day': 1,
            'default_month': 1,
            'default_year': 1900
        }
        # Build our config from defaults, overriding defaults with supplied config
        self._config = ObjectFromDict({**self.defaults, **config})
        self.name = name
        self.type_checkers.append(DateTypeCheck())

    def get_typed_value(self, post_data):
        day = post_data.get(self.id + '-day', '')
        month = post_data.get(self.id + '-month', '')
        year = post_data.get(self.id + '-year', '')

        user_input = year + '/' + month + '/' + day

        for checker in self.type_checkers:
            result = checker.validate(user_input)
            if not result.is_valid:
                raise Exception(result.errors[0])
                return None

        return self._cast_user_input(user_input)

    def _cast_user_input(self, user_input):
        return datetime.strptime(user_input, "%Y/%m/%d")

    # nto callled currently
    def _prepare(self):
        self.defaults = {
            'collect_day': True,
            'collect_month': True,
            'collect_year': True,
            'default_day': 1,
            'default_month': 1,
            'default_year': 1900
        }

        # Initialise emty widgets array
        self.widgets = []

        # Build the required widgets

        if self._config.collect_day:
            days = range(1, 31)
            self.widgets.append(DropdownWidget(self.name + '-d', days))

        if self._config.collect_month:
            months = {
                '1': "January",
                '2': "February",
                '3': "March",
                '4': 'April',
                '5': 'May',
                '6': 'June',
                '7': 'July',
                '8': 'August',
                '9': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'December'
            }
            self.widgets.append(DropdownWidget(self.name + '-m', months))

        if self._config.collect_year:
            self.widgets.append(TextWidget(self.name + '-y'))
