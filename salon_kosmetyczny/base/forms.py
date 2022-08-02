from django import forms
from django.forms import ModelForm
from .models import Team, Appointment


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'image', 'description')
        labels = {
            'name': '',
            'image': '',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('client', 'worker', 'date', 'description')
        labels = {
            'client': '',
            'worker': 'Worker',
            'date': 'YYYY-MM-DD HH:MM:SS',
            'description': '',
        }
        widgets = {
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'client'}),
            'worker': forms.Select(attrs={'class': 'form-select', 'placeholder': 'worker'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
