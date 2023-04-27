from django.contrib import admin

from . import models


class RoleAdmin(admin.ModelAdmin):
    list_display = ('title', )


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'nickname', 'email', )


admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.UserInfo, UserInfoAdmin)
