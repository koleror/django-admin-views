from django.contrib.auth import get_user_model
from django.test import TestCase


class AdminTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_superuser(
            username='foo',
            password='bar'
        )

    def test_display_admin(self):
        self.client.force_login(self.user)
        response = self.client.get('/admin/')

        self.assertEqual(response.status_code, 200)
        self.assertInHTML(
            """
            <th scope="row">
            <img src="/static/admin_views/icons/link.png" alt="Link to 'Go to google'">
            <a href="https://google.com">Go to google</a></th>
            """,
            response.rendered_content
        )
        self.assertInHTML(
            """
            <th scope="row">
            <img src="/static/admin_views/icons/view.png"
            alt="Custom admin view 'Redirect to CNN'">
            <a href="/admin/myapp/testmodel/redirect_to_cnn">Redirect to CNN</a></th>
            """,
            response.rendered_content
        )
