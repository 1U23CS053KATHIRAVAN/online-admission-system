from django.contrib import admin
from django.utils.html import format_html
from .models import Student, Course


# ===============================
# COURSE ADMIN
# ===============================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "seat_limit",
        "total_students",
        "seats_remaining",
    )

    search_fields = ("name",)

    list_per_page = 10

    # -------------------------------
    # TOTAL STUDENTS IN COURSE
    # -------------------------------
    def total_students(self, obj):
        return Student.objects.filter(course=obj).count()

    total_students.short_description = "Total Students"

    # -------------------------------
    # REMAINING SEATS
    # -------------------------------
    def seats_remaining(self, obj):

        approved_students = Student.objects.filter(
            course=obj,
            status="Approved"
        ).count()

        remaining = obj.seat_limit - approved_students

        if remaining <= 0:
            return format_html(
                '<span style="color:red;font-weight:bold;">Full</span>'
            )

        return remaining

    seats_remaining.short_description = "Seats Left"


# ===============================
# STUDENT ADMIN
# ===============================
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "application_id",
        "full_name",
        "course",
        "status_badge",
        "document_button",
        "created_at",
    )

    list_filter = (
        "status",
        "course",
        "created_at",
    )

    search_fields = (
        "full_name",
        "phone",
        "application_id",
    )

    list_editable = (
        "course",
    )

    readonly_fields = (
        "application_id",
        "document_button",
        "created_at",
    )

    ordering = ("-created_at",)

    list_per_page = 10

    # -------------------------------
    # STATUS BADGE
    # -------------------------------
    def status_badge(self, obj):

        colors = {
            "Approved": "#28a745",
            "Pending": "#ffc107",
            "Rejected": "#dc3545",
            "Waiting": "#17a2b8",
        }

        color = colors.get(obj.status, "#6c757d")

        return format_html(
            '<span style="padding:6px 14px;border-radius:20px;color:white;background:{};font-weight:bold;">{}</span>',
            color,
            obj.status
        )

    status_badge.short_description = "Status"

    # -------------------------------
    # DOCUMENT BUTTON
    # -------------------------------
    def document_button(self, obj):

        if obj.document:
            return format_html(
                '<a style="background:#0d6efd;color:white;padding:6px 12px;border-radius:6px;text-decoration:none;" href="{}" target="_blank">View Document</a>',
                obj.document.url
            )

        return format_html(
            '<span style="color:gray;">No Document</span>'
        )

    document_button.short_description = "Document"