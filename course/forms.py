from django import forms
from course.models import Course, Fee


class CreateCourseForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    level = forms.CharField(label='Level', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    total_amount = forms.FloatField(widget=forms.HiddenInput(), label='Total Amount', required=False)
    course_desc = forms.CharField(label='Description', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'rows': '3'}))

    class Meta:
        model = Course
        fields = ['name', 'level', 'total_amount', 'course_desc']


class CreateFeeForm(forms.ModelForm):
    fee_desc = forms.CharField(label='Description', max_length=100, required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'rows': '3'}))
    amount = forms.FloatField(label='Amount', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Fee
        fields = ['fee_desc', 'amount']
