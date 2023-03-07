from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50, default='')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.category


class Car(models.Model):
    name = models.CharField(max_length=50, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField(default=0)
    year = models.IntegerField(default=0)
    seats = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    Manual = 'Manual'
    Automatic = 'Automatic'
    TYPE_CHOICES = [
        (Manual, 'Manual'),
        (Automatic, 'Automatic'),
    ]
    gearbox = models.CharField(max_length=50, choices=TYPE_CHOICES, default='')
    Diesel = 'Diesel'
    Petrol = 'Petrol'
    TYPE_CHOICES_Fuel = [
        (Diesel, 'Diesel'),
        (Petrol, 'Petrol'),
    ]
    fuel = models.CharField(max_length=50, choices=TYPE_CHOICES_Fuel, default='')
    Po = 'Po'
    Jo = 'Jo'
    AVAILABLE_CHOICES = [
        (Po, 'Po'),
        (Jo, 'Jo'),
    ]

    # available = models.CharField(max_length=50, choices=AVAILABLE_CHOICES, default='')

    def __str__(self):
        return self.name

class Top_Deal(models.Model):
    deals = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.deals.name

class Footer(models.Model):
    name=models.CharField(max_length=50, default='')
    email=models.CharField(max_length=50, default='')
    contact=models.CharField(max_length=50, default='')
    instagram=models.CharField(max_length=50, default='')
    copyright=models.CharField(max_length=50, default='')
    def __str__(self):
        return self.name


class Contact(models.Model):
    fullname = models.CharField(max_length=12, default='')
    email = models.EmailField(max_length=50, default='')
    message = models.TextField(max_length=300, default='')
    def __str__(self):
        return self.fullname


class RegisterUser(models.Model):
    name = models.CharField(max_length=12, default='')
    surname = models.CharField(max_length=12, default='')
    email = models.EmailField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    confirmpassword = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name + self.surname