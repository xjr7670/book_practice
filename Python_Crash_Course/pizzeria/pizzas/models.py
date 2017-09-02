from django.db import models

class Pizza(models.Model):

    name = models.TextField(20)

    def __str__(self):
        return self.name


class Topping(models.Model):

    pizza = models.ForeignKey(Pizza)
    name = models.TextField(20)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name
