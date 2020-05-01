from django.urls import path
from . import views

app_name = 'imovie'

urlpatterns = [
    path('', views.download_trailer, name='list')
]
