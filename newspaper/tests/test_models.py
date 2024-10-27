from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Topic, Newspaper


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


class ModelTests(TestCase):
    def test_topic_str(self):
        topic = sample_topic()
        self.assertEqual(str(topic), topic.name)

    def test_redactor_str(self):
        redactor = sample_redactor()
        self.assertEqual(
            str(redactor),
            f"years of experience number: {redactor.years_of_experience}, "
            f"username: {redactor.username}, "
            f"first_name: {redactor.first_name}, "
            f"last_name: {redactor.last_name}",
        )

    def test_newspaper_str(self):
        topic = sample_topic()
        redactor = sample_redactor()

        newspaper = Newspaper.objects.create(
            title="test_title",
            content="test_content",
            topic=topic,
        )
        newspaper.save()
        newspaper.publishers.add(redactor)

        self.assertEqual(
            str(newspaper),
            f"Title: {newspaper.title}, " f"written by {newspaper.publishers}",
        )

    def test_create_redactor_with_years_of_experience(self):
        redactor = sample_redactor()

        self.assertEqual(redactor.username, "redactor")
        self.assertEqual(redactor.years_of_experience, 5)
        self.assertTrue(redactor.check_password("<PASSWORD>"))
