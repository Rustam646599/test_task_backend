# PYTHON

# LIBS
from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework_tracking.mixins import LoggingMixin
from restapi.tgbot import serializers as tg_bot_serializers
from apps.users.models import TgUser


class TgUserCreateAPIView(LoggingMixin, generics.CreateAPIView):
    """
        Создает ТГ пользователя
    """
    serializer_class = tg_bot_serializers.TgUserCreateSerializer
    permission_classes = (permissions.AllowAny,)  # FIXME для теста
    logging_methods = ('POST',)


class TgUserRetrieveAPIView(LoggingMixin, generics.RetrieveAPIView):
    """
        Получить пользователя
    """
    queryset = TgUser.objects.all()
    serializer_class = tg_bot_serializers.TgUserRetrieveSerializer
    permission_classes = (permissions.AllowAny,)  # FIXME для теста
    logging_methods = ('GET',)
    lookup_field = 'uid'


class VideoPostCreateAPIVIew(LoggingMixin, generics.CreateAPIView):
    """
        Опубликовать видео
    """
    serializer_class = tg_bot_serializers.VideoPostCreateSerializer
    permission_classes = (permissions.AllowAny,)  # FIXME для теста
    logging_methods = ('POST',)
