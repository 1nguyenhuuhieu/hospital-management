from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Profile)
class ProfileDetailAdmin(admin.ModelAdmin):
    pass