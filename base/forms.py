from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email*'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone*', 'type': 'number'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject*'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text Message*', 'name': 'comment'}),
        }