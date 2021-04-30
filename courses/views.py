from django.shortcuts import render
from . models import Course

# Create your views here.


def course_selector(request):
    courses = Course.objects.all()
    conext = {'courses': courses}
    return render(request, 'courses/course_selector.html', conext)
