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

2. Add ``admin_views`` to ``INSTALLED_APPS`` in your ``settings.py``

3. Run the management command ``admin_views_install_templates`` to install the
   necessary modified admin index template to your project's TEMPLATE_DIRs.
   You will be prompted for which of these directories you would like it installed
   in if there are multiple directories defined.

Usage
=====

All of this magic happens in your model's admin definition.  You simply subclass your
admin from ``AdminViews`` instead of the standard ``admin.ModelAdmin``.
In this example we have a custom view that does nothing but redirect the user to CNN
and a direct URL link that goes to my company's homepage::

    from django.contrib import admin
    from django.shortcuts import redirect

    from admin_views.admin import AdminViews

    from example_app.models import TestModel

    class TestAdmin(AdminViews):
        admin_views = (
                        ('Redirect to CNN', 'redirect_to_cnn'),
                        ('Go to revsys.com', 'http://www.revsys.com'),
            )

        def redirect_to_cnn(self, *args, **kwargs):
            return redirect('http://www.cnn.com')

    admin.site.register(TestModel, TestAdmin)

These will now show up in the admin below the usual Django admin model CRUD interfaces
for `example_app` with a couple of different icons to distinquish between custom admin
views and a direct URL link.

With this third-party developers need only instruct their users to install their app,
``django-admin-views`` and run the ``admin_views_install_templates`` command.

Hope you find it useful and as always feedback is certainly welcome.

Screenshot
==========

`Example Screenshot <https://github.com/frankwiles/django-admin-views/wiki>`_

Author
======
Frank Wiles <frank@revsys.com> <http://www.revsys.com>

Attribution
===========
Blue link icon on direct URLs by http://www.doublejdesign.co.uk/

Admin view icon by http://www.fatcow.com/

