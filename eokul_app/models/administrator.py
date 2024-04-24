from django.db import models

from eokul_app.models.base import BaseModel


class Administrator(BaseModel):

    class Meta(object):
        db_table = "administrator"
        app_label = "eokul_app"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    authority = models.CharField(max_length=15)

  