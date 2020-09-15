from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
            username=request.POST["username"], password=request.POST["password1"])
            return HttpResponseRedirect('/apple/')
        return HttpResponseRedirect('account/signup')

    else:
        return render(request, 'account/signup.html')


def login(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/apple/')
        else:
            return render(request, 'account/signup.html')
    else:
        return render(request, 'account/login.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/apple/')
