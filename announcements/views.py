from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import ResponseFilter
from .models import Announcement, Response
from .forms import AnnouncementForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class AnnouncementsView(ListView, LoginRequiredMixin):
    model = Announcement
    template_name = "announcements/announcements.html"


class AnnounceView(DetailView, PermissionRequiredMixin):
    model = Announcement
    template_name = "announcements/announce.html"
    context_object_name = "announce"
    permission_required = ['announcements.add_announcement', 'announcements.change_announcement', 'announcements.delete_announcement',
                           'announcements.view_announcement', 'announcements.add_response', 'announcements.view_responses']


class AnnounceAddView(CreateView, PermissionRequiredMixin):
    model = Announcement
    template_name = 'announcements/announce_create.html'
    form_class = AnnouncementForm
    permission_required = ['add_announcement', 'change_announcement', 'delete_announcement',
                           'view_announcement', 'add_response', 'view_responses']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AnnounceAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('announce', kwargs={'pk': self.object.id})


class AnnounceEditView(UpdateView, PermissionRequiredMixin):
    model = Announcement
    template_name = 'announcements/announce_edit.html'
    form_class = AnnouncementForm
    permission_required = ['add_announcement', 'change_announcement', 'delete_announcement',
                           'view_announcement', 'add_response', 'view_responses']

    def get_success_url(self):
        return reverse('announce', kwargs={'pk': self.object.id})


class AnnounceDeleteView(DeleteView, PermissionRequiredMixin):
    model = Announcement
    template_name = 'announcements/announce_delete.html'
    success_url = reverse_lazy('announcements')
    permission_required = ['add_announcement', 'change_announcement', 'delete_announcement',
                           'view_announcement', 'add_response', 'view_responses']


class ResponseAddView(CreateView, PermissionRequiredMixin):
    model = Response
    template_name = 'announcements/response_create.html'
    fields = ['body']
    permission_required = ['add_announcement', 'change_announcement', 'delete_announcement',
                           'view_announcement', 'add_response', 'view_responses']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.to_announce = Announcement.objects.get(pk=self.kwargs['pk'])
        return super(ResponseAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('announcements')


class MyResponsesView(ListView, PermissionRequiredMixin):
    model = Response
    template_name = 'announcements/my_responses.html'
    permission_required = ['add_announcement', 'change_announcement', 'delete_announcement',
                           'view_announcement', 'add_response', 'view_responses']

    def get_queryset(self):
        return Response.objects.filter(to_announce__author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        return context


def accept_response(request, response_id, *args, **kwargs):
    current = Response.objects.get(id=response_id)
    if current and current.status == 0:
        current.accept()
    return HttpResponseRedirect(reverse('my_responses'))


def decline_response(request, response_id, *args, **kwargs):
    current = Response.objects.get(id=response_id)
    if current and current.status == 0:
        current.decline()
    return HttpResponseRedirect(reverse('my_responses'))