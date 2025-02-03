from django.test import (
    TestCase,
    RequestFactory,
)
from new_tests_2.views import HomeView

class HomeViewTestCase(TestCase):
    def test_environment_set_in_context(self):
        request = RequestFactory().get("HomeView/")
        view = HomeView()
        view.setup(request)

        print(view.template_name)

        self.assertEqual(view.template_name, "new_tests_2/home.html")
        self.assertIn("environment", view.get_context_data())