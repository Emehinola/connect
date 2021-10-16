from django.shortcuts import render
from events.views import get_event
from events.models import Event
from blog.models import Blog
from . models import View

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
    view = View.objects.last() # gets the last model
    view.number += 1 # increments views by one
    view.save() # saves the change made to the View model
    
    no_of_view = View.objects.last().number
    return render(request, 'index/aggregate.html', {'events': events, 'no_of_views': view})
