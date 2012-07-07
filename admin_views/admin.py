from functools import update_wrapper
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.defaults import *

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
                added_urls.extend(
                        patterns('',
                            url(regex=r'%s' % link[1],
                                name=link[1],
                                view=self.admin_site.admin_view(view_func))
                        )
                )
                self.local_view_names.append(link[0])

                # Build URL from known info
                info = self.model._meta.app_label, self.model._meta.module_name
                self.output_urls.append(
                    (
                        'view',
                         link[0],
                         "/admin/%s/%s/%s" % (info[0],
                                              info[1],
                                              link[1])
                    )
                )

            else:
                self.direct_links.append(link)
                self.output_urls.append(('url', link[0], link[1]))

        return added_urls + original_urls

