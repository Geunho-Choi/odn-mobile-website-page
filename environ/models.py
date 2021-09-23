from django.db import models
from core.models import TimeStampedModel
from buoys.models import Buoy

# Create your models here.


class Environ(TimeStampedModel):

    ocean = models.CharField(max_length=80, default="none")
    location = models.CharField(max_length=80)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    oxygen = models.FloatField(default=0)
    hydrogen = models.FloatField(default=0)
    salt = models.FloatField(default=0)
    turbidity = models.FloatField(default=0)
    measurement_time = models.DateTimeField()
    odn_data = models.ForeignKey(
        Buoy, related_name="environ", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.location
