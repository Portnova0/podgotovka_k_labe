from django.urls import path
from .views import EventList
urlpatterns = [

    path('event/', EventList.as_view(), name='index'),
]
