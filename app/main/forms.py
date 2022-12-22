from django.forms import ModelForm
from .models import Memory
from django.forms.widgets import TextInput, Textarea, Select, ClearableFileInput


class MemoryForm(ModelForm):
    """Form for creation a new article (Page: Add a news article)"""
    class Meta:
        # we use the only model we have
        model = Memory
        fields = ['place', 'text', 'photo', ]

        # widgets will define how it's going to look like
        widgets = {
            "place": TextInput(attrs={'class': 'form-control', 'placeholder': "Name of place"}),
            "text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Fill it with your best memories'}),
            "photo": ClearableFileInput(attrs={'class': 'form-control'}),
        }


class AddMemoryForm(ModelForm):
    """Create/Update form for a memory entry"""
    class Meta:
        # we use the only model we have
        model = Memory
        fields = ['place', 'text', 'photo', ]

        # widgets will define how it's going to look like
        widgets = {
            "place": TextInput(attrs={'class': 'form-control', 'placeholder': "Name of the place"}),
            "text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Full text'}),
            "photo": ClearableFileInput(attrs={'class': 'form-control'}),
        }

