from django.forms import ModelForm
from .models import News
from tinymce.widgets import TinyMCE


class NewsAddForm(ModelForm):
    class Meta:
        model = News
        fields = ['subject', 'text_source', 'html_source']
        labels = {'subject': "Subject письма",
                  "text_source": "Текстовая версия письма",
                  "html_source":' HTML-версия письма'}

        widgets = {'html_source': TinyMCE}
