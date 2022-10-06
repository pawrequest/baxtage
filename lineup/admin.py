from django.contrib import admin

from .models import *


@admin.register(Person, Artist, Performance, Act, Crew)
class PersonAdmin(admin.ModelAdmin):
    pass
# Register your models here.
