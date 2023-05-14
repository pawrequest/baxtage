from django.contrib import admin

from .show import Performance, Show, TechnicalSpec, Instrument, Microphone, Act
from .people import Person, Role


@admin.register(Person, Role)
class PersonAdmin(admin.ModelAdmin):
    ...


@admin.register(Show, Act, Instrument, TechnicalSpec, Microphone)
class ShowAdmin(admin.ModelAdmin):
    ...

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    ...

