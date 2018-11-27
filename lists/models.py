from django.db import models
from django.urls import reverse


class List(models.Model):
    """списк"""

    def get_absolute_url(self):
        """получить абсолютный урл"""
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """элемент списка"""
    text = models.TextField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)

