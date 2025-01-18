from django import forms
from .models import Booking, Experiment, Chemical, Equipment, Antibody, Protocol, Experiment

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['equipment', 'user', 'start_time', 'end_time']

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['title', 'description']

from django import forms
from .models import Chemical

class ChemicalForm(forms.ModelForm):
    class Meta:
        model = Chemical
        fields = ['name', 'concentration', 'description']  # Add all fields you need here
        labels = {
            'name': 'Chemical Name',
            'concentration': 'Concentration (mg/mL)',
            'description': 'Description',
        }
        help_texts = {
            'name': 'Enter the chemical\'s name.',
            'concentration': 'Specify the concentration of the chemical.',
            'description': 'Add any additional details about the chemical.',
        }


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'description', 'availability']

class AntibodyForm(forms.ModelForm):
    class Meta:
        model = Antibody
        fields = ['name', 'species', 'concentration']

class ProtocolForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = ['title', 'description', 'notes']

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['title', 'description', 'date', 'notes']
