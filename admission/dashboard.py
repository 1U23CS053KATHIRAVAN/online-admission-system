from admin_tools.dashboard import modules, Dashboard
from .models import Student, Course


class CustomIndexDashboard(Dashboard):

    def init_with_context(self, context):

        # =============================
        # STUDENT STATISTICS
        # =============================
        total_students = Student.objects.count()
        approved = Student.objects.filter(status="Approved").count()
        pending = Student.objects.filter(status="Pending").count()
        rejected = Student.objects.filter(status="Rejected").count()

        self.children.append(modules.LinkList(
            'Admission Statistics',
            children=[
                f"Total Applications: {total_students}",
                f"Approved Students: {approved}",
                f"Pending Applications: {pending}",
                f"Rejected Applications: {rejected}",
            ]
        ))

        # =============================
        # COURSE STATISTICS
        # =============================
        courses = Course.objects.all()

        course_data = []

        for course in courses:
            count = Student.objects.filter(course=course).count()
            course_data.append(f"{course.name} : {count} students")

        self.children.append(modules.LinkList(
            'Course Statistics',
            children=course_data
        ))

        # =============================
        # RECENT APPLICATIONS
        # =============================
        self.children.append(modules.ModelList(
            'Recent Applications',
            models=('admission.models.Student',),
        ))