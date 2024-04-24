from django.db import models

from eokul_app.models.base import BaseModel


class Lesson(BaseModel):

    class Meta(object):
        db_table = "lesson"
        app_label = "eokul_app"

    lesson_code = models.CharField(max_length=6)
    lesson_text = models.CharField(max_length=50)

    