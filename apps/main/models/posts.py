import datetime

from django.db import models

from core.libs.utils import get_timestamp_from_datatime


def get_video_upload_path(instance, filename) -> str:
    """Путь загружаемого видео"""

    path = f'posts/videos/%Y/%m/%d/{filename}'
    return datetime.datetime.now().strftime(path)


class VideoPost(models.Model):
    """Модель отвечающая за посты"""

    tg_user = models.ForeignKey('users.TgUser', on_delete=models.CASCADE, related_name='video_posts',
                                help_text='ID пользователя тг')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(max_length=50, verbose_name='Электронная почта',)
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(max_length=500, verbose_name='Описание')
    video_url = models.CharField(  # TODO нужно скрыть это поле в url есть токен бота
        max_length=255, verbose_name='', help_text='url для скачивания видео с тг')
    video = models.FileField(upload_to=get_video_upload_path, verbose_name='Видео', null=True)
    is_download = models.BooleanField(default=False, verbose_name='Видео скачено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    class Meta:
        db_table = 'video_posts'
        verbose_name_plural = 'Видео посты'

    def __str__(self) -> str:
        return str(self.id)

    @property
    def created_at_timestamp(self) -> int:
        """Возвращает дату/время в timestamp"""

        return get_timestamp_from_datatime(self.created_at)
