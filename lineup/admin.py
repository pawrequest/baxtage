from django.contrib import admin

from .show import Performance, Show, TechRider
from lineup.equipment import Instrument, Microphone
from .people import Act, Person, Role


@admin.register(Person, Role)
class PersonAdmin(admin.ModelAdmin):
    ...


@admin.register(Show, Act, Instrument, TechRider, Microphone)
class ShowAdmin(admin.ModelAdmin):
    ...

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    ...

