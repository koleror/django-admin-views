Overview
========

While "the admin is not your app", it is often useful to be able to easily add
a bit of functionality to the admin for internal staff or other internal users
that are tech savvy enough to use the admin.

There are several third party project such as
`AdminPlus <https://github.com/jsocol/django-adminplus>`_, but they require the
user to redefine the Admin.site object.  This is fine for developers who are
setting up a Django project, but not ideal for developers who are writing
third party tools for other developers to use in their projects.

django-admin-views attempts to solve this by simply overriding the admin
templates to provide two features:

1. Easily define custom admin views and link them on the admin pages
2. Easily add in external URL links

Installation Steps
==================

1. ``pip install django-admin-views``

2. Add ``admin_views`` to ``INSTALLED_APPS`` in your ``settings.py`` before admin site, i.e. ``django.contrib.admin``.

If you are using a custom Admin Site, you'll need to configure the ``ADMIN_VIEWS_SITE`` setting to point to your admin site instance:

.. code-block:: python

    ADMIN_VIEWS_SITE = "myproject.admin.admin_site"

Usage
=====

All of this magic happens in your model's admin definition.  Subclass your
admin from ``AdminViews`` instead of the standard ``admin.ModelAdmin``.
In this example we have a custom view that does nothing but redirect the user to CNN
and a direct URL link that goes to Google:

.. code-block:: python

    from django.contrib import admin
    from django.shortcuts import redirect

    from admin_views.admin import AdminViews

    from example_app.models import TestModel

    class TestAdmin(AdminViews):
        admin_views = (
            ("Redirect to CNN", "redirect_to_cnn"),
            ("Go to google.com", "https://google.com"),
        )

        def redirect_to_cnn(self, *args, **kwargs):
            return redirect("https://www.cnn.com")

    admin.site.register(TestModel, TestAdmin)

These will now show up in the admin below the usual Django admin model CRUD interfaces
for ``example_app`` with a couple of different icons to distinquish between custom admin
views and a direct URL link.

With this third-party developers need only instruct their users to install their app
and ``django-admin-views``.

Hope you find it useful and as always feedback is certainly welcome.

Screenshot
==========

.. image:: https://raw.githubusercontent.com/koleror/django-admin-views/master/screenshots/admin.png

Author
======
Frank Wiles frank@revsys.com

Maintainer
==========
Hugo Defrance defrance.hugo@gmail.com
