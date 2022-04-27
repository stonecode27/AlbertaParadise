from django.urls import path, include
from .views import AnnouncementsView, AnnounceView, AnnounceAddView, AnnounceEditView, AnnounceDeleteView

urlpatterns = [
    path('', AnnouncementsView.as_view(), name='announcements'),
    path('<int:pk>', AnnounceView.as_view(), name='announce'),
    path('create/', AnnounceAddView.as_view(), name='announce_add'),
    path('<int:pk>/edit/', AnnounceEditView.as_view(), name='announce_edit'),
    path('<int:pk>/delete/', AnnounceDeleteView.as_view(), name='announce_delete')

]