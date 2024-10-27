from django.contrib.auth import get_user_model
from django.urls import reverse

from django.test import TestCase, Client

from newspaper.models import Newspaper, Topic

NEWSPAPERS_URL = reverse("newspaper:newspaper-list")
TOPICS_URL = reverse("newspaper:topic-list")
REDACTORS_URL = reverse("newspaper:redactor-list")


def sample_redactor():
    return get_user_model().objects.create_user(
        username="redactor",
        email="<EMAIL>",
        password="<PASSWORD>",
        years_of_experience=5,
        first_name="redactor_name",
        last_name="redactor_last_name",
    )


def sample_topic():
    return Topic.objects.create(name="test")


class NewspaperTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(NEWSPAPERS_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateNewspaperTestCase(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            email="<EMAIL>",
            username="testuser",
        )
        self.client.force_login(self.user)

    def test_retrieve_newspapers(self):
        topic = sample_topic()

        newspaper = Newspaper.objects.create(
            title="test_title",
            content="test_content",
            topic=topic,
        )
        newspaper.save()
        newspaper.publishers.add(self.user)
        newspapers = Newspaper.objects.all()

        response = self.client.get(NEWSPAPERS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["newspaper_list"]), list(newspapers))
        self.assertTemplateUsed(
            response,
            "newspaper/newspaper_list.html"
        )


class TopicTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(TOPICS_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTopicTestCase(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            email="<EMAIL>",
            username="testuser",
        )
        self.client.force_login(self.user)

    def test_retrieve_topics(self):
        topics = Topic.objects.all()

        response = self.client.get(TOPICS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["topic_list"]), list(topics))
        self.assertTemplateUsed(
            response,
            "newspaper/topic_list.html"
        )


class RedactorTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(REDACTORS_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateRedactorTestCase(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            email="<EMAIL>",
            username="testuser",
        )
        self.client.force_login(self.redactor)

    def test_retrieve_redactors(self):
        redactors = get_user_model().objects.all()

        response = self.client.get(REDACTORS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(redactors)
        )
        self.assertTemplateUsed(
            response,
            "newspaper/redactor_list.html"
        )
