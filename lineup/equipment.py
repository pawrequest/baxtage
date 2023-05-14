from django.db import models

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
