from app.schema.widget import Widget


class TextareaWidget(Widget):
    def __init__(self, name=None):
        self.template = 'textarea_widget'
        self.name = name
