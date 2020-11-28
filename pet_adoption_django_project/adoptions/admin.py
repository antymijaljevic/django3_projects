from django.contrib import admin

from .models import Pet, Vaccine #import your models

# admin.site.register(Vaccine)

@admin.register(Pet)

class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex'] #set what you want to see on main of panel