from django.urls import path
from . import views

app_name = "admission"

urlpatterns = [

    path("", views.home, name="home"),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    path("student-dashboard/", views.student_dashboard, name="student_dashboard"),

    # IMPORTANT
    path("student-profile/", views.student_profile, name="student_profile"),

    path("apply-course/", views.apply_course, name="apply_course"),

    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("all-students/", views.all_students, name="all_students"),

    path(
        "update-status/<int:student_id>/<str:status>/",
        views.update_status,
        name="update_status"
    ),

    path(
        "download-application-pdf/",
        views.download_application_pdf,
        name="download_application_pdf"
    ),
]