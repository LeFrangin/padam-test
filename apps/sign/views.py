from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import JoinForm


def join(request):
    form = JoinForm(request.POST or None)
    if form.is_valid():
        userDjango = User.objects.create(
            username = form.cleaned_data['email'],
            last_name = form.cleaned_data['surname'],
            first_name = form.cleaned_data['firstname'],
            email = form.cleaned_data['email'])

        userDjango.set_password(request.POST['password'])
        userDjango.save()
        return redirect('/sign/in')

    return render(request, 'form.html', locals())


class SignUp(CreateView):
    model = User
    template_name = "form.html"
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "password",
    ]

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        context['title'] = "S'inscrire"
        context['form_url'] = "sign_up"
        return context

    def form_valid(self, form):
        if form.is_valid():
            userDjango = User.objects.create(
                username=form.instance.username,
                last_name=form.instance.last_name,
                first_name=form.instance.first_name,
                email=form.instance.email
            )

            userDjango.set_password(form.instance.password)
            userDjango.save()
            return HttpResponseRedirect(reverse_lazy('sign_in'))
