# coding: utf-8

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import SignUp

urlpatterns = [
    url(r'^in$', auth_views.login, {'template_name': 'form.html', 'extra_context': {
        "title": "Se connecter à Padam test",
        "form_url": "sign_in"
    }}, name='sign_in'),
    url(r'^out$', auth_views.logout, {'next_page': 'sign_in'}, name='sign_out'),
    url(r'^up$', SignUp.as_view(), name='sign_up'),
]

