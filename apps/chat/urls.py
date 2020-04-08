# Django Library
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

# Localfolder Library
from .views import (
    chat_home, get_by_sid, get_client_name, get_history, register_message)
from .views.trigger import (
    DeleteTrigger, TriggerCreateView, TriggerDetailView, TriggerListView,
    TriggersUpdateView)

urlpatterns = [
    url(r'chat-home', chat_home, name='chat-home'),
    path('get_by_sid/<str:sid>', get_by_sid, name='get-by-sid'),
    path('get_client_name/<str:sid>', get_client_name, name='get-client-name'),
    path('get_history/<str:sid>', get_history),
    path('register_message', register_message),
    path('triggers', TriggerListView.as_view(), name='triggers'),
    path('trigger/add/', TriggerCreateView.as_view(), name='trigger-add'),
    path('trigger/<int:pk>/', TriggerDetailView.as_view(), name='trigger-detail'),
    path('trigger/<int:pk>/update', TriggersUpdateView.as_view(), name='trigger-update'),
    path('trigger/<int:pk>/delete/', DeleteTrigger, name='trigger-delete'),
]
