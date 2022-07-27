from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    return render(request, 'home.html', {})


# Navbar things
def treatments(request):
    return render(request, 'treatments.html', {})


def prices(request):
    return render(request, 'prices.html', {})


def reviews(request):
    return render(request, 'reviews.html', {})


def sale(request):
    return render(request, 'sale.html', {})


def training(request):
    return render(request, 'training.html', {})


def team(request):
    return render(request, 'team.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def appointment(request):
    return render(request, 'appointment.html', {})
# End navbar
