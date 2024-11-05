from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="<PASSWORD>",
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_superuser(
            username="redactor",
            password="<PASSWORD>",
            years_of_experience=5,
        )

    def test_redactor_years_of_experience_listed(self):
        url = reverse("admin:newspaper_redactor_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.redactor.years_of_experience)

    def test_redactor_detail_years_of_experience_listed(self):
        url = reverse(
            "admin:newspaper_redactor_change",
            args=[self.redactor.id]
        )
        response = self.client.get(url)
        self.assertContains(response, self.redactor.years_of_experience)
