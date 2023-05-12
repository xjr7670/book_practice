from django.db import models
from django.urls import reverse


class Department(models.Model):
    dep_name = models.CharField(max_length=32, verbose_name='部门名称', unique=True, blank=False)
    dep_script = models.CharField(max_length=60, verbose_name='备注', null=True)

    def get_absolute_url(self):
        return reverse('depdetail', kwargs={'dep_id': self.pk})


class Person(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')
    email = models.EmailField(max_length=32, verbose_name='电子邮箱')
    gender = models.CharField(max_length=1, choices=(('1', '男'), ('2', '女')), verbose_name='性别')
    head_img = models.ImageField(upload_to='headimage', blank=True, null=True, verbose_name='头像')
    attachment = models.FileField(upload_to='filedir', blank=True, null=True, verbose_name='附件')

    def get_gender_display(self):
        return '男' if self.gender == '2' else '女'


class LogUser(models.Model):
    account = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')

