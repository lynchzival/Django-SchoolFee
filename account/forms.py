from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control form-control-user',
                                                       'placeholder': 'Enter username...'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control form-control-user',
                                                           'placeholder': 'Password'}))


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(label="First Name", widget=TextInput(attrs={'class': 'form-control form-control-user'}),
                                 required=False)

    last_name = forms.CharField(label="Last Name", widget=TextInput(attrs={'class': 'form-control form-control-user'}),
                                required=False)

    username = forms.CharField(label="Username", widget=TextInput(attrs={'class': 'form-control form-control-user'}))
    email = forms.EmailField(label="Email", widget=TextInput(attrs={'class': 'form-control form-control-user'}))

    password = None

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
                raise forms.ValidationError('Email already exists')
        return email

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password",
                                   widget=PasswordInput(attrs={'class': 'form-control form-control-user'}))

    new_password1 = forms.CharField(label="New Password",
                                    widget=PasswordInput(attrs={'class': 'form-control form-control-user'}))

    new_password2 = forms.CharField(label="Confirm Password",
                                    widget=PasswordInput(attrs={'class': 'form-control form-control-user'}))
