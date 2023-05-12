from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='分类名')
    des = models.CharField(max_length=100, verbose_name='备注', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='标签名')
    des = models.CharField(max_length=100, verbose_name='备注', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Loguser(AbstractUser):
    nickname = models.CharField(max_length=32, verbose_name='昵称', blank=True)
    telephone = models.CharField(max_length=11, null=True, unique=True)
    head_img = models.ImageField(upload_to='headimage', blank=True, null=True, verbose_name='头像')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = '用户信息表'


class Blog(models.Model):
    title = models.CharField(max_length=70, verbose_name='文章标题')
    body = RichTextUploadingField(verbose_name='文本内容')
    created_time = models.DateTimeField(verbose_name='创建时间')
    modified_time = models.DateTimeField(verbose_name='修改时间')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='文章摘要')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    author = models.ForeignKey(Loguser, on_delete=models.CASCADE, verbose_name='作者')
    views = models.IntegerField(default=0, verbose_name='查看次数')

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt = strip_tags(self.body)[:118]
            super(Blog, self).save(*args, **kwargs)
        else:
            super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = '文档管理表'
        verbose_name_plural = '文档管理表'




