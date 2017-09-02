from django.db import models

class mealPlan(models.Model):
    """meal_plan的主页"""

    text = models.TextField(50)

    def __str__(self):
        return self.text
