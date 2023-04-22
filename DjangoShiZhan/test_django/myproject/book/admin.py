from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publishdate'
    empty_value_display = '-无值-'
    filter_horizontal = ('author',)
    fieldsets = (
        (
            '图书信息',
            {
                'fields': (('title', 'publishdate'), 'publishing', 'author')
            }
        ),
        (
            '图书简介',
            {
                'classes': ('collapse',), 'fields': ('descript',)
            }
        ),
    )

    def change_publishing(self, request, queryset):
        publishing_obj = models.Publishing.objects.get(name='清华大学出版社')
        rows = queryset.update(publishing=publishing_obj)
        self.message_user(request, f'{rows} 条记录被修改成 ”新生活出版社“ ')

    def descript_str(self, obj):
        return obj.descript[:20]

    change_publishing.short_description = '选中记录的出版社改为 ”新生活出版社“'
    descript_str.short_description = '简介'
    list_filter = ('title', 'publishing', 'author')
    search_fields = ('title', 'publishing__name', 'author__name')
    list_display = ('title', 'descript_str', 'publishdate', 'publishing',)
    show_full_result_count = True
    list_per_page = 6
    actions = ['change_publishing']


class PublishingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_editable = ('address',)
    list_per_page = 10


class AuthorAdmin(admin.ModelAdmin):
    def header_data(self, obj):
        return mark_safe(u'<img src="/media/%s" width="50px" height="30px" />' % obj.header)

    header_data.short_description = '简介'
    list_display = ('name', 'email', 'birthday', 'header_data')
    list_per_page = 10


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Publishing, PublishingAdmin)
admin.site.register(models.Author, AuthorAdmin)
