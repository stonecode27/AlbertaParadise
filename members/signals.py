from random import randint

from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import OneTimeCode



@receiver(post_save, sender=User)
def send_verification_code(sender, instance, created, **kwwargs):
    if created:
        print(f'{instance.username} has been created')
        registered_group = Group.objects.get(name='Registered')
        registered_group.user_set.add(instance)
        new_user = OneTimeCode.objects.create(user=instance, code=''.join([str(randint(0, 9)) for _ in range(6)]))
        new_user.save()
        subject = f"""{instance.email}, подтвердите ваш email!"""
        text_content = f'Здравствуйте, {instance.username}, добро пожаловать на сайт Alberta Paradise. Код подтверждения {new_user.code}'
        msg = EmailMultiAlternatives(subject, text_content, "albertaparadise@mail.ru", [instance.email])
        msg.send()

