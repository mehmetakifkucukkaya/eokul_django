from django.shortcuts import render


def login(request):
    return render(request, template_name='eokul_app/login.html')