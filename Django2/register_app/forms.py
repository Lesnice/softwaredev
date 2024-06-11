from django import forms
from .models import user

class DateInput(forms.DateInput):
    input_type = 'date'
    
class UserForm(forms.ModelForm):
    class Meta:
        model=UserForm
        fields=('name', 'photo', 'email', 'password')