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

class County(forms.ModelForm):
    class Meta:
        model = County
        fields = ['name','county']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your County Name'
            }),
            'county': forms.Select(attrs={
                'class': 'form-control border-0 bg-light',
            }),
            
        }
    def __str__(self):
        return self.name