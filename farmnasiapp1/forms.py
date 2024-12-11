# forms.py
from django import forms
from .models import Contact
from .models import County

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'style': 'height: 150px'
            }),
            
        }

    def __str__(self):
        return self.name



class CountyForm(forms.ModelForm):
    class Meta:
        model = County
        fields = ['name', 'county']  # Specify the fields to include in the form
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter County Name'
            }),
            'county': forms.Select(attrs={
                'class': 'form-control border-0 bg-light',
            }),
        }

    def __str__(self):
        return self.cleaned_data.get('name', '')
