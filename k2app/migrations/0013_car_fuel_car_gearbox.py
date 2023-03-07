# Generated by Django 4.1.5 on 2023-02-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k2app', '0012_remove_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='fuel',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Petrol', 'Petrol')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='gearbox',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='', max_length=50),
        ),
    ]
