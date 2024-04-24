from django.core.exceptions import ValidationError

from django.db import models

from eokul_app.models.base import BaseModel

def validate_grade(value):
    if not (1 <= int(value) <= 12):
        raise ValidationError(
            'Grade "%(value)s" is not valid. Grade must be between 1 and 12.',
            params={'value': value},
        )

def validate_tc(value):
    if (len(value) != 11 ):
        raise ValidationError(
            'TC No "%(value)s" is not valid. TC must be exactly 11 digits ',
            params={'value': value},
        )
    
def validate_std_no(value):
    if (len(value) != 6 ):
        raise ValidationError(
            'Student No "%(value)s" is not valid. Student No must be exactly 6 digits ',
            params={'value': value},
        )  

def validate_absentee(value):
    if (value < 0 ):
        raise ValidationError(
            'Absentee "%(value)s" is not valid. Absentee must be greater than 0',
            params={'value': value},
        ) 
        

class Student(BaseModel):
    class Meta(object):
        db_table = "student"
        app_label = "eokul_app"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tc_no = models.CharField(max_length=11 , validators=[validate_tc])
    std_no = models.CharField(max_length=6 , validators=[validate_std_no])
    grade = models.CharField(max_length=2, validators=[validate_grade])
    absentee = models.IntegerField(default=0, validators=[validate_absentee])
