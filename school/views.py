from datetime import datetime

from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render

from enrollment.models import Enroll
from payment.models import Payment, Action
from student.models import Student


def index(request):
    payment = Payment.objects.all().order_by('-date_created')[:10]

    earnings = {}
    for month in range(1, 13):
        earnings[month] = Payment.objects.filter(date_created__month=month).aggregate(Sum('amount'))['amount__sum'] or 0

    monthly = earnings[datetime.now().month]
    annual = sum(earnings.values())
    enroll = Enroll.objects.all().count()
    students = Student.objects.all().count()

    return render(request, 'index.html', {
        'payment': payment,
        'earnings': earnings,
        'monthly': monthly,
        'annual': annual,
        'enroll': enroll,
        'students': students,
    })


def activity(request):
    payment_activity = Action.objects.all().order_by('-created')
    return render(request, 'activity/index.html', {'payment_activity': payment_activity})
