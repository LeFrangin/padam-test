# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from cars.models import Cars

# Create your models here.


class Bookings(models.Model):
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de creation")
    reservation_date = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Date de réservation")
    reservation_hour = models.TimeField(auto_now_add=False, auto_now=False, verbose_name="Heure de réservation")
    car = models.OneToOneField(Cars, related_name='car')
    user = models.ForeignKey(User, related_name='user')
    start_address = models.CharField(max_length=250, verbose_name="Départ")
    dest_address = models.CharField(max_length=250, verbose_name="Destination")
    state = models.BooleanField()
    duration = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('booking_detail', kwargs={'pk': self.pk})


