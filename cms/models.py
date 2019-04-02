from django.db import models
from sorl.thumbnail import ImageField


# Create your models here.

class TopBanner(models.Model):
    image = ImageField()
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    button_text = models.CharField(max_length=30)

    def __str__(self):
        return self.title



class BottomBanner(models.Model):
    image = ImageField()
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    button_text = models.CharField(max_length=30)
    is_big = models.BooleanField()


class Menu(models.Model):
    title = models.CharField(max_length=50)
    weight = models.IntegerField()
    href = models.CharField(max_length=255)

    def __str__(self):
        return self.title
