
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", administrator_views.admin_login, name="admin_login"),
    path("student/", student_views.student_login , name="student_login"),
    path("admin/dashboard/", administrator_views.admin_dashboard, name="admin-dashboard"),
    path("student/dashboard/", student_views.student_dashboard, name="student-dashboard"),
    path('', general_views.login, name="index")
]
