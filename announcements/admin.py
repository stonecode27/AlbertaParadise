from django.contrib import admin
from announcements.models import Announcement, Category, Response, AnoCat
from news.models import News

admin.site.register(Category)
admin.site.register(Response)
admin.site.register(AnoCat)
admin.site.register(News)


class AnoCatInline(admin.TabularInline):
    model = AnoCat

class AnoAdmin(admin.ModelAdmin):
    inlines = [AnoCatInline,]

admin.site.register(Announcement, AnoAdmin)