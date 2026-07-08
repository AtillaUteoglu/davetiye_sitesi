from django.urls import path
from davetiye_app import views

urlpatterns = [
    path('', views.davetiye, name='davetiye'),
]
