from django.contrib import messages
from django.shortcuts import render, redirect
from . import models
from . import forms


def index(request):
    students = models.Student.objects.all()
    return render(request, 'student/index.html', {'students': students})


def create(request):
    form = forms.CreateStudentForm()
    return render(request, 'student/create.html', {'form': form})


def store(request):
    if request.method == 'POST':
        form = forms.CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully')
            return redirect('student.index')
        else:
            return render(request, 'student/create.html', {'form': form})
    else:
        return redirect('student.create')


def edit(request, sid):
    try:
        student = models.Student.objects.get(id=sid)
        form = forms.CreateStudentForm(instance=student)
        return render(request, 'student/edit.html', {'form': form})
    except models.Student.DoesNotExist:
        return redirect('student.index')


def update(request, sid):
    if request.method == 'POST':
        try:
            student = models.Student.objects.get(id=sid)
            form = forms.CreateStudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                messages.success(request, 'Student updated successfully')
                return redirect('student.index')
            else:
                return render(request, 'student/edit.html', {'form': form})
        except models.Student.DoesNotExist:
            return redirect('student.index')
    else:
        return redirect('student.index')


def delete(request, sid):
    if request.method == 'POST':
        try:
            student = models.Student.objects.get(id=sid)
            student.delete()
            messages.success(request, 'Student deleted successfully')
            return redirect('student.index')
        except models.Student.DoesNotExist:
            return redirect('student.index')
    else:
        return redirect('student.index')
