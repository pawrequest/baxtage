from django.db import models


class TechRider(models.Model):
    tour_eng = models.ForeignKey('Crew', on_delete=models.CASCADE)
    mixer = models.CharField(max_length=50, blank=True, null=True)
    spec_sheet = models.FileField(default=None, blank=True, null=True)


class HospitalityRider(models.Model):
    pass


class Rider(models.Model):
    tech = TechRider
    hospitality = HospitalityRider
