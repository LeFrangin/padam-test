# -*- coding: utf-8 -*-

from django.conf.urls import url
from views import BookingList, BookingDetail, BookingCreate, BookingDelete

urlpatterns = [
    url(r'^list/$', BookingList.as_view(), name='booking_list'),
    url(r'^(?P<pk>\d+)$', BookingDetail.as_view(), name='booking_detail'),
    url(r'^new$', BookingCreate.as_view(), name='booking_new'),
    url(r'^delete/(?P<pk>\d+)$', BookingDelete.as_view(), name='booking_delete')
]

