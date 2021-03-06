from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, through='AnoCat')
    creation_date = models.DateTimeField(auto_now_add=True)
    body = tinymce_models.HTMLField()

    def __str__(self):
        return self.header


class AnoCat(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    to_announce = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    body = models.TextField(max_length=254)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Condition(models.IntegerChoices):
        idle = 0
        declined = 1
        accepted = 2

    status = models.IntegerField(choices=Condition.choices, auto_created=0, default=0)

    def accept(self):
        self.status = 2
        self.save()

    def decline(self):
        self.status = 1
        self.save()

    def __str__(self):
        return self.body[:20]
