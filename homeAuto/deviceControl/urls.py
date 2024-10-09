from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('publish', views.publish_message, name='publish'),
    path("lobby", views.lobby, name="lobby"),
    path("<str:room_name>/", views.room, name="room"),
]