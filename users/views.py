from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdationForm ,ProfileUpdationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for { username }, Now login!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form, 'title': 'Register!'})




@login_required
def profile(request):
    if request.method == 'POST':
        u_update = UserUpdationForm(request.POST, instance=request.user)
        p_update = ProfileUpdationForm(request.POST, request.FILES, instance=request.user.profile)
        if u_update.is_valid() and p_update.is_valid():
            u_update.save()
            p_update.save()
            messages.success(request, "Your information has been updated!")
            return redirect('profile')
    else:
        u_update = UserUpdationForm(instance=request.user)
        p_update = ProfileUpdationForm(instance=request.user.profile)
    context = {
        'u_update':u_update,
        'u_profile':p_update
    }
    return render(request, 'users/profile.html', context)