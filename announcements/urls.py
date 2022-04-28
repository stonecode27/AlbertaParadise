from django.urls import path, include
from .views import AnnouncementsView, AnnounceView, AnnounceAddView, AnnounceEditView, AnnounceDeleteView,\
    ResponseAddView, MyResponsesView, accept_response, decline_response

urlpatterns = [
    path('', AnnouncementsView.as_view(), name='announcements'),
    path('<int:pk>', AnnounceView.as_view(), name='announce'),
    path('create/', AnnounceAddView.as_view(), name='announce_add'),
    path('<int:pk>/edit/', AnnounceEditView.as_view(), name='announce_edit'),
    path('<int:pk>/delete/', AnnounceDeleteView.as_view(), name='announce_delete'),
    path('<int:pk>/response/', ResponseAddView.as_view(), name='response'),
    path('myresponses/', MyResponsesView.as_view(), name='my_responses'),
    path('responses/<int:response_id>/accept/', accept_response, name='accept'),
    path('responses/<int:response_id>/decline/', decline_response, name='decline')
]