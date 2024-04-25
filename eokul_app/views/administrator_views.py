import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from eokul_app.permission import is_admin_login
from eokul_app.models import Administrator


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admin = Administrator.objects.filter(username =username, password = password ).first()
        
        
        
        if admin is not None:
            serialized_admin = {
                'id' : admin.id,
                "first_name" : admin.first_name,
                'last_name' : admin.last_name,
                "username" : admin.username,
                "password" : admin.password,
                "authority" : admin.authority
            }
            request.session['admin'] = json.dumps(serialized_admin)
            redirect_url = reverse("admin-dashboard")
            return HttpResponseRedirect(redirect_url)  # Admin panosuna yönlendir
        else:
            return HttpResponse('Geçersiz admin bilgileri.')

    return render(request, 'login.html')


def admin_dashboard(req, username):
    
    if is_admin_login(req, username):
        return render(req, "eokul_app/admin_dashboard.html")
    
    else :
        redirect_url = reverse("index")
        return HttpResponseRedirect(redirect_url)