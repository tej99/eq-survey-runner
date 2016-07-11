from app.schema.widget import Widget


class CurrencyWidget(Widget):
    def __init__(self, name=None):
        self.template = 'currency_widget'
        self.name = name
