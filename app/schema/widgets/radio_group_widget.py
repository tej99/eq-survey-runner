from app.schema.widget import Widget


class RadioGroupWidget(Widget):
    def __init__(self, name=None, options=None):
        self.template = 'radio_group_widget'
        self.name = name
        self.options = options
