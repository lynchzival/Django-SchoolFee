from django import forms

from course.models import Course
from enrollment.models import Enroll
from student.models import Student


class CreateEnrollForm(forms.ModelForm):
    student_id = forms.ModelChoiceField(queryset=Student.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}),
                                        label='Student', initial=1)

    course_id = forms.ModelChoiceField(queryset=Course.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control'}),
                                       label='Course')

    total_fee = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = Enroll
        fields = ['student_id', 'course_id', 'total_fee']
