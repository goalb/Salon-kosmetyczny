from django import forms
from django.forms import ModelForm
from .models import Team


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
