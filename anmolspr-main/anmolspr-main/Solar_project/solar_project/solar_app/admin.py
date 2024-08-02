from django.contrib import admin
from .models import MySolarrr,hourlyspl

class solarAdmin(admin.ModelAdmin):
    list_display = ['date','sales','revenue','invertor_power_conversion','faulty_panels','working_panels','weather_prediction','maintainance_cost','Profit_and_loss','Rain_prediction','Energy_Distribution']  # Fields to display in the list view
     # Fields to display in the list view
    
admin.site.register(MySolarrr, solarAdmin)



class hourlryadmin(admin.ModelAdmin):
    list_display = ['solar_generation','production','temperature','performance','humidity','efficiency','UV_index','Irradiance']
    
admin.site.register(hourlyspl, hourlryadmin)








