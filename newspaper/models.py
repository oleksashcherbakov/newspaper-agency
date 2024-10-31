from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from newspaper_agency import settings


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(
        blank=True, null=True, default=0, validators=[MaxValueValidator(100)]
    )

    class Meta:
        ordering = ("first_name",)

    def __str__(self):
        return (
            f"years of experience number: {self.years_of_experience}, "
            f"username: {self.username}, "
            f"first_name: {self.first_name}, "
            f"last_name: {self.last_name}"
        )


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    published_date = models.DateField(blank=True, null=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="newspapers", blank=True
    )

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return f"Title: {self.title}, written by {self.publishers}"
