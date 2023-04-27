from django.contrib import admin

from .models import Fare, Department, CarInfo, LogUser


admin.site.register(Fare)
admin.site.register(Department)
admin.site.register(CarInfo)
admin.site.register(LogUser)
