from django.core.exceptions import ValidationError

from django.db import models

from eokul_app.models.base import BaseModel

def validate_grade(value):
    if not (1 <= int(value) <= 12):
        raise ValidationError(
            'Grade "%(value)s" is not valid. Grade must be between 1 and 12.',
            params={'value': value},
        )

class Student(BaseModel):
    class Meta(object):
        db_table = "student"
        app_label = "eokul_app"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tc_no = models.CharField(max_length=11)
    std_no = models.CharField(max_length=6)
    grade = models.CharField(max_length=2, validators=[validate_grade])
    absentee = models.IntegerField(default=0)
