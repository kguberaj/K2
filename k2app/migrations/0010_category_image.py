# Generated by Django 4.1.5 on 2023-02-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k2app', '0009_rename_top_deals_top_deal'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
