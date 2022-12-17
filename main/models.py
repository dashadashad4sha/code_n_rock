from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=500, blank=True, null=True)
    product_number = models.CharField(max_length=500, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    factory = models.CharField(max_length=500, blank=True, null=True)
    comment = models.CharField(blank=True, max_length=500, null=True)

    def __str__(self):
        return self.product_name

