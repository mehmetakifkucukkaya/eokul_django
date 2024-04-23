from django.db import models


class Student(models.Model):

    class Meta(object):
        db_table = "student"
        app_label = "eokul_app"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tc_no = models.CharField(max_length=11)
    std_no = models.CharField(max_length=6)
    grade = models.CharField(max_length=2)
    absentee = models.IntegerField(default=0)

    """Her tabloya özel zaman damgaları, deleted_time soft delete yapmak için kullanılacak"""
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    deleted_time = models.DateTimeField()

    