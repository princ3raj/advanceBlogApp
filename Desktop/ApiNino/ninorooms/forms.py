from django import forms
from .models import NinoRooms


class NinoCreateView(forms.ModelForm):
    class Meta:
        model = NinoRooms
        fields = '__all__'