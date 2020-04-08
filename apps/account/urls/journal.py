# Django Library
from django.urls import path

# Localfolder Library
from ..views import (
    JournalAutoComplete, JournalCreateView, JournalDeleteView,
    JournalDetailView, JournalListView, JournalUpdateView)

app_name = 'PyJournal'

urlpatterns = [
    # ========================= Account Plan URL's ========================= #
    path('', JournalListView.as_view(), name='list'),
    path('add/', JournalCreateView.as_view(), name='add'),
    path('<int:pk>/', JournalDetailView.as_view(), name='detail'),
    path('<int:pk>/update', JournalUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', JournalDeleteView.as_view(), name='delete'),
    # ==================== Auto completado de Productos ==================== #
    path('autocomplete', JournalAutoComplete.as_view(), name='autocomplete'),
]
