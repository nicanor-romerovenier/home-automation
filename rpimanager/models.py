from django.db import models


# Create your models here.
class RelaySwitch(models.Model):
    description = models.CharField(max_length=100)
    state = models.BooleanField(help_text="False means switched off")

    def __str__(self):
        return self.description
