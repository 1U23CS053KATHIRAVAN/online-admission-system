from django import forms
from .models import Student


class StudentApplicationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['course', 'full_name', 'phone', 'address', 'document']

        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'document': forms.FileInput(attrs={'class': 'form-control'}),
        }