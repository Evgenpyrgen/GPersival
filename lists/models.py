from django.db import models


class List(models.Model):
    """списк"""
    pass

class Item(models.Model):
    """элемент списка"""
    text = models.TextField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)

