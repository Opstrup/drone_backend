from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from backend_api.views import index_page


class IndexPageTest(TestCase):
    """
    Test class for the index page.
    """