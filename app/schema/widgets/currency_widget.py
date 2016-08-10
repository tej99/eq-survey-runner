from app.schema.widget import Widget
from flask import render_template
import logging

logger = logging.getLogger(__name__)


class CurrencyWidget(Widget):
    def render(self, state):
        widget_params = {
            'answer': {
                'name': self.name,
                'id': state.schema_item.id,
                'label': state.schema_item.label,
                'value': state.input,
                'placeholder': ''
            },
            'debug': {
                'schema': state.schema_item,
                'state': state
            }
        }
        return render_template('partials/widgets/currency_widget.html', **widget_params)