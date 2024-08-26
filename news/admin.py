from django.contrib import admin
from .models import News, Comments


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'newscreator', 'created')
    list_display_links = ('title',)
    search_fields = ('title', 'newscreator')


class CommentsAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('commentlocation', 'author', 'info', 'created')
    list_display_links = ('commentlocation',)
    search_fields = ('commentlocation', 'author', 'info')


admin.site.register(News, NewsAdmin)


admin.site.register(Comments, CommentsAdmin)
