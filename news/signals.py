from random import randint

from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import News



@receiver(post_save, sender=News)
def send_news(sender, instance, created, **kwwargs):
    if created:
        subject = instance.subject
        text_content = instance.text_source
        html_content = instance.html_source
        msg = EmailMultiAlternatives(subject, text_content, "albertaparadise@mail.ru",
                                     User.objects.all().values_list('email', flat=True))
        msg.send()

