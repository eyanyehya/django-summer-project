from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    text = models.TextField(default='')
    title = models.CharField(max_length=200, default='')
    # author = models.ForeignKey(
    #     'auth.User',
    #     on_delete=models.CASCADE
    # )
    first_name = models.CharField(max_length=200, default='')
    body = models.TextField(default='')

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
