from itertools import product
from django.contrib import admin
from .models import Order, Customer,Role,Employee,Student,Product

# Register your models here.
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
