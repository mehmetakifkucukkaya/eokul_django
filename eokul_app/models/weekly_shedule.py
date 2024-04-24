from django.db import models

from eokul_app.models.base import BaseModel
from eokul_app.models.lesson import Lesson
from eokul_app.models.student import Student


class WeeklyShedule(BaseModel):

    class Meta(object):
        db_table = "weekly_shedule"
        app_label = "eokul_app"

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    day_of_week = models.CharField(max_length=20)
    time = models.TimeField()
