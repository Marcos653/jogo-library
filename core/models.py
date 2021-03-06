from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.category

class Jogo(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=2)
    categories = models.ManyToManyField(Category, null=True, blank=True)
    platform = models.CharField(max_length=255, null=True, blank=True)
    link_image = models.CharField(max_length=255, null=True, blank=True)
    describe = models.TextField(null=True, blank=True)
    storage = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(default=0, null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
     
