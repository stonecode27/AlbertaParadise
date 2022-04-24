# Generated by Django 4.0.3 on 2022-04-11 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('body', tinymce.models.HTMLField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('to_announce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcements.announcements')),
            ],
        ),
        migrations.CreateModel(
            name='AnoCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcements.announcements')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcements.categories')),
            ],
        ),
        migrations.AddField(
            model_name='announcements',
            name='category',
            field=models.ManyToManyField(through='announcements.AnoCat', to='announcements.categories'),
        ),
    ]