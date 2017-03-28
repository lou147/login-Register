from django.shortcuts import render


def register(request):

    return render(request, 'register.html', {'test': 'test123123'})


def user_login(request):

    return render(request, 'login.html', {})
