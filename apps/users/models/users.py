from django.db import models
from django.contrib.auth.models import AbstractUser
from core.libs.utils import get_timestamp_from_datatime


class User(AbstractUser):
    """Модель юзера"""
    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return str(self.username)


class TgUser(models.Model):
    """Пользователи тг-бота"""
    uid = models.IntegerField(unique=True, db_index=True, verbose_name='ID пользователя',
                              help_text='ID пользователя в телеграмме')
    name = models.CharField(max_length=50, verbose_name='Имя', help_text='')
    phone = models.CharField(max_length=12, verbose_name='Мобильный номер', help_text='')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации', help_text='')

    class Meta:
        db_table = 'telegram_users'
        verbose_name_plural = 'Пользователи телеграмм бота'

    def __str__(self) -> str:
        return str(self.id)

    @property
    def created_at_timestamp(self) -> int:
        """Возвращает дату/время в timestamp"""
        return get_timestamp_from_datatime(self.created_at)

