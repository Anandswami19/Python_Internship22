 
# from importlib.util import resolve_name
# from itertools import product
# from sre_constants import CATEGORY
# from traceback import print_exception

'''
from django.db import models

# Create your models here.
class role(models.Model):
    role_name=models.CharField(max_length=50)
    role_description=models.TextField()

    class Meta:
        db_table='role'

class employee(role):
            employee_name=models.CharField(max_length=50)
            employee_Email=models.CharField(max_length=50)
            employee_password=models.CharField(max_length=50)
            employee_phone=models.CharField(max_length=50)
            employee_address=models.TextField()
            employee_dob=models.DateTimeField()
            class Meta:
                db_table='employee' 
class student(models.Model):
    #   role_id=models.ForeignKey(role,on_delete=models.CASCADE)
      role_id=models.OneToOneField(role,on_delete=models.CASCADE)
      student_name=models.CharField(max_length=50)
      student_Email=models.CharField(max_length=50)
      student_password=models.CharField(max_length=50)
      student_phone=models.CharField(max_length=50)
      student_address=models.TextField()
      student_dob=models.DateField()

class Customer(models.Model):
    customer_name=models.CharField(max_length=50)

    class Meta:
        db_table='customer'

class Product(models.Model):
    CATEGORY=(('indor','indor'),('outdoor','outdoor'))
    name=models.CharField(max_length=200)
    price=models.FloatField()
    date_created=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='Product'

class Order(models.Model):
    STATUS=(('pending','pending'),('od','od'),('delivered','delivered'))
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)    
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    Status=models.CharField(max_length=200,choices=STATUS)

    class Meta:
        db_table='Order'

'''

from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=50)
    role_description = models.TextField()
    class Meta:
        db_table = 'role'

class Employee(Role):
    employee_name = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=50)
    employee_password = models.CharField(max_length=50)
    employee_phone = models.CharField(max_length=50)
    employee_address = models.TextField()
    employee_dob = models.DateField()

    class Meta:
        db_table = 'employee'
    
class Student(models.Model):
    #role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    role_id = models.OneToOneField(Role, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_password = models.CharField(max_length=50)
    student_phone = models.CharField(max_length=50)
    student_address = models.TextField()
    student_dob = models.DateField()

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'customer'

class Product(models.Model):
    CATEGORY =(('indor','indor'),('outdoor','outdoor'))
    name = models.CharField(max_length=200)
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'product'

class Order(models.Model):
    STATUS = (
    ('pending','pending'),('od','od'),('delivered','delivered'))
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,choices=STATUS)
    class Meta:
        db_table = 'order'


            


        