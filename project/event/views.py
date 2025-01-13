from django.shortcuts import render
from .models import *
from django.views.generic import ListView
class EventList(ListView):
    model = Event
    template_name = 'event/event.html'
    context_object_name = 'events'
# Create your views here.
