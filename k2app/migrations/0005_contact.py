# Generated by Django 4.1.5 on 2023-02-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k2app', '0004_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=12)),
                ('email', models.EmailField(default='', max_length=50)),
                ('message', models.TextField(default='', max_length=300)),
            ],
        ),
    ]
