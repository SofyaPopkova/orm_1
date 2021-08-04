from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
    pass
