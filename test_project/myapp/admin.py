from admin_views.admin import AdminViews
from django.contrib import admin
from django.shortcuts import redirect

from .models import TestModel


class TestAdmin(AdminViews):
    admin_views = (
        ('Redirect to CNN', 'redirect_to_cnn'),  # Admin view
        ('Go to google', 'https://google.com'),  # Direct url
    )

    def redirect_to_cnn(self, *args, **kwargs):
        return redirect('https://www.cnn.com')


admin.site.register(TestModel, TestAdmin)
