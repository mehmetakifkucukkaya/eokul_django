from django.db import models
from django.core.validators import RegexValidator

from eokul_app.models.base import BaseModel

class Lesson(BaseModel):

    class Meta(object):
        db_table = "lesson"
        app_label = "eokul_app"

    # yalnızca harfle başlamak için 
    starts_with_letter = RegexValidator(
        regex=r'^[a-zA-Z].*$', 
        message="Lesson code must start with a letter."
    )

    lesson_code = models.CharField(
        max_length=6,
        validators=[starts_with_letter]
    )
    lesson_text = models.CharField(max_length=50)
