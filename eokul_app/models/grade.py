from django.db import models

from eokul_app.models.base import BaseModel
from eokul_app.models.lesson import Lesson
from eokul_app.models.student import Student


class Grade(BaseModel):

    class Meta(object):
        db_table = "grade"
        app_label = "eokul_app"

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    exam1_grade = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    exam2_grade = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    