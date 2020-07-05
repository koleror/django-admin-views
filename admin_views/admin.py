from django.contrib import admin
from django.conf.urls import *
from django.conf import settings
from django.contrib.auth.decorators import permission_required


ADMIN_URL_PREFIX = getattr(settings, 'ADMIN_VIEWS_URL_PREFIX', '/admin')


class AdminViews(admin.ModelAdmin):
    """
    Standard admin subclass to handle easily adding views to
    the Django admin for an app
    """

    def __init__(self, *args, **kwargs):
        super(AdminViews, self).__init__(*args, **kwargs)
        self.direct_links = []
        self.local_view_names = []
        self.output_urls = []

    def get_urls(self):
        original_urls = super(AdminViews, self).get_urls()
        added_urls = []

        for link in self.admin_views:
            if hasattr(self, link[1]):
                view_func = getattr(self, link[1])
                if len(link) == 3:
                    # View requires permission
                    view_func = permission_required(
                        link[2], raise_exception=True)(view_func)
                added_urls.extend(
                    [
                        url(regex=r'^%s$' % link[1],
                            name=link[1],
                            view=self.admin_site.admin_view(view_func)
                            )
                    ]
                )
                self.local_view_names.append(link[0])

                try:
                    model_name = self.model._meta.model_name
                except AttributeError:
                    model_name = self.model._meta.module_name  # removed as of Django 1.8

                # Build URL from known info
                info = self.model._meta.app_label, model_name
                self.output_urls.append((
                    'view',
                    link[0],
                    "%s/%s/%s/%s" % (ADMIN_URL_PREFIX,
                                     info[0], info[1], link[1]),
                    link[2] if len(link) == 3 else None,
                )
                )
            else:
                self.direct_links.append(link)
                self.output_urls.append(
                    ('url', link[0], link[1], link[2] if len(link) == 3 else None))

        return added_urls + original_urls
