from django.db import models

class Color(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    description = models.TextField(max_length = 140)
    codehexa = models.TextField(max_length = 10)

    class Meta:
        app_label = 'supermarket_ms'
