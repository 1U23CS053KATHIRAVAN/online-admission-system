from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Course, Student


# ==============================
# Home
# ==============================

def home(request):
    return render(request, "admission/home.html")


# ==============================
# Register
# ==============================

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("admission:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("admission:register")

        User.objects.create_user(username=username, email=email, password=password)

        messages.success(request, "Registration successful. Please login.")
        return redirect("admission:login")

    return render(request, "admission/register.html")


# ==============================
# Login
# ==============================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect("admission:admin_dashboard")
            else:
                return redirect("admission:student_dashboard")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "admission/login.html")


# ==============================
# Logout
# ==============================

@login_required
def logout_view(request):
    logout(request)
    return redirect("admission:login")


# ==============================
# Student Dashboard
# ==============================

@login_required
def student_dashboard(request):

    student = Student.objects.filter(user=request.user).first()

    return render(
        request,
        "admission/student_dashboard.html",
        {"student": student}
    )


# ==============================
# Student Profile (NEW FEATURE)
# ==============================

@login_required
def student_profile(request):

    student = Student.objects.filter(user=request.user).first()

    return render(
        request,
        "admission/student_profile.html",
        {"student": student}
    )


# ==============================
# Apply Course
# ==============================

@login_required
def apply_course(request):

    courses = Course.objects.all()

    # Prevent multiple applications
    if Student.objects.filter(user=request.user).exists():
        messages.warning(request, "You have already submitted an application.")
        return redirect("admission:student_dashboard")

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        dob = request.POST.get("dob")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        course_id = request.POST.get("course")
        document = request.FILES.get("document")

        if not course_id:
            messages.error(request, "Please select a course.")
            return redirect("admission:apply_course")

        course = get_object_or_404(Course, id=course_id)

        Student.objects.create(
            user=request.user,
            full_name=full_name,
            dob=dob,
            phone=phone,
            address=address,
            course=course,
            document=document,
            status="Pending"
        )

        messages.success(request, "Application submitted successfully!")
        return redirect("admission:student_dashboard")

    return render(
        request,
        "admission/apply_course.html",
        {"courses": courses}
    )


# ==============================
# Admin Dashboard
# ==============================

@login_required
@staff_member_required
def admin_dashboard(request):

    students = Student.objects.all().order_by("-id")

    total_students = students.count()
    pending = students.filter(status="Pending").count()
    approved = students.filter(status="Approved").count()
    rejected = students.filter(status="Rejected").count()

    context = {
        "students": students,
        "total_students": total_students,
        "pending": pending,
        "approved": approved,
        "rejected": rejected,
    }

    return render(
        request,
        "admission/admin_dashboard.html",
        context
    )


# ==============================
# All Students
# ==============================

@login_required
@staff_member_required
def all_students(request):

    students = Student.objects.all().order_by("-id")

    return render(
        request,
        "admission/all_students.html",
        {"students": students}
    )


# ==============================
# Update Status
# ==============================

@login_required
@staff_member_required
def update_status(request, student_id, status):

    student = get_object_or_404(Student, id=student_id)

    student.status = status
    student.save()

    messages.success(request, "Status updated successfully!")

    return redirect("admission:admin_dashboard")


# ==============================
# Download Application PDF
# ==============================

@login_required
def download_application_pdf(request):

    student = Student.objects.filter(user=request.user).first()

    template = get_template("admission/application_pdf.html")
    html = template.render({"student": student})

    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="application.pdf"'

    pisa.CreatePDF(html, dest=response)

    return response