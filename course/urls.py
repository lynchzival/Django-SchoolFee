from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', login_required(views.index), name='course.index'),
    path('create/', login_required(views.create), name='course.create'),
    path('store/', login_required(views.store), name="course.store"),
    path('edit/<int:cid>/', login_required(views.edit), name="course.edit"),
    path('update/<int:cid>/', login_required(views.update), name="course.update"),
    path('delete/<int:cid>/', login_required(views.delete), name="course.delete"),
]
