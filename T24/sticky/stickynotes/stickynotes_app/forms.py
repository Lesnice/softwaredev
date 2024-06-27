# stickynotes_app/forms.py

from django import forms
from .models import Note



class NoteForm(forms.ModelForm):
    """ 
    Form for creating and updating note objects
    
    Fields:
    - title: CharField for the note title.
    - content: Text field for the note content.
    
    Meta Class:
    -Defines the model to use (Note) and the fields to include in the form.
    
    :param forms.ModelForm: Django's ModleForm class."""
    
    class Meta():
        model = Note
        fields =['title', 'content', 'author']

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']