from django.urls import path

from . import views

urlpatterns = [
    path("<str:room_name>/", views.index, name="index"),
    path('publish', views.publish_message, name='publish'),
]