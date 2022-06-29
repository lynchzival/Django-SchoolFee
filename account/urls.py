from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='account.login'),
    path('profile/edit/', login_required(views.profile_edit), name='account.profile.edit'),
    path('profile/', login_required(views.profile_view), name='account.profile'),
    path('logout/', login_required(views.logout_view), name='account.logout'),
    path('profile/password/', login_required(views.password_change), name='account.password.change'),
]
