from django.db import models

# Create your models here.


class Events(models.Model):
    event_id = models.IntegerField(null=False, unique=True)
    name = models.CharField(null=False, blank=False,max_length=100)
    link = models.URLField(null=False, blank=False,)
    description = models.TextField(null=False, blank=False,)
    date = models.DateField(null=False, blank=False,)
    image_url = models.URLField(null=False, blank=False,)
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    class Meta:
        ordering = ['-date']
