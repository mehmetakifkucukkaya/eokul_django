from django.db import models


class Administrator(models.Model):

    class Meta(object):
        db_table = "administrator"
        app_label = "eokul_app"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    authority = models.CharField(max_length=15)

    """Her tabloya özel zaman damgaları, deleted_time soft delete yapmak için kullanılacak"""
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    deleted_time = models.DateTimeField()