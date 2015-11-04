from django.conf import settings


ADMIN_VIEWS_SITE = getattr(settings, 'ADMIN_VIEWS_SITE', 'django.contrib.admin.site')
