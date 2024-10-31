from django.urls import path

from . import views

urlpatterns = [
    path("<str:room_name>/", views.index, name="deviceindex"),
    path('publish', views.publish_message, name='publish'),
    path('leave-home', views.leave_home, name='leave_home'),
]