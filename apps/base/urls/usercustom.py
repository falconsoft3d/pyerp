# Django Library
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

# Localfolder Library
from ..views import (
    ChangePasswordForm, DoChangePassword, UserCreateView, UserDeleteView,
    UserDetailView, UserListView, UserUpdateView)
from ..views.usercustom import (
    ActivateUserView, AvatarUpdateView, LogOutModalView, PasswordRecoveryView,
    ProfileView, SignUpView, cambio_clave)

app_name = 'PyUser'

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>', ActivateUserView.as_view(), name='activar'),
    path(
        'login/',
        LoginView.as_view(
            template_name='usercustom/login.html',
            # redirect_field_name='next',
            success_url='home'
        ),
        name='login'),
    path(
        'logout',
        LogoutView.as_view(next_page='PyUser:login'),
        name='logout'
    ),
    path('logoutmodal/', LogOutModalView.as_view(), name='logout-modal'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('changepasword', cambio_clave, name='change-password'),
    path(
        'password-recovery',
        PasswordRecoveryView.as_view(),
        name='password-recovery'
    ),
    path(
        'password-recovery/<uidb64>/<token>',
        PasswordRecoveryView.as_view(),
        name='password-set'
    ),
    path('avatar', AvatarUpdateView.as_view(), name='avatar'),

    path('users/list/', UserListView.as_view(), name='list'),
    path('user/add/', UserCreateView.as_view(), name='add'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
    path('user/change-password/<int:pk>', ChangePasswordForm, name='password-change'),
    path('user/change-password-confirm/<int:pk>', DoChangePassword, name='do-change-password'),
]
