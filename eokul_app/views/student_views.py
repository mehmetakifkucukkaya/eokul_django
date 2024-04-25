import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from eokul_app.models.student import Student

def student_login(request):
    if request.method == 'POST':
        tc_no = request.POST.get('tc_no')
        std_no = request.POST.get('std_no')
        student = Student.objects.filter(tc_no=tc_no, std_no=std_no).first()
        
        if student is not None:
            serialized_student = {
                'id' : student.id,
                "first_name" : student.first_name,
                'last_name' : student.last_name,
                "tc_no" : student.tc_no,
                "std_no" : student.std_no,
                "grade" : student.grade,
                "absentee" : student.absentee
            }
            request.session['student'] = json.dumps(serialized_student)
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