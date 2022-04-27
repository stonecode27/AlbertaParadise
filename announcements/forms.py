from django.forms import ModelForm
from .models import Announcement
from tinymce.widgets import TinyMCE

class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['header', 'category', 'body']
        labels = {'header': "Заголовок", "category": "Категория", "body":''}
        widgets = {'body': TinyMCE}
