from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.admin import site

from ..admin import AdminViews

register = template.Library()

@register.simple_tag
def get_admin_views(app_name):
    output = []
    STATIC_URL = settings.STATIC_URL

    for k, v in site._registry.items():
        if app_name.lower() not in str(k._meta):
            continue

        if isinstance(v, AdminViews):
            for type, name, link in v.output_urls:
                if type == 'url':
                    img_url = "%sadmin_views/icons/link.png" % STATIC_URL
                    alt_text = "Link to '%s'" % name
                else:
                    img_url = "%sadmin_views/icons/view.png" % STATIC_URL
                    alt_text = "Custom admin view '%s'" % name

                output.append(
                        """<tr>
                              <th scope="row">
                                  <img src="%s" alt="%s" />
                                  <a href="%s">%s</a></th>
                              <td>&nbsp;</td>
                              <td>&nbsp;</td>
                           </tr>
                        """ % (img_url, alt_text, link, name)
                    )

    return "".join(output)

