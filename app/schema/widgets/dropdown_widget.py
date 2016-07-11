from app.schema.widget import Widget


class DropdownWidget(Widget):
    def __init__(self, name=None, options=None):
        super().__init__()
        self.template = 'dropdown_widget'
