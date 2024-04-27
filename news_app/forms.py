from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ['user', 'email', 'msg']
        fields = '__all__'