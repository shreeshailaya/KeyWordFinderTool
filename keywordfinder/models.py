from django.db import models


class DataBase(models.Model):
    url = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    csrf_code = models.CharField(max_length=200)

