from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from restapi.tgbot.swagger import tg_bot_schema_view

urlpatterns = [

    path('api/tg-bot/v1/', include('restapi.tgbot.urls')),
    path('admin/', admin.site.urls),
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    # path('jet/', include('jet.urls', 'jet')),

]
urlpatterns += [
    re_path(r'^swagger/tg-bot/v1/$', tg_bot_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^docs/tg-bot/v1/$', tg_bot_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
