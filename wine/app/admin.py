from django.contrib import admin

# Register your models here.
from models import Car, User

class CarAdmin(admin.ModelAdmin):
    fields = ('name', 'image')

admin.site.register(Car, CarAdmin)

class UserAdmin(admin.ModelAdmin):
    fields = ('name', 'email')

admin.site.register(User, UserAdmin)