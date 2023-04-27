from django.contrib import admin

from .models import Person, Department


admin.site.register(Person)
admin.site.register(Department)

