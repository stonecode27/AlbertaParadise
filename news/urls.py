from django.urls import path, include
from .views import RecentNews, NewsAddView

urlpatterns = [
    path('', RecentNews.as_view(), name='recent_news'),
    path('create/', NewsAddView.as_view(), name='create_news')
]
