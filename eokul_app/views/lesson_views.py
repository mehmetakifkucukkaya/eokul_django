from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from eokul_app.permission import is_student_login

def list_lesson_by_std_no(req, std_no):
    if is_student_login(req, std_no):
        return HttpResponse(std_no + " için dersler")
    else:
        redirect_url = reverse("index")
        return HttpResponseRedirect(redirect_url)