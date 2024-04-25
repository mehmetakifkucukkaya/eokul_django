

from django.db import models
from eokul_app.models.base import BaseModel
from eokul_app.models.lesson import Lesson
from eokul_app.models.student import Student


class StudentsLesson(BaseModel):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    
    class Meta(object):
        db_table = "students_lesson"
        app_label = "eokul_app"