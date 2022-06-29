from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from account.forms import LoginForm, EditProfileForm, ChangePasswordForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if 'remember' not in request.POST:
                request.session.set_expiry(0)

            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('index')
        else:
            return render(request, 'account/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    else:
        return redirect('index')


def profile_edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account.profile')
        else:
            return render(request, 'account/profile.edit.html', {'form': form})
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'account/profile.edit.html', {'form': form})


def profile_view(request):
    return render(request, 'account/profile.html')


def password_change(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('account.profile')
        else:
            return render(request, 'account/profile.password.html', {'form': form})
    else:
        form = ChangePasswordForm(request.user)
        return render(request, 'account/profile.password.html', {'form': form})
