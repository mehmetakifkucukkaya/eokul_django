from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(null=True, blank=True)
    deleted_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
