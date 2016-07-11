from app.schema.widget import Widget


class CheckboxGroupWidget(Widget):
    def __init__(self, name=None, options=None):
        self.template = 'checkbox_group_widget'
        self.name = name
        self.options = options
