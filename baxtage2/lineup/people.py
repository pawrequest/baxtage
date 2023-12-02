from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    roles = models.ManyToManyField(Role, related_name='people')

    def __str__(self):
        return self.name


class Act(models.Model):
    name = models.CharField(max_length=50)
    performers = models.ManyToManyField(Person, related_name='acts', limit_choices_to={'roles__name': 'Performer'})
    primary_contact = models.ForeignKey(Person, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
