from django.contrib import admin
from .models import Person, LogUser


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'head_img')


class LogUserAdmin(admin.ModelAdmin):
    list_display = ('account', 'password')


admin.site.register(Person, PersonAdmin)
admin.site.register(LogUser, LogUserAdmin)

