# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView, DetailView, CreateView

from .models import Bookings
from cars.models import Cars

from helpers import set_car_disponibility, get_duration


class BookingCreate(CreateView):
    model = Bookings
    template_name = "form.html"
    fields = [
        "reservation_date",
        "reservation_hour",
        "start_address",
        "dest_address"
    ]

    def get_context_data(self, **kwargs):
        context = super(BookingCreate, self).get_context_data(**kwargs)
        context['title'] = "Nouvelle réservation"
        context['form_url'] = "booking_new"
        return context

    def form_valid(self, form):
        cars = Cars.objects.filter(disponibility=True)  # Get a car with a better way
        duration = get_duration(form.instance.start_address, form.instance.dest_address)
        print duration
        if duration is None:
            form.add_error('start_address', 'l\'adresse de départ ou de destination ne semble pas correct')
            return self.form_invalid(form)

        car = cars.first()
        if car is None:
            form.add_error('reservation_date', 'Désolé, plus aucune voiture n\'est disponible. Veuillez réessayer plus tard')
            return self.form_invalid(form)

        set_car_disponibility(car.id, False)  # Update the disponibility of the car

        form.instance.car = car  # Add the car to the form values
        form.instance.user = self.request.user
        form.instance.state = True
        form.instance.duration = duration

        return super(BookingCreate, self).form_valid(form)


class BookingDelete(DeleteView):
    model = Bookings
    success_url = reverse_lazy('booking_list')

    def delete(self, request, *args, **kwargs):
        booking_id = self.kwargs['pk']
        booking = Bookings.objects.get(id=booking_id)
        print booking_id
        print booking.car.id
        set_car_disponibility(booking.car.id, True)
        booking.delete()

        return HttpResponseRedirect(reverse_lazy('booking_list'))


class BookingDetail(DetailView):
    model = Bookings
    template_name = "bookings/detail.html"
    context_object_name = "booking"


class BookingList(ListView):
    model = Bookings
    template_name = "bookings/list.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Bookings.objects.filter(user=self.request.user)
