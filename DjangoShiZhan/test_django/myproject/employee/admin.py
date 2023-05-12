from django.contrib import admin
from .models import Employee2, Employee, EmployeeInfo, Department, Group


class Employee2Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'dep', 'group', 'salary', 'info')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dep_name', 'dep_script')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_script')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Employee2, EmployeeAdmin)
admin.site.register(EmployeeInfo, EmployeeInfoAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Department, DepartmentAdmin)
