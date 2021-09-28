from django.shortcuts import render
from events.views import get_event
from events.models import Event
from blog.models import Blog

# Create your views here.


def home(request):
    events = get_event(request)
    blogs = Blog.objects.all()[:6]

    context = {
        'events': events,
        'blogs': blogs
    }

    return render(request, 'index/index.html', context)


def aggregate(request):
    events = Event.objects.all()[:2]  # gets the last two events
    return render(request, 'index/aggregate.html', {'events': events})
