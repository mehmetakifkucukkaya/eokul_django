
from django.urls import path
from .views import *

urlpatterns = [
    path('', general_views.index)
]
