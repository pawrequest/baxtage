from django.db import models

from lineup.equipment import Instrument
from lineup.people import Act


class Show(models.Model):
    def __str__(self):
        return f'{self.name} - {self.start_date}'

    name = models.CharField(max_length=100)
    start_date = models.DateField()
    venue = models.CharField(max_length=100)

#
# class HospitalityRider(models.Model):
#     notes = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.notes}'
#

class TechRider(models.Model):
    instruments = models.ManyToManyField(Instrument, related_name='tech_riders')
    notes = models.TextField(blank=True, null=True)

    @property
    def total_channels(self):
        return sum([i.num_channels for i in self.instruments.all()])

    def __str__(self):
        return f'{[i.name for i in self.instruments.all()]}'


class Performance(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    acts = models.ManyToManyField(Act, related_name='performances')
    tech_rider = models.ForeignKey(TechRider, on_delete=models.SET_NULL, null=True, blank=True, related_name='performance')

    start_time = models.DateTimeField()

    def __str__(self):
        return f'{self.start_time.time()} - {[act.name for act in self.acts.all()]}'
