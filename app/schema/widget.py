from abc import ABCMeta
from flask import render_template


class Widget(metaclass=ABCMeta):
    def __init__(self):
        self.template = None
        self.container = None

    @staticmethod
    def get_instance(widget_type):
        # Import subclasses, avoidking circular dependencies
        from app.schema.widgets.dropdown_widget import DropdownWidget
        from app.schema.widgets.radio_group_widget import RadioGroupWidget
        from app.schema.widgets.checkbox_group_widget import CheckboxGroupWidget
        from app.schema.widgets.text_widget import TextWidget
        from app.schema.widgets.currency_widget import CurrencyWidget
        from app.schema.widgets.textarea_widget import TextareaWidget

        widget_type = str(widget_type).upper()
        if widget_type == 'DROPDOWNWIDGET':
            return DropdownWidget()
        elif widget_type == 'RADIOGROUPWIDGET':
            return RadioGroupWidget()
        elif widget_type == 'DATEWIDGET':
            return TextWidget()
        elif widget_type == 'TEXTAREAWIDGET':
            return TextareaWidget()
        elif widget_type == 'CHECKBOXGROUPWIDGET':
            return CheckboxGroupWidget()
        elif widget_type == 'TEXTWIDGET':
            return TextWidget()
        elif widget_type == 'CURRENCYWIDGET':
            return CurrencyWidget()

    def render(self):
        if self.template:
            return render_template('partials/widgets/' + self.template + '.html',
                                   widget=self,
                                   answer=self.container,
                                   question=self.container.container)
        else:
            return ''
