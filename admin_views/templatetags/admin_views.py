import sys
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.html import format_html_join

from .. import conf
from ..admin import AdminViews
from ..compat import import_string

site = import_string(conf.ADMIN_VIEWS_SITE)

register = template.Library()


if sys.version_info < (3,):
    import codecs

    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x


@register.simple_tag
def get_admin_views(app, perms):
    output = []
    STATIC_URL = settings.STATIC_URL

    for k, v in site._registry.items():
        app_name = app.get('app_label', app['name'].lower())
        if app_name not in str(k._meta):
            continue

        if isinstance(v, AdminViews):
            for type, name, link, perm in v.output_urls:
                if perm and perm not in perms:
                    continue
                if type == 'url':
                    img_url = "%sadmin_views/icons/link.png" % STATIC_URL
                    alt_text = "Link to '%s'" % name
                else:
                    img_url = "%sadmin_views/icons/view.png" % STATIC_URL
                    alt_text = "Custom admin view '%s'" % name

                output.append(list(map(u, (img_url, alt_text, link, name))))

    output = sorted(output, key=lambda x: x[3])

    return mark_safe(
        format_html_join(
            u(''),
            u("""<tr>
                    <th scope="row">
                    <img src="{}" alt="{}" />
                    <a href="{}">{}</a></th>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                  </tr>
              """), output)
      )
