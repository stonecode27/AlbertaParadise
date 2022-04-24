from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    text_source = models.TextField()
    html_source = tinymce_models.HTMLField()
    send_date = models.DateTimeField()

    def __str__(self):
        return self.subject

