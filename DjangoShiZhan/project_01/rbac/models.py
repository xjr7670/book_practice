from django.db import models


class Role(models.Model):
    title = models.CharField(max_length=32, unique=True, verbose_name='Role Name')
    permissions = models.ManyToManyField("Permission", blank=True, verbose_name='Permissions')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Role Table'


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=32)
    email = models.EmailField()
    roles = models.ManyToManyField('Role')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name_plural = 'User Table'


class Permission(models.Model):
    title = models.CharField(max_length=32, unique=True, verbose_name='Authority Name')
    url = models.CharField(max_length=128, unique=True, verbose_name='URL')
    perm_code = models.CharField(max_length=32, verbose_name='Authority Code')
    perm_group = models.ForeignKey(to='PermGroup', blank=True, on_delete=models.CASCADE,
                                   verbose_name='Belonging Authority Group')
    pid = models.ForeignKey(to='Permission', null=True, blank=True, on_delete=models.CASCADE,
                            verbose_name='Belonging Second Menu')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Authority Table'


class PermGroup(models.Model):
    title = models.CharField(max_length=32, verbose_name='Group name')
    menu = models.ForeignKey(to='Menu', verbose_name='Belonging Menu', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Authority Group'


class Menu(models.Model):
    title = models.CharField(max_length=32, unique=True, verbose_name='Top Level Menu')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Top Level Menu'




