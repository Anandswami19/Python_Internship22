# Generated by Django 4.0.2 on 2022-02-18 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Employee_Email',
            new_name='employee_Email',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employee_address',
            new_name='employee_address',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employee_dob',
            new_name='employee_dob',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employee_name',
            new_name='employee_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employee_password',
            new_name='employee_password',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employee_phone',
            new_name='employee_phone',
        ),
        migrations.AlterModelTable(
            name='employee',
            table='employee',
        ),
    ]
