# Generated by Django 4.1.5 on 2023-01-31 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k2app', '0003_rename_cars_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('contact', models.CharField(default='', max_length=50)),
                ('instagram', models.CharField(default='', max_length=50)),
                ('copyright', models.CharField(default='', max_length=50)),
            ],
        ),
    ]