from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.main import models


@admin.register(models.VideoPost)
class VideoPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'title', 'is_download', 'created_at', 'post_video')
    list_display_links = ('id', 'title')
    list_filter = ('created_at', 'is_download')
    search_fields = ('title', 'first_name', 'id')
    exclude = ('video_url',)
    readonly_fields = (
        'tg_user', 'first_name', 'last_name',
        'email', 'title', 'description',
        'video', 'is_download', 'created_at'
    )

    def post_video(self, post_video):
        if post_video.video:
            url = post_video.video.url
            return mark_safe(f'<video width="320" height="150" controls> <source src="{url}" type="video/mp4"></video>')
        else:
            return mark_safe('Видео еще не загружено')

    post_video.short_description = 'Видео'
