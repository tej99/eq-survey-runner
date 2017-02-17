import logging

from flask import Blueprint
from flask import request
from flask import session
from flask import g
from werkzeug.exceptions import NotFound
from flask import render_template

from app.submitter.submitter import SubmitterFactory

from datetime import datetime, timezone

# pylint: disable=too-many-locals
logger = logging.getLogger(__name__)
feedback_blueprint = Blueprint('feedback', __name__, template_folder='templates')


@feedback_blueprint.before_request
def check_feedback_state():
    if session.get('feedback'):
        g.referrer = request.referrer
    else:
        raise NotFound


@feedback_blueprint.route('/feedback', methods=['GET', 'POST'])
def get_feedback():
    if request.method == "POST":
        form = request.form
        satisfaction = form.get('satisfaction')
        survey_type = session.get('form_type')
        comment = form.get('comment')
        submitted_at = datetime.now(timezone.utc)

        if satisfaction:
            message = {
                'submitted_at': submitted_at.isoformat(),
                'survey_type': survey_type,
                'satisfaction': satisfaction,
                'comment': comment,
                'survey_id':'feedback',
                "collection": {
                "instrument_id": "1"},
            }

            submitter = SubmitterFactory.get_submitter()
            submitter.send_answers(message)

            session.clear()
            return render_template("thank-you-feedback.html")
        else:
            return render_template("feedback.html", error=True)

    return render_template("feedback.html", error=False)
