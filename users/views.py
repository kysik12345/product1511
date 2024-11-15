from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from project.settings import LOGIN_REDIRECT_URL

from .forms import SignForm
from .models import Profile


User = get_user_model()


User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, phone_number=form.changed_data.get('phone_number'))
            raw_password = form.changed_data.get('passwors1')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('/')
    
    else:
        form = SignForm()
    return render(request, 'users/register.html', context = {'form': form} )
def log_in(request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                url = request.GET.get('next', LOGIN_REDIRECT_URL)
                return redirect(url)
        context = {'form': form}
        return render(request, template_name='users/login.html', context=context)

@login_required    
def log_out(request):
    log_out(request)
    return redirect('/')



@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user != user:
       raise PermissionDenied()

    context = {'user': user, 'title': 'Информация о профиле'}
    return render(request, template_name='users/profile.html', context=context)