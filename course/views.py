from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect

from course import models
from course.forms import CreateCourseForm, CreateFeeForm


def index(request):
    courses = models.Course.objects.all()
    return render(request, 'course/index.html', {'courses': courses})


def create(request):
    course = CreateCourseForm()
    fee = CreateFeeForm()
    return render(request, 'course/create.html', {'course': course, 'fee': fee})


def store(request):
    if request.method == 'POST':
        course_valid = CreateCourseForm(request.POST)
        fee_valid = CreateFeeForm(request.POST)

        if course_valid.is_valid() and fee_valid.is_valid():
            fee_desc = request.POST.getlist('fee_desc[]')
            fee_amount = request.POST.getlist('amount[]')

            if len(fee_desc) > 0 and len(fee_amount) > 0:
                with transaction.atomic():
                    course = course_valid.save()
                    for i in range(len(fee_desc)):
                        models.Fee.objects.create(course=course, fee_desc=fee_desc[i], amount=fee_amount[i])
                    messages.success(request, 'Course created successfully')
                    return redirect('course.index')
            else:
                messages.warning(request, 'Please add atleast one fee')
                return redirect('course.create')

        else:
            return render(request, 'course/create.html', {'course': course_valid, 'fee': fee_valid})
    else:
        return redirect('course.create')


def edit(request, cid):
    try:
        course = models.Course.objects.get(id=cid)
        fee = models.Fee.objects.filter(course=course)
        course_form = CreateCourseForm(instance=course)
        fee_form = CreateFeeForm(instance=fee.last())
        return render(request, 'course/edit.html', {'course': course_form, 'fee': fee_form, 'fees': fee})
    except models.Course.DoesNotExist:
        return redirect('course.index')


def update(request, cid):
    if request.method == 'POST':
        try:
            course = models.Course.objects.get(id=cid)
            fee = models.Fee.objects.filter(course=course)
            course_form = CreateCourseForm(request.POST, instance=course)
            fee_form = CreateFeeForm(request.POST, instance=fee.last())
            if course_form.is_valid() and fee_form.is_valid():
                fee_desc = request.POST.getlist('fee_desc[]')
                fee_amount = request.POST.getlist('amount[]')

                if len(fee_desc) > 0 and len(fee_amount) > 0:
                    with transaction.atomic():
                        fee.delete()
                        course_form.save()
                        for i in range(len(fee_desc)):
                            models.Fee.objects.create(course=course, fee_desc=fee_desc[i], amount=fee_amount[i])
                        messages.success(request, 'Course updated successfully')
                        return redirect('course.index')
                else:
                    messages.warning(request, 'Please add atleast one fee')
                    return redirect('course.edit', cid=cid)
            else:
                return render(request, 'course/edit.html', {'course': course_form, 'fee': fee_form, 'fees': fee})
        except models.Course.DoesNotExist:
            return redirect('course.index')
    else:
        return redirect('course.index')


def delete(request, cid):
    try:
        course = models.Course.objects.get(id=cid)
        course.delete()
        messages.success(request, 'Course deleted successfully')
        return redirect('course.index')
    except models.Course.DoesNotExist:
        return redirect('course.index')
