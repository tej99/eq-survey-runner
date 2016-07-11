from app.schema.widget import Widget


class TextWidget(Widget):
    def __init__(self, name=None):
        self.template = 'text_widget'
        self.name = name
