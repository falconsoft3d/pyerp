# Django Library
from django.urls import path

# Localfolder Library
from .views.other_views import IndexEasy

app_name = 'home'
urlpatterns = [
    path('', IndexEasy, name='home_easy'),
]
