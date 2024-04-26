from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from eokul_app.models.weekly_shedule import WeeklyShedule
from eokul_app.permission import is_student_login
from eokul_app.models import Student, StudentsLesson, Lesson

def list_lesson_by_std_no(req, std_no):
    if is_student_login(req, std_no):
        student = Student.objects.filter(std_no = std_no).first()
        student_lessons = list(StudentsLesson.objects.filter(student = student.id))
        lessons = Lesson.objects.all()
        # for lesson in student_lessons:
        #     lessons.add(Lesson.objects.filter(pk = lesson).first())
        
        
            
        context = {
            "lessons" : lessons,
        }
        
        return render(req, "eokul_app/students_lesson.html", context)
    else:
        redirect_url = reverse("index")
        return HttpResponseRedirect(redirect_url)