from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from eokul_app.models.student import Student

def student_login(request):
    if request.method == 'POST':
        tc_no = request.POST.get('tc_no')
        std_no = request.POST.get('std_no')
        student = Student.objects.filter(tc_no=tc_no, std_no=std_no).first()
        
        if student is not None:
            request.session['student'] = student.id
            redirect_url = reverse("student-dashboard")
            return HttpResponseRedirect(redirect_url)  # Öğrenci panosuna yönlendir
        else:
            return HttpResponse('Geçersiz öğrenci bilgileri.')

    return render(request, 'login.html')


def student_dashboard(req):
    
    if 'student' in req.session:
        return render(req, "eokul_app/student_dashboard.html")
    
    else :
        return HttpResponseRedirect('/')