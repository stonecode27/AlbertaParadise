from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from .views import SignUpView, VerifyView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='members/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify/<user_id>', VerifyView.as_view(), name='verify')
]