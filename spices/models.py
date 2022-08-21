from django.contrib.auth import get_user_model
from django.db import models


class Spice(models.Model):
    name = models.CharField(max_length=64)
    plant_type = models.CharField(max_length=128)
    description = models.TextField(default=" ")
    submitter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
