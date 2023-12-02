from django.db import models
from django.utils.text import slugify


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


class ActTechRider(models.Model):
    act = models.ForeignKey('Act', on_delete=models.CASCADE, related_name='tech_riders')
    slug = models.SlugField()
    num_performers = models.IntegerField(default=1)
    instruments = models.ManyToManyField(Instrument, related_name='tech_riders')
    notes = models.TextField(blank=True, null=True)


    @property
    def total_channels(self):
        return sum([i.num_channels for i in self.instruments.all()])

    def __str__(self):
        return f'{self.act.name} {self.num_performers} Pieces- TechRider # {self.id}'

    def save(self, *args, **kwargs):
        name = f'{self.act.name} TechRider # {self.id}'
        self.slug = slugify(name)
        super().save(*args, **kwargs)
