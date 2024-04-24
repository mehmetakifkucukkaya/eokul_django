from django.db import models
from django.core.validators import MinLengthValidator
from eokul_app.models.base import BaseModel

class Administrator(BaseModel):
    MUDUR = 'Mudur'
    OGRETMEN = 'Ogretmen'

    AUTHORITY_CHOICES = [
        (MUDUR, 'Müdür'),
        (OGRETMEN, 'Öğretmen'),
    ]

    class Meta(object):
        db_table = "administrator"
        app_label = "eokul_app"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=16,validators=[MinLengthValidator(6)])
    password = models.CharField(max_length=16 ,validators=[MinLengthValidator(8)])
    authority = models.CharField(max_length=15, choices=AUTHORITY_CHOICES)

