from django.db.models.signals import post_save, pre_save
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from .models import Response



@receiver(post_save, sender=Response)
def response_notification(sender, instance, created, **kwwargs):
    if created:
        user = instance.to_announce.author
        subject = f"""{user.username}, у вас новый отклик!"""
        text_content = f'Здравствуйте, {user.username}. На ваше объявление {instance.to_announce.header} появился отклик!'
        msg = EmailMultiAlternatives(subject, text_content, "albertaparadise@mail.ru", [user.email])

        msg.send()

@receiver(post_save, sender=Response)
def accept_notification(sender, instance, created, **kwargs):
    if not(created) and instance.status == 2:
        user = instance.author
        subject = f"""{user.username}, ваш отклик принят!"""
        text_content = f'Здравствуйте, {user.username}. ваш отклик на объявление "{instance.to_announce.header[:20]}" принят! Скорее свяжитесь с {instance.to_announce.author.username}. '
        msg = EmailMultiAlternatives(subject, text_content, "albertaparadise@mail.ru", [user.email])

        msg.send()