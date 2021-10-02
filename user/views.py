from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from mainframe.models import *
from user.forms import SignUpForm
from properties.models import LovedProperties, Property

basic_features = Basic.objects.all()


def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()

    context = {
        'basics': basic_features,
        'form': form
    }
    return render(request, 'user/login.html', context)


def Register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    context = {
        'basics': basic_features,
        'form': form
    }
    return render(request, 'user/register.html', context)


def Logout(request):
    logout(request)
    return redirect('/')


def Dashboard(request):
    loved_properties = LovedProperties.objects.all()

    propertyId = request.GET.get('property-delete')
    
    if propertyId != None:
        deletedProperty = LovedProperties.objects.get(id=propertyId)
        deletedProperty.delete()

    context = {
        'basics': basic_features,
        'loved_properties': loved_properties

    }
    return render(request, 'user/dashboard.html', context)
