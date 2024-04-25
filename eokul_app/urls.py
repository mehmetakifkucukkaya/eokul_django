
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", administrator_views.admin_login, name="admin_login"),
    path("student/", student_views.student_login , name="student_login"),
    path("admin/<str:username>", administrator_views.admin_dashboard, name="admin-dashboard"),
    path("student/<str:std_no>", student_views.student_dashboard, name="student-dashboard"),
    path("student/<str:std_no>/lesson", lesson_views.list_lesson_by_std_no, name="lesson"),
    path('', general_views.login, name="index")
]
