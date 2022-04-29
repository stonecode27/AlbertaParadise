from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from .models import News
from .forms import NewsAddForm
from django.contrib.auth.mixins import PermissionRequiredMixin


class RecentNews(ListView, PermissionRequiredMixin):
    model = ListView
    queryset = News.objects.order_by('-id')
    template_name = 'news/adminnews.html'
    permission_required = ['add_logentry', 'change_logentry', 'delete_logentry', 'view_logentry', 'add_announcement',
                           'add_announcements', 'change_announcement', 'change_announcements', 'delete_announcement',
                           'delete_announcements', 'view_announcement', 'view_announcements', 'add_anocat', 'change_anocat',
                           'delete_anocat', 'view_anocat', 'add_categories', 'add_category', 'change_categories',
                           'change_category', 'delete_categories', 'delete_category', 'view_categories', 'view_category',
                           'add_news', 'change_news', 'delete_news', 'view_news', 'add_response', 'add_responses',
                           'change_response', 'change_responses', 'delete_response', 'delete_responses', 'view_response',
                           'view_responses', 'add_group', 'change_group', 'delete_group', 'view_group', 'add_permission',
                           'change_permission', 'delete_permission', 'view_permission', 'add_user', 'change_user',
                           'delete_user', 'view_user', 'add_onetimecode', 'change_onetimecode', 'delete_onetimecode',
                           'view_onetimecode', 'add_news', 'change_news', 'delete_news', 'view_news']


class NewsAddView(CreateView, PermissionRequiredMixin):
    model = News
    form_class = NewsAddForm
    template_name = 'news/news_create.html'
    success_url = reverse_lazy('recent_news')
    permission_required = ['add_logentry', 'change_logentry', 'delete_logentry', 'view_logentry', 'add_announcement',
                           'add_announcements', 'change_announcement', 'change_announcements', 'delete_announcement',
                           'delete_announcements', 'view_announcement', 'view_announcements', 'add_anocat', 'change_anocat',
                           'delete_anocat', 'view_anocat', 'add_categories', 'add_category', 'change_categories',
                           'change_category', 'delete_categories', 'delete_category', 'view_categories', 'view_category',
                           'add_news', 'change_news', 'delete_news', 'view_news', 'add_response', 'add_responses',
                           'change_response', 'change_responses', 'delete_response', 'delete_responses', 'view_response',
                           'view_responses', 'add_group', 'change_group', 'delete_group', 'view_group', 'add_permission',
                           'change_permission', 'delete_permission', 'view_permission', 'add_user', 'change_user',
                           'delete_user', 'view_user', 'add_onetimecode', 'change_onetimecode', 'delete_onetimecode',
                           'view_onetimecode', 'add_news', 'change_news', 'delete_news', 'view_news']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewsAddView, self).form_valid(form)
