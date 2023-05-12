from django.contrib import admin
from .models import LogUser


class LogUserAdmin(admin.ModelAdmin):
    list_display = ('account', 'password', 'email', 'hobby', 'gender', 'hair', 'img')


admin.site.register(LogUser, LogUserAdmin)
