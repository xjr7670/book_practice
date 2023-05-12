from django.contrib import admin

from . import models


class AuthorityAdmin(admin.ModelAdmin):
    list_display = ('codename', 'url', 'name')


admin.site.register(models.Authority, AuthorityAdmin)

