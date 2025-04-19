from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500 , default="https://cdn.pixabay.com/photo/2021/04/06/15/00/pie-6156640_1280.jpg")

