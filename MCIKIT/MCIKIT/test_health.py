from django.test import SimpleTestCase
from django.urls import reverse


class HealthCheckTests(SimpleTestCase):
    def test_get_returns_expected_json(self):
        response = self.client.get(reverse("health"), secure=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_post_is_rejected(self):
        response = self.client.post(reverse("health"), secure=True)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.headers["Allow"], "GET")

    def test_protected_profile_redirects_to_login(self):
        profile_path = reverse("users:user_profile")
        login_path = reverse("users:login")

        response = self.client.get(profile_path, secure=True)

        self.assertRedirects(
            response, f"{login_path}?next={profile_path}", fetch_redirect_response=False
        )
