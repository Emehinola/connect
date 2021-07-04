from django.shortcuts import render
from . models import Event

# views for getting events available

# get events


def get_event(request):
    # gets the 2 latest events availbale in the database
    events = Event.objects.all()[:2]

    return events
