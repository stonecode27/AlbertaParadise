from django.urls import path, include
from .views import AnnouncementsView

urlpatterns = [
    path('', AnnouncementsView.as_view(), name='announcements')
]