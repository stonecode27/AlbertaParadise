from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import RegistrationForm
from .models import OneTimeCode
from random import randint


class SignUpView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'members/signup.html'
    success_url = 'members/verify'

    # def post(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)
    #     OneTimeCode.objects.create(user=request.user, code=''.join([str(randint(0, 9)) for _ in range(6)]))


def verify(request):
    return HttpResponse('Подтверди')