from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """博客模形"""

    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'blogposts'

    def __str__(self):
        return self.text
