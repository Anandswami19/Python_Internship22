# Generated by Django 4.0.2 on 2022-02-19 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0004_customer_product_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='order',
            table='Order',
        ),
    ]
