from django.db import models


# class Category(models.Model):
#     category = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return self.category
class Jogo(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    # categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    platform = models.CharField(max_length=255, null=True, blank=True)
    link_image = models.CharField(max_length=255, null=True, blank=True)
    describe = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title