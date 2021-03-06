from werkzeug.contrib.cache import NullCache

from app import cache, settings
from tests.integration.integration_test_case import IntegrationTestCase


class TestApplicationVariables(IntegrationTestCase):

    def setUp(self):
        settings.EQ_ENABLE_CACHE = False
        IntegrationTestCase.setUp(self)

    def tearDown(self):
        settings.EQ_ENABLE_CACHE = True
        IntegrationTestCase.tearDown(self)

    def test_schema_is_cached(self):
        with self.application.app_context():

            self.assertTrue(isinstance(cache.cache, NullCache))
