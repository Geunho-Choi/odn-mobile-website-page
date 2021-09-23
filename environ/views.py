from django.shortcuts import render
from environ.models import Environ
from django.views.generic import DetailView, TemplateView
from environ.api import clean_data

# Create your views here.


class EnvironView(TemplateView):

    """Environ View Definition"""

    template_name = "environ/environ.html"
    model = Environ


def api_view(request):

    datum = clean_data(request)
    for i in datum:
        ocean = i.get("ocean")
        location = i.get("location")
        lat = i.get("lat")
        lon = i.get("lon")
        measurement_time = i.get("measurement_time")
        temperature = i.get("temperature")
        oxygen = i.get("oxygen")
        hydrogen = i.get("hydrogen")
        salt = i.get("salt")
        turbidity = i.get("turbidity")
        if temperature is None:
            continue
        if oxygen is None:
            oxygen = 0
        if hydrogen is None:
            hydrogen = 0
        if salt is None:
            salt = 0
        if turbidity is None:
            turbidity = 0

        if Environ.objects.filter(lat=lat, lon=lon, measurement_time=measurement_time):
            continue

        else:
            data = Environ.objects.create(
                ocean=ocean,
                location=location,
                lat=lat,
                lon=lon,
                temperature=temperature,
                oxygen=oxygen,
                hydrogen=hydrogen,
                salt=salt,
                turbidity=turbidity,
                measurement_time=measurement_time,
            )
            data.save()
