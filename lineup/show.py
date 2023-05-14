from django.db import models

from lineup.people import Person


class Show(models.Model):
    def __str__(self):
        return f'{self.name} - {self.start_date}'

    name = models.CharField(max_length=100)
    start_date = models.DateField()
    venue = models.CharField(max_length=100)


class Performance(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    acts = models.ManyToManyField('Act', related_name='performances')
    start_time = models.DateTimeField()

    def __str__(self):
        return f'{self.start_time.time()} - {[act.name for act in self.acts.all()]}'


class Microphone(models.Model):
    name = models.CharField(max_length=50)
    is_condenser = models.BooleanField(default=False)
    is_dynamic = models.BooleanField(default=True)
    takes_phantom_power = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Instrument(models.Model):
    default_microphone = models.ForeignKey(Microphone, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=50)
    is_miked = models.BooleanField(default=False)
    is_direct = models.BooleanField(default=False)
    num_channels = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class TechnicalSpec(models.Model):
    instruments = models.ManyToManyField(Instrument, related_name='technical_specs')

    notes = models.TextField(blank=True, null=True)

    @property
    def total_channels(self):
        return sum([i.num_channels for i in self.instruments.all()])

    def __str__(self):
        return f'{[i.name for i in self.instruments.all()]}'


class Act(models.Model):
    tech_spec = models.ForeignKey(TechnicalSpec, on_delete=models.SET_NULL, null=True, blank=True)
    performers = models.ManyToManyField(Person, related_name='acts')
    primary_contact = models.ForeignKey(Person, on_delete=models.PROTECT)

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
