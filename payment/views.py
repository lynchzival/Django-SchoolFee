from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect

from course.models import Fee
from enrollment.models import Enroll
from payment.forms import CreatePaymentForm, DateSelectionForm
from payment.models import Payment, Action


def index(request):
    payments = Payment.objects.all()
    return render(request, 'payment/index.html', {'payments': payments})


def create(request):
    form = CreatePaymentForm()
    return render(request, 'payment/create.html', {'form': form})


def store(request):
    if request.method == 'POST':
        form = CreatePaymentForm(request.POST)
        if form.is_valid():

            with transaction.atomic():
                instace = form.save(commit=False)
                instace.created_by = request.user
                instace.save()
                Action.objects.create(sender=request.user, verb="created this payment", target=form.instance)
                messages.success(request, 'Payment created successfully')

            return redirect('payment.index')
        else:
            return render(request, 'payment/create.html', {'form': form})

    else:
        return redirect('payment.create')


def get_outstanding_balance(request):
    balance = Enroll.objects.get(id=request.POST.get('enroll_id')).balance()
    return JsonResponse({'data': balance})


def edit(request, pid):
    try:
        payment = Payment.objects.get(id=pid)
        form = CreatePaymentForm(instance=payment)
        return render(request, 'payment/edit.html', {'form': form})
    except Payment.DoesNotExist:
        messages.error(request, 'Payment does not exist')
        return redirect('payment.index')


def update(request, pid):
    if request.method == 'POST':
        try:
            payment = Payment.objects.get(id=pid)
            form = CreatePaymentForm(request.POST, instance=payment)
            if form.is_valid():

                with transaction.atomic():
                    form.save()
                    Action.objects.create(sender=request.user, verb="updated this payment", target=form.instance)
                    messages.success(request, 'Payment updated successfully')

                return redirect('payment.index')

            else:
                return render(request, 'payment/edit.html', {'form': form})
        except Payment.DoesNotExist:
            messages.error(request, 'Payment does not exist')
            return redirect('payment.index')
    else:
        return redirect('payment.index')


def delete(request, pid):
    if request.method == 'POST':
        try:
            payment = Payment.objects.get(id=pid)

            with transaction.atomic():
                Action.objects.create(sender=request.user, verb="deleted this payment", target=payment)
                payment.delete()
                messages.success(request, 'Payment deleted successfully')

            return redirect('payment.index')
        except Payment.DoesNotExist:
            messages.error(request, 'Payment does not exist')
            return redirect('payment.index')
    else:
        return redirect('payment.index')


def invoice(request, pid):
    try:
        current = Payment.objects.get(id=pid)
        # history = Payment.objects.filter(enroll_id=current.enroll_id)
        fees = Fee.objects.filter(course_id=current.enroll_id.course_id)

        history = Payment.objects.filter(enroll_id=current.enroll_id, id__lte=current.id)
        return render(request, 'payment/invoice.html', {'pay_current': current, 'pay_history': history, 'fees': fees})
    except Payment.DoesNotExist:
        messages.error(request, 'Payment does not exist')
        return redirect('payment.index')


def report(request):
    month = request.GET.get('month')
    year = request.GET.get('year')

    if month and year:
        payments = Payment.objects.filter(date_created__month=month, date_created__year=year)
    else:
        payments = Payment.objects.all()

    form = DateSelectionForm()
    return render(request, 'payment/report.html', {'form': form, 'payments': payments})
