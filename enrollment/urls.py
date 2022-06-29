from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', login_required(views.index), name='enroll.index'),
    path('create/', login_required(views.create), name="enroll.create"),
    path('get_course_total_amount/', login_required(views.get_course_total_amount),
         name="enroll.get_course_total_amount"),
    path('store/', login_required(views.store), name="enroll.store"),
    path('edit/<int:eid>', login_required(views.edit), name="enroll.edit"),
    path('update/<int:eid>', login_required(views.update), name="enroll.update"),
    path('delete/<int:eid>', login_required(views.delete), name="enroll.delete"),
]
