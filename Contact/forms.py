from django import forms

from .models import Contact

class UserForm(forms.ModelForm):
    name = forms.CharField(label='Full Name',max_length=50)
    phoneno = forms.CharField(label='Phone Number',max_length=12)
    class Meta:
        model = Contact
        fields = ['name', 'phoneno']

