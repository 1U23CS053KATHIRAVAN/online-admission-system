from django.db import models
from django.contrib.auth.models import User
import uuid


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    seat_limit = models.PositiveIntegerField(default=30)

    def __str__(self):
        return self.name


class Student(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Waiting", "Waiting"),
    ]

    # Application Number
    application_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    # User
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # Personal Details
    full_name = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    # Documents
    document = models.FileField(
        upload_to="documents/",
        max_length=255
    )

    # Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    # Admin Remarks
    admin_remark = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name if self.full_name else self.user.username
