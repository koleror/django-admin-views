import os
from shutil import rmtree
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command

class AdminViewsTests(TestCase):
    """ Test django-admin-views """

    def setUp(self):
        # Create a superuser to login as
        self.superuser = User.objects.create_superuser('frank', 'frank@revsys.com', 'pass')
        self.TEMPLATE_DIR = settings.TEMPLATE_DIRS[0]

    def test_urls_showup(self):
        self.client.login(username='frank', password='pass')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

        # Make sure our links and images show up
        self.assertTrue('/static/admin_views/icons/view.png' in response.content)
        self.assertTrue('/static/admin_views/icons/link.png' in response.content)
        self.assertTrue('/admin/example_app/testmodel/process' in response.content)
        self.assertTrue('http://www.ljworld.com' in response.content)

        # Test that we can go to the URLs
        response = self.client.get('/admin/example_app/testmodel/process')
        self.assertEqual(response.status_code, 302)

    def test_management_command(self):
        call_command('admin_views_install_templates')
        self.assertTrue(os.path.exists(os.path.join(self.TEMPLATE_DIR, 'admin/index.html')))

    def test_management_command_with_args(self):
        call_command('admin_views_install_templates', os.path.join(self.TEMPLATE_DIR))
        self.assertTrue(os.path.exists(os.path.join(self.TEMPLATE_DIR, 'admin/index.html')))

    def tearDown(self):
        admin_subdir = os.path.join(self.TEMPLATE_DIR, 'admin/')

        if os.path.exists(admin_subdir):
            rmtree(admin_subdir)

