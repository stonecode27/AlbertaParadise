from django.views.generic import CreateView, ListView
from .models import News


class RecentSendedNews(ListView):
    model = ListView
    queryset = News.objects.order_by('-id')



class NewsAddView(CreateView):
    model = News

