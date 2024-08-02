from django.db.models import Sum
from django.utils import timezone
from django.db.models.functions import TruncWeek
from django.db import models
from datetime import timedelta


class MySolarrr(models.Model):
    date = models.DateField(default=timezone.now)
    sales = models.IntegerField(default=0)
    revenue = models.IntegerField(default=0)
    invertor_power_conversion = models.IntegerField(default=0)
    faulty_panels = models.IntegerField(default=0)
    working_panels = models.IntegerField(default=0)
    weather_prediction = models.IntegerField(default=0)
    maintainance_cost = models.IntegerField(default=0)
    Profit_and_loss = models.IntegerField(default=0)
    Rain_prediction = models.IntegerField(default=0)
    Energy_Distribution = models.IntegerField(default=0)
    


class hourlyspl(models.Model):
    solar_generation = models.IntegerField(default=0)
    production = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)
    performance = models.CharField(max_length=200, default='')
    humidity = models.IntegerField(default=0)
    efficiency = models.IntegerField(default=0)
    UV_index = models.IntegerField(default=0)
    Irradiance = models.IntegerField(default=0)
    


    
    