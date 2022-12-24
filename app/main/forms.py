from django.forms import ModelForm
from .models import Memory
from django.forms.widgets import TextInput, Textarea, ClearableFileInput


class MemoryForm(ModelForm):
    """Create/Update form for a memory entry"""
    class Meta:
        # we use the only model we have
        model = Memory
        fields = ['place', 'text', 'photo', 'latitude', 'longitude']

        # widgets will define how it's going to look like
        widgets = {
            "latitude": TextInput(attrs={'id': "id_lat", 'class': 'form-control', 'placeholder': "Latitude of the place"}),
            "longitude": TextInput(attrs={'id': "id_lng", 'class': 'form-control', 'placeholder': "Longitude of the place"}),
            "place": TextInput(attrs={'class': 'form-control', 'placeholder': "Name of the place"}),
            "text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Full text'}),
            "photo": ClearableFileInput(attrs={'class': 'form-control'}),
        }

