from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


class Authority(models.Model):
    codename = models.CharField('权限代码', max_length=32)
    url = models.CharField('URL Config Name', max_length=128)
    name = models.CharField('Authority Description', max_length=120)

    def save(self, *args, **kwargs):
        content_type_obj = ContentType.objects.get(app_label='test_auth', model='Authority')
        permission = Permission.objects.create(codename=self.codename,
                                               name=self.name,
                                               content_type=content_type_obj)
        super(Authority, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        content_type_obj = ContentType.objects.get(app_label='test_auth',
                                                   model='Authority')
        permission = Permission.objects.get(codename=self.codename,
                                            content_type=content_type_obj)
        permission.delete()
        super(Authority, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Authority Table'
        verbose_name_plural = verbose_name
