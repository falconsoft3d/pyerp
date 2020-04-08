# Django Library
from django.contrib.auth import views as auth_views
from django.urls import path

# Localfolder Library
from .views.bim_budget import (
    BimBudgetCreateView, BimBudgetDetailView, BimBudgetListView,
    BimBudgetUpdateView, DeleteBimBudget)
from .views.bim_project import (
    BimProjectCreateView, BimProjectDetailView, BimProjectListView,
    BimProjectUpdateView, DeleteBimProject)

app_name = 'bim'



urlpatterns = [
    path('budget', BimBudgetListView.as_view(), name='budget'),
    path('budget/add/', BimBudgetCreateView.as_view(), name='budget-add'),
    path('budget/<int:pk>/', BimBudgetDetailView.as_view(), name='budget-detail'),
    path('budget/<int:pk>/update', BimBudgetUpdateView.as_view(), name='budget-update'),
    path('budget/<int:pk>/delete/', DeleteBimBudget, name='budget-delete'),

    path('project', BimProjectListView.as_view(), name='project'),
    path('project/add/', BimProjectCreateView.as_view(), name='project-add'),
    path('project/<int:pk>/', BimProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/update', BimProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', DeleteBimProject, name='project-delete'),
]
