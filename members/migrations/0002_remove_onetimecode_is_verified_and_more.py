# Generated by Django 4.0.3 on 2022-04-24 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onetimecode',
            name='is_verified',
        ),
        migrations.AlterField(
            model_name='onetimecode',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]