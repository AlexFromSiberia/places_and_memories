from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea, ClearableFileInput
from .models import Memory


class MemoryForm(ModelForm):
    """Create/Update form for a memory entry"""
    class Meta:
        # we use the only model we have
        model = Memory
        fields = ['place', 'text', 'photo', 'latitude', 'longitude']

        # widgets will define how it's going to look like
        widgets = {
            "latitude": TextInput(attrs={'id': "id_lat", 'class': 'form-control',
                                         'placeholder': "Enter latitude of the place"}),
            "longitude": TextInput(attrs={'id': "id_lng", 'class': 'form-control',
                                          'placeholder': "Enter longitude of the place"}),
            "place": TextInput(attrs={'class': 'form-control',
                                      'placeholder': "Enter name of the place"}),
            "text": Textarea(attrs={'class': 'form-control',
                                    'placeholder': 'Here you can describe all the memories'}),
            "photo": ClearableFileInput(attrs={'class': 'form-control'}),
        }
