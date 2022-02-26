# Generated by Django 4.0.2 on 2022-02-24 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'exam',
            },
        ),
    ]
