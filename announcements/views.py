from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Announcement


class AnnouncementsView(ListView):
    model = Announcement
    template_name = "announcements/announcements.html"


