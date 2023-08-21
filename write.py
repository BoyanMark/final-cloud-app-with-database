# Django specific settings
import inspect
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
from django.db import connection

# Ensure settings are read
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from onlinecourse.models import Course
from datetime import date


def write_courses():
    # Add Courses
    course_django = Course(
        name="Django Course",
        description="Developing Applications with SQL, Databases, and Django",
    )
    course_django.save()

    course_cloud_app = Course(
        name="Cloud Application Development with Database",
        description="Develop and deploy application on cloud",
    )
    course_cloud_app.save()

    course_python = Course(
        name="Introduction to Python",
        description="Learn core concepts of Python and obtain hands-on "
        "experience via a capstone project",
    )
    course_python.save()

    print("Course objects all saved... ")


def clean_data():
    # Delete all data to start from fresh
    Course.objects.all().delete()


# Clean any existing data first
clean_data()
write_courses()
