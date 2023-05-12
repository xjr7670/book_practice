from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')
    email = models.EmailField(verbose_name='Email')
    dep = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Department(models.Model):
    dep_name = models.CharField(max_length=32, verbose_name='Department Name', unique=True, blank=False)
    dep_script = models.CharField(max_length=60, verbose_name='Comment', null=True)

    def __str__(self):
        return self.dep_name
