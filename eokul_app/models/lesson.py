from django.db import models


class Lesson(models.Model):

    class Meta(object):
        db_table = "lesson"
        app_label = "eokul_app"

    lesson_code = models.CharField(max_length=6)
    lesson_text = models.CharField(max_length=50)

    """Her tabloya özel zaman damgaları, deleted_time soft delete yapmak için kullanılacak"""
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    deleted_time = models.DateTimeField()