import unittest
from app import create_app
from tests.integration.create_token import create_token


class TestEmptyComments(unittest.TestCase):

    def setUp(self):
        self.application = create_app('development')
        self.client = self.application.test_client()

    def test_empty_comments(self):
        # Get a token
        token = create_token('0203', '1')
        resp = self.client.get('/session?token=' + token.decode(), follow_redirects=True)
        self.assertEquals(resp.status_code, 200)

        # We are on the landing page
        content = resp.get_data(True)

        self.assertRegexpMatches(content, '<title>Introduction</title>')
        self.assertRegexpMatches(content, '>Get Started<')
        self.assertRegexpMatches(content, '(?s)Monthly Business Survey - Retail Sales Index.*?Monthly Business Survey - Retail Sales Index')

        # We proceed to the questionnaire
        post_data = {
            'action[start_questionnaire]': 'Start Questionnaire'
        }
        resp = self.client.post('/questionnaire/introduction', data=post_data, follow_redirects=False)
        self.assertEquals(resp.status_code, 302)

        block_one_url = resp.headers['Location']

        resp = self.client.get(block_one_url, follow_redirects=False)
        self.assertEquals(resp.status_code, 200)

        # We are in the Questionnaire
        content = resp.get_data(True)
        self.assertRegexpMatches(content, '<title>Survey</title>')
        self.assertRegexpMatches(content, '>Monthly Business Survey - Retail Sales Index</')
        self.assertRegexpMatches(content, "What are the dates of the sales period you are reporting for\?")
        self.assertRegexpMatches(content, ">Save &amp; Continue<")

        # We fill in our answers
        form_data = {
            # Start Date
            "6fd644b0-798e-4a58-a393-a438b32fe637-day": "01",
            "6fd644b0-798e-4a58-a393-a438b32fe637-month": "4",
            "6fd644b0-798e-4a58-a393-a438b32fe637-year": "2016",
            # End Date
            "06a6a4b7-6ce4-4687-879d-3443cd8e2ff0-day": "30",
            "06a6a4b7-6ce4-4687-879d-3443cd8e2ff0-month": "04",
            "06a6a4b7-6ce4-4687-879d-3443cd8e2ff0-year": "2016",
            # Total Turnover
            "e81adc6d-6fb0-4155-969c-d0d646f15345": "100000",
            # User Action
            "action[save_continue]": "Save &amp; Continue",
            # Empty comment
            "215015b1-f87c-4740-9fd4-f01f707ef558": "  "
        }

        # We submit the form
        resp = self.client.post(block_one_url, data=form_data, follow_redirects=False)
        self.assertEquals(resp.status_code, 302)

        # There are no validation errors
        self.assertRegexpMatches(resp.headers['Location'], r'\/questionnaire\/summary$')

        summary_url = resp.headers['Location']

        resp = self.client.get(summary_url, follow_redirects=False)
        self.assertEquals(resp.status_code, 200)

        # We are on the review answers page
        content = resp.get_data(True)
        self.assertRegexpMatches(content, '<title>Summary</title>')
        self.assertRegexpMatches(content, '>Monthly Business Survey - Retail Sales Index</')
        self.assertRegexpMatches(content, '>Your responses<')
        self.assertRegexpMatches(content, '>Please check carefully before submission<')
        self.assertRegexpMatches(content, '>Submit answers<')

        # We submit our answers
        post_data = {
            "action[submit_answers]": "Submit answers"
        }
        resp = self.client.post(summary_url, data=post_data, follow_redirects=False)
        self.assertEquals(resp.status_code, 302)
        self.assertRegexpMatches(resp.headers['Location'], r'\/questionnaire\/thank-you$')
        resp = self.client.get(resp.headers['Location'], follow_redirects=True)
        self.assertEquals(resp.status_code, 200)

        # We are on the thank you page
        content = resp.get_data(True)
        self.assertRegexpMatches(content, '<title>Thank You</title>')
        self.assertRegexpMatches(content, '(?s)Monthly Business Survey - Retail Sales Index.*?Monthly Business Survey - Retail Sales Index')
        self.assertRegexpMatches(content, '>Successfully Received<')