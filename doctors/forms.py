from django import forms
from .models import Doctor, Specialisation, DoctorLeave

class SpecialisationForm(forms.ModelForm):
    class Meta:
        model = Specialisation
        fields = ['name']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'qualification',
            'specialisation',
            'experience_years',
            'consultation_fee',
            'is_verified',
        ]

class DoctorLeaveForm(forms.ModelForm):
    class Meta:
        model = DoctorLeave
        fields = ['date', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
