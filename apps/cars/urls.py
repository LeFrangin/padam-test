from django.conf.urls import url
from views import CarsList, CarDetail

urlpatterns = [
    url(r'^list/$', CarsList.as_view(), name='car_list'),
    url(r'^(?P<pk>\d+)$', CarDetail.as_view(), name='car_detail'),
]

