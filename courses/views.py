from django.shortcuts import render
from . models import Course
import json
from django.http import JsonResponse
from events.models import Event

# Create your views here.


def course_selector(request):
    events = Event.objects.all()[:2]
    courses = Course.objects.all()
    no_of_views = sum([i.no_of_views for i in courses])
    conext = {'courses': courses, 'events': events, 'no_of_views': no_of_views}
    return render(request, 'courses/course_selector.html', conext)


def get_course(request):
    course = request.GET.get('course')  # course searched for

    # increases the number of views by one, i.e whenever the page is viewed
    course_object = Course.objects.get(course_title=course)
    course_object.no_of_views += 1
    course_object.save()

    olevel = course_object.olevel_subjects
    jamb = course_object.jamb_subjects
    desc = course_object.description
    no_of_views = course_object.no_of_views

    return JsonResponse({'course': course, 'olevel': olevel, 'jamb': jamb, 'desc': desc, 'no_of_views': no_of_views}, safe=False)
