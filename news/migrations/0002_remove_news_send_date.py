# Generated by Django 4.0.3 on 2022-04-28 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='send_date',
        ),
    ]