from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.shortcuts import render
from django.urls import path


class HomePageTest (TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('Home/')
        self.assertEqual(found.func, home_page)
        home_page = None
