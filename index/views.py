from django.shortcuts import render
from events.views import get_event

# Create your views here.


def home(request):
    events = get_event(request)

    context = {
        'events': events
    }

    return render(request, 'index/index.html', context)


def aggregate(request):
    return render(request, 'index/aggregate.html')
