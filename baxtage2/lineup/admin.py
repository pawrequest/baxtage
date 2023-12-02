from django.contrib import admin

from lineup.gear import ActTechRider, Instrument, Microphone
from lineup.models import Performance
from lineup.people import Act, Person, Role
from lineup.show import Show


@admin.register(Person, Role)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(ActTechRider)
class ActTechAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    ...

@admin.register(Act, Instrument, Microphone)
class ActAdmin(admin.ModelAdmin):
    ...


@admin.register(Performance, Show)
class PerformanceAdmin(admin.ModelAdmin):
    exclude = ('slug',)
