from itertools import product
from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    product_description=models.TextField()
    product_qty=models.IntegerField()
    product_colour=models.CharField(max_length=50,null=True)
    product_Status=models.BooleanField(default=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=
    True)
    


class ProductCatagory(models.Model):
    category_name=models.CharField(max_length=50)
    category_description=models.TextField()
    class Meta:
        db_table='category'    
