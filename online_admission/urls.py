from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# =====================================
# CUSTOM ADMIN BRANDING
# =====================================
admin.site.site_header = "Online Admission Administration"
admin.site.site_title = "Admission Admin Portal"
admin.site.index_title = "Welcome to Online Admission Management System"


# =====================================
# URL PATTERNS
# =====================================
urlpatterns = [

    # Admin Panel
    path("admin/", admin.site.urls),

    # Main Application
    path(
        "",
        include(
            ("admission.urls", "admission"),
            namespace="admission"
        )
    ),
]


# =====================================
# STATIC & MEDIA FILES (DEVELOPMENT)
# =====================================
if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
