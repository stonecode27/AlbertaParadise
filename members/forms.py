from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User, Group
from django.forms import CharField, PasswordInput, EmailField, TextInput, NumberInput, Form


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=TextInput(attrs={"autofocus": True}), label='Логин')
    password = CharField(
        label='Пароль',
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    error_messages = {
        "invalid_login": (
            "Неправильно введен логин или пароль, либо пользователь не зарегистрирован"
        ),
        "inactive": ("This account is inactive."),
    }


class RegistrationForm(UserCreationForm):
    password1 = CharField(
        label='Пароль',
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="Придумайте пароль, который сможете вспомнить, но не сможет подобрать злоумышленник",
    )
    password2 = CharField(
        label="Подтверждение пароля",
        widget=PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Введите пароль повторно для подтверждения",
    )
    email = EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password1",
                  "password2",)
        labels = {"username": "Имя пользователя"}
        help_texts = {"username": "Буквы, цифры и следующие символы @/./+/-/_."}
        field_classes = {'username': UsernameField}

class VerificationForm(Form):
    code = CharField(min_length=6, max_length=6, label='Код подтверждения:',
                     help_text='Код подтверждения был отправлен на почту, указанную при регистрации. '
                               'Если код не приходит - проверьте папку "спам"',
                     widget=NumberInput)
