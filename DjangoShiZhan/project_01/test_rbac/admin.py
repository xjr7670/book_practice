from django.contrib import admin
from rbac import models


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'perm_code', 'perm_group', 'pid']


class PermGroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'menu']


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'nickname', 'email']


admin.site.register(models.Menu)
admin.site.register(models.Role)
admin.site.register(models.PermGroup, PermGroupAdmin)
admin.site.register(models.Permission, PermissionAdmin)
admin.site.register(models.UserInfo, UserInfoAdmin)


