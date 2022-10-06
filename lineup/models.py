from django.db import models


# Create your models here.
class Organisation(models.Model):
    pass


class Person(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Artist(Person):
    instrument = models.CharField(max_length=50)


class Crew(Person):
    role = models.CharField(max_length=50)


class Act(models.Model):  # act is a table of artists?
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    artists = models.ManyToManyField(Artist)
    tour_eng = models.ForeignKey('Crew', on_delete=models.CASCADE, blank=True, null=True)
    pass


class TechRider(models.Model):
    tour_eng = models.ForeignKey('Crew', on_delete=models.CASCADE)
    mixer = models.CharField(max_length=50, blank=True, null=True)
    spec_sheet = models.FileField(default=None, blank=True, null=True)

class HospitalityRider(models.Model):
    pass


class Rider(models.Model):
    tech = TechRider
    hospitality = HospitalityRider


class Performance(models.Model):
    linecheck_time = models.DateTimeField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    act = models.ForeignKey('Act', on_delete=models.CASCADE)
    tech_brief = models.TextField(blank=True,null=True)
    hospitality_brief = models.TextField(blank=True,null=True)


class Show(models.Model):
    performances: list
    pass
