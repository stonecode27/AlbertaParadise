from django.apps import AppConfig


class MembersConfig(AppConfig):
    name = 'members'

    # нам надо переопределить метод ready, чтобы при готовности нашего приложения импортировался модуль со всеми функциями обработчиками
    def ready(self):
        import members.signals