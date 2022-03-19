from django.urls import path
from restapi.tgbot import views

app_name = 'tg_bot'
urlpatterns = [
    # USERS
    path('users/<int:uid>/', views.TgUserRetrieveAPIView.as_view()),
    path('users/', views.TgUserCreateAPIView.as_view()),
    # POST
    path('posts/', views.VideoPostCreateAPIVIew.as_view())

]
