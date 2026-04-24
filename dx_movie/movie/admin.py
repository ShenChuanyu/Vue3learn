from django.contrib import admin
from .models import Category,Movie
from django import forms
from django.db import models
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {
            'widget': forms.NumberInput(attrs={
                'min': 2000,
                'max': 2030,
                'step': 1,
            })
        },
    }

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)