from django import forms
from .models import Shelf

class ShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        fields = ["name", "latitude", "longitude"]
