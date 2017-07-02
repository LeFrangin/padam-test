# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from .models import Cars

# Create your views here.


class CarDetail(DetailView):
    model = Cars
    template_name = "cars/detail.html"
    context_object_name = "car"


class CarsList(ListView):
    model = Cars
    template_name = "cars/list.html"
    context_object_name = "cars"

