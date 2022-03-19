from rest_framework import serializers
from apps.users.models import TgUser
from apps.main.models import VideoPost
from apps.main import tasks as main_tasks


class TgUserCreateSerializer(serializers.ModelSerializer):
    """Сериализация данных юзера с тг бота."""

    class Meta:
        model = TgUser
        fields = ('id', 'uid', 'name', 'phone', 'created_at_timestamp')


class TgUserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = TgUser
        fields = ('id', 'uid', 'name', 'phone', 'created_at_timestamp')


class VideoPostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoPost
        fields = (
            'id', 'tg_user', 'first_name', 'last_name',
            'email', 'title', 'description', 'video_url', 'created_at_timestamp'
        )

    def create(self, validated_data):
        instance = super(VideoPostCreateSerializer, self).create(validated_data)
        main_tasks.post_video_download.delay(instance.pk)  # Скачивает видео из тг
        return instance
