from django.db import models

from lineup.people import Act


class Show(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.venue} - {self.start_date}'

#
# class TechSpec(models.Model):
#     notes = models.TextField(blank=True, null=True)
#     acts = models.ManyToManyField(Act, related_name='tech_specs')
#
#     def __str__(self):
#         return f'{"".join(act.name for act in self.acts.all())}'
