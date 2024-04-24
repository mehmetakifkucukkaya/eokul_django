from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from eokul_app.models.student import Student

def student_login(request):
    if request.method == 'POST':
        tc_no = request.POST.get('tc_no')
        std_no = request.POST.get('std_no')
        student = Student.objects.filter(tc_no=tc_no, std_no=std_no).first()
        
        if student is not None:
            request.session['student'] = student.id
            return HttpResponseRedirect('/student/dashboard/')  # Öğrenci panosuna yönlendir
        else:
            return HttpResponse('Geçersiz öğrenci bilgileri.')

    return render(request, 'login.html')


def student_dashboard(req):
    
    if 'student' in req.session:
        return HttpResponse("Student Dashboard")
    
    else :
        return HttpResponseRedirect('/')