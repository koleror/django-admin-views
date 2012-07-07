from django.contrib import admin
from admin_views.admin import AdminViews, admin_view
from django.shortcuts import redirect

from example_project.example_app.models import TestModel

class TestAdmin(AdminViews):
    admin_views = (
            ('Process This', 'process'),              # Admin view
            ('Go to LJW', 'http://www.ljworld.com'),  # Direct URL
    )

    @admin_view
    def process(self, *args, **kwargs):
        return redirect('http://www.cnn.com')

admin.site.register(TestModel, TestAdmin)
