from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', login_required(views.index), name='payment.index'),
    path('create/', login_required(views.create), name='payment.create'),
    path('store/', login_required(views.store), name='payment.store'),
    path('get_outstanding_balance/', login_required(views.get_outstanding_balance),
         name='payment.get_outstanding_balance'),
    path('edit/<int:pid>/', login_required(views.edit), name='payment.edit'),
    path('update/<int:pid>/', login_required(views.update), name='payment.update'),
    path('delete/<int:pid>/', login_required(views.delete), name='payment.delete'),
    path('invoice/<int:pid>', login_required(views.invoice), name='payment.invoice'),
    path('report/', login_required(views.report), name='payment.report'),
]
