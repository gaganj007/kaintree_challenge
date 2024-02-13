from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def str(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def str(self):
        return self.name

class Item(models.Model):
    sku = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    in_stock = models.IntegerField()
    available_stock = models.IntegerField()

    def str(self):
        return self.name