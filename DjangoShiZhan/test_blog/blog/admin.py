from django.contrib import admin
from . import models


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'modified_time', 'category', 'author', 'views')


admin.site.register(models.Loguser)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)

