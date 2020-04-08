# Django Library
from django.contrib.auth import views as auth_views
from django.urls import path

# Thirdparty Library
from apps.payroll.views.employee import (
    DeleteEmployee, EmployeeCreateView, EmployeeDetailView, EmployeeListView,
    EmployeeUpdateView)

# Localfolder Library
from .views.department import (
    DeleteDepartment, DepartmentCreateView, DepartmentDetailView,
    DepartmentListView, DepartmentUpdateView)

app_name = 'payroll'

urlpatterns = [
    path('employee', EmployeeListView.as_view(), name='employee'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee-add'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/update', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', DeleteEmployee, name='employee-delete'),

    path('department', DepartmentListView.as_view(), name='department'),
    path('department/add/', DepartmentCreateView.as_view(), name='department-add'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('department/<int:pk>/update', DepartmentUpdateView.as_view(), name='department-update'),
    path('department/<int:pk>/delete/', DeleteDepartment, name='department-delete'),
]
