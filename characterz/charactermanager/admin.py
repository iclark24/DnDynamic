from django.contrib import admin
from django.contrib.auth.models import User
from .models import Race, Feature

# Register your models here.

admin.site.register(Race)
admin.site.register(Feature)
