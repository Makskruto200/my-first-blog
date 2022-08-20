from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            request.session['name'] = request.POST['username']
            return redirect('/app/profile/')

        else:
            return redirect('/login/')

    return render(request, 'main/authorization.html')


def create_user(request):
    if request.method == "POST":
        try:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.last_name = 'user'
            user.save()
        except:
            return redirect('/create_user/')

        return redirect('/login/')
    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


