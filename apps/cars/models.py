# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Cars(models.Model):
    disponibility = models.BooleanField()
    name = models.CharField(max_length=250, verbose_name="Nom")
    year = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'apps_cars'
