from django.contrib import admin
from django.db.models import Count

from apps.users import models


@admin.register(models.User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'username', 'is_staff', 'is_active')
    list_display_links = ('id', 'username')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'id')


@admin.register(models.TgUser)
class TgUserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'uid', 'get_posts_count', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'uid', 'id')
    readonly_fields = ('name', 'phone', 'uid')

    def get_posts_count(self, tg_user):
        """Возвращает количество постов юзера"""

        return tg_user.posts_count

    get_posts_count.short_description = 'Количество загруженных видео'

    def get_queryset(self, request):
        """Оптимизация запросов"""

        queryset = super().get_queryset(request).annotate(
            posts_count=Count('video_posts')
        )
        return queryset
