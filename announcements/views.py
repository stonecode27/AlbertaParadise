from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Announcement
from .forms import AnnouncementForm


class AnnouncementsView(ListView):
    model = Announcement
    template_name = "announcements/announcements.html"


class AnnounceView(DetailView):
    model = Announcement
    template_name = "announcements/announce.html"
    context_object_name = "announce"


class AnnounceAddView(CreateView):
    model = Announcement
    template_name = 'announcements/announce_create.html'
    form_class = AnnouncementForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AnnounceAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('announce', kwargs={'pk': self.object.id})


class AnnounceEditView(UpdateView):
    model = Announcement
    template_name = 'announcements/announce_edit.html'
    form_class = AnnouncementForm

    def get_success_url(self):
        return reverse('announce', kwargs={'pk': self.object.id})


class AnnounceDeleteView(DeleteView):
    model = Announcement
    template_name = 'announcements/announce_delete.html'
    success_url = reverse_lazy('announcements')

