# Generated by Django 5.1 on 2024-09-14 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_topic_newspaper'),
    ]

    operations = [
        migrations.AddField(
            model_name='redactor',
            name='years_of_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]