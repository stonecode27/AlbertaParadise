from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from .views import SignUpView, verify

urlpatterns = [
    path('login/', LoginView.as_view(template_name='members/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify/', verify)
]