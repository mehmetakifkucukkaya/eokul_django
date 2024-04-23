from django.db import models

from eokul_app.models.lesson import Lesson
from eokul_app.models.student import Student


class WeeklyShedule(models.Model):

    class Meta(object):
        db_table = "weekly_shedule"
        app_label = "eokul_app"

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    day_of_week = models.CharField(max_length=20)
    time = models.TimeField()

    """Her tabloya özel zaman damgaları, deleted_time soft delete yapmak için kullanılacak"""
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    deleted_time = models.DateTimeField()