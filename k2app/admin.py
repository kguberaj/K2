from django.contrib import admin
from k2app import models
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Car)
admin.site.register(Footer)
admin.site.register(Contact)
admin.site.register(Top_Deal)
admin.site.register(RegisterUser)