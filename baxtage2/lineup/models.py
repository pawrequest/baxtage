from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify

from lineup.gear import ActTechRider, Instrument
from lineup.people import Act
from lineup.show import Show


class Performance(models.Model):
    acts = models.ManyToManyField(Act, related_name='performances')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='performances')
    # tech_spec = models.OneToOneField(TechSpec, on_delete=models.PROTECT, related_name='performance')
    slug = models.SlugField()
    start_time = models.DateTimeField()

    @property
    def name(self):
        return f'{" and ".join([act.name for act in self.acts.all()])} on {self.start_time:%a-%d} at {self.start_time:%H-%M} '

    def get_absolute_url(self):
        return reverse('lineup:performance_detail', args=[self.slug])


@receiver(m2m_changed, sender=Performance.acts.through)
def update_slug(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear", "post_save"]:
        name = f'{instance.start_time:%a-%d-%H-%M} {" and ".join([act.name for act in instance.acts.all()])}'
        instance.slug = slugify(name)
        instance.save()
