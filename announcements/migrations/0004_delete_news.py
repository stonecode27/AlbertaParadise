# Generated by Django 4.0.3 on 2022-04-13 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_alter_response_body_news'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
    ]
