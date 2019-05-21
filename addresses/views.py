from django.shortcuts import render
from .forms import DeliveryAddressAddForm
from django.shortcuts import redirect
from django.http import Http404


def add(request):
    if request.method == "POST":
        form = DeliveryAddressAddForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('orders:checkout')
    raise Http404('Bad Request')
