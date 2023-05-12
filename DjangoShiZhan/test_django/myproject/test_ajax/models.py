from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=32, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
