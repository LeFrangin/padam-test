from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import googlemaps
from datetime import datetime

from cars.models import Cars


def set_car_disponibility(id_car, state):
    try:
        car = Cars.objects.get(id=id_car)
        car.disponibility = state
        car.save()
    except ObjectDoesNotExist:
        return None

# gmaps direction


def get_duration(start_address, dest_address):
    gmaps = googlemaps.Client(key='AIzaSyBp_bgC_kgp-0HR-qlaPkeIE06JnEPsMfc')
    now = datetime.now()
    try:
        directions_result = gmaps.directions(
            start_address,
            dest_address,
            mode="driving",
            departure_time=now)
        return directions_result[0]['legs'][0]['duration_in_traffic']['text']
    except googlemaps.exceptions.ApiError as inst:
        raise Http404(inst.args[0])
    except KeyError as e:
        return None
    except IndexError as e:
        return None
