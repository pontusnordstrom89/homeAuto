from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('publish', views.publish_message, name='publish'),
    path('set-state', views.set_get_state_indicator, name='set_get_state'),
]