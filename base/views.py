from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Team, Appointment, User
from .forms import TeamForm, AppointmentForm
from django.contrib import messages


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


#  Everything with team
def add_team(request):
    submitted = False
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect('/add_team?submitted=True')
    else:
        form = TeamForm
        if 'submitted' in request.GET:
            submitted = True
        # Success message
    return render(request, 'base/add_team.html', {'form': form, 'submitted': submitted})


def team(request):
    teammates = Team.objects.all()
    return render(request, 'base/team.html', {'teammates': teammates})


def contact(request):
    return render(request, 'contact.html', {})


def add_appointment(request):
    submitted = False
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # appointment.client = request.user.id
            appointment = form.save(commit=False)
            appointment.client = request.user.id
            appointment.save()
            # Going back to the same page
            return HttpResponseRedirect('/add_appointment?submitted=True')
    else:
        form = AppointmentForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'base/add_appointment.html', {'form': form, 'submitted': submitted})


def show_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    return render(request, 'base/show_appointment.html', {'appointment': appointment})


def list_appointment(request):
    list_appointment = Appointment.objects.all().order_by('date')
    return render(request, 'base/list_appointment.html', {'show_appointment': list_appointment})


def update_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if form.is_valid():
        form.save()
        return redirect('list_appointment')
    return render(request, 'base/update_appointment.html', {'appointment': appointment, 'form': form})


def delete_appointment(request):
    return render(request, 'contact.html', {})

