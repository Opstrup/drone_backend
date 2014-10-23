from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from backend_api.views import index_page


class IndexPageTest(TestCase):
    """
    Test class for the index page.
    """

    def test_root_url_resolves_to_home_page_view(self):
        """
        Test root url to home_page
        """
        found = resolve('/')
        self.assertEqual(found.func, index_page)

    def test_home_page_returns_correct_html(self):
        """
        Test the correct html for the home_page
        """
        request = HttpRequest()
        response = index_page(request)
        expected_html = render_to_string('index.html')
        self.assertEqual(response.content.decode(), expected_html)
