from django.db import models
from .category_model import Category
from .color_model import Color

class Product(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 140)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    unit_measurement = models.CharField(max_length = 2)
    quantity = models.IntegerField()
    color = models.ForeignKey(Color, on_delete= models.CASCADE)

    class Meta:
        app_label = 'supermarket_ms'
