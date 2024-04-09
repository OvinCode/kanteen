from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages, auth
from .models import User
# Create your views here.

def registerUser(request):
    if request.method == 'POST':

        form = UserForm(request.POST)
        if form.is_valid():
            # Access cleaned data and process it
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
    else:
        form = UserForm()

    return render(request, 'accounts/registerUser.html', {'form': form})

        # form = UserForm(request.POST)
        # first_name = form.cleaned_data['first_name']
        # last_name = form.cleaned_data['last_name']
        # username = form.cleaned_data['username']
        # email = form.cleaned_data['email']
        # password = form.cleaned_data['password']
        # user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        # user.save()

        # return render(request, 'accounts/registerUser.html', {'form': form})

def login(request):

    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myAccount')
    
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate [email,password]

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('myAccount')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    
    auth.logout(request)
    messages.info(request, 'You are now logged out.')
    return redirect('login')


def myAccount(request):
    return redirect('home')
