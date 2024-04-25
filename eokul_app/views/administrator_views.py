from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from eokul_app.models import Administrator


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admin = Administrator.objects.filter(username =username, password = password )
        
        if admin is not None:
            request.session['admin'] = admin.id
            redirect_url = reverse("admin-dashboard")
            return HttpResponseRedirect(redirect_url)  # Admin panosuna yönlendir
        else:
            return HttpResponse('Geçersiz admin bilgileri.')

    return render(request, 'login.html')


def admin_dashboard(req):
    return HttpResponse("Admin Sayfası")