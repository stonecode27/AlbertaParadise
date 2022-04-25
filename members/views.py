from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import RegistrationForm, VerificationForm
from .models import OneTimeCode
from random import randint


class SignUpView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'members/signup.html'
    success_url = reverse_lazy('verify')


class VerifyView(FormView):
    form_class = VerificationForm
    template_name = 'members/verify.html'
    success_url = reverse_lazy('announcements')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        provided_code = request.POST['code']
        user = request.user
        actual_code = OneTimeCode.objects.get(user=user).code
        if provided_code == actual_code:
            OneTimeCode.objects.get(user=user).delete()
            verified_group = Group.objects.get(name='Verified')
            if not request.user.groups.filter(name='Verified').exists():
                verified_group.user_set.add(user)





