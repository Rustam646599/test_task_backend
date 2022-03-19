from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from restapi.tgbot import urls

tg_bot_schema_view = get_schema_view(
   openapi.Info(
      title="Telegram bot api",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   patterns=[
       re_path(r'api/tg-bot/v1/', include(urls))
   ]
)
