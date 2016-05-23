import os
from shutil import rmtree

import sys
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command


if sys.version_info < (3,):
    def b(x):
        return x
else:
    def b(x):
        return x.encode("ascii")


class AdminViewsTests(TestCase):
    """ Test django-admin-views """

    def setUp(self):
        # Create a superuser to login as
        self.superuser = User.objects.create_superuser('frank', 'frank@revsys.com', 'pass')

    def test_urls_showup(self):
        self.client.login(username='frank', password='pass')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

        # Make sure our links and images show up
        self.assertTrue(b('/static/admin_views/icons/view.png') in response.content)
        self.assertTrue(b('/static/admin_views/icons/link.png') in response.content)
        self.assertTrue(b('/admin/example_app/testmodel/process') in response.content)
        self.assertTrue(b('http://www.ljworld.com') in response.content)

        # Test that we can go to the URLs
        response = self.client.get('/admin/example_app/testmodel/process')
        self.assertEqual(response.status_code, 302)
