# Django Library
from django.urls import path

# Localfolder Library
from ..views import (
    AccountMoveCreateView, AccountMoveDeleteView, AccountMoveDetailView,
    AccountMoveListView, AccountMoveUpdateView, move_state)

app_name = 'PyAccountMove'

urlpatterns = [
    # ========================= Account Move URL's ========================= #
    path('', AccountMoveListView.as_view(), name='list'),
    path('add/', AccountMoveCreateView.as_view(), name='add'),
    path('<int:pk>/', AccountMoveDetailView.as_view(), name='detail'),
    path('<int:pk>/update', AccountMoveUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', AccountMoveDeleteView.as_view(), name='delete'),
    path('state/<int:pk>/<int:state>', move_state, name='state'),
]
