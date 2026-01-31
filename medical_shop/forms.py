from django import forms
from .models import MedicalShop, DoctorShopConnection

class MedicalShopForm(forms.ModelForm):
    class Meta:
        model = MedicalShop
        fields = [
            'name',
            'address',
            'city',
            'location_lat',
            'location_lng',
            'phone',
            'working_from',
            'working_to',
            'is_verified',
            'is_active',
        ]
        widgets = {
            'working_from': forms.TimeInput(format='%H:%M'),
            'working_to': forms.TimeInput(format='%H:%M'),
        }


class DoctorShopConnectionForm(forms.ModelForm):
    class Meta:
        model = DoctorShopConnection
        fields = ['medical_shop', 'doctor', 'status']
