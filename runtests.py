#!/usr/bin/env python
import os
import sys
from os.path import dirname, abspath

from django.conf import settings


TEST_ROOT = os.path.dirname(__file__)
PROJECT_ROOT = os.path.join(TEST_ROOT, '../../example_project/example_project/')

if not settings.configured:
    settings.configure(
        DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': 'foo.db',
                }
        },
        SITE_ID = 1,
        COVERAGE_MODULE_EXCLUDES = [
            'tests$', 'settings$', 'urls$',
            'common.views.test', '__init__', 'django',
        ],
        ROOT_URLCONF = 'example_project.urls',
        WSGI_APPLICATION = 'example_project.wsgi.application',
        TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates/"),),
        STATIC_URL='/static/',
        INSTALLED_APPS = [
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django_coverage',
            'admin_views',
            'example_project.example_app',
            'django.contrib.admin',
        ],
    )

from django.test.simple import DjangoTestSuiteRunner
from django_coverage.coverage_runner import CoverageRunner

def runtests(*test_args):
    if not test_args:
        test_args = ['admin_views']
    parent = dirname(abspath(__file__))
    example_project = os.path.join(parent, 'example_project')
    sys.path.insert(0, example_project)
    runner = CoverageRunner()
    failures = runner.run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
