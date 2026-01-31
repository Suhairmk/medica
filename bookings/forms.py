from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'patient',
            'medical_shop',
            'doctor',
            'appointment_date',
            'description',
            'booked_by_call',
        ]
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']


from .models import NotificationLog

class NotificationForm(forms.ModelForm):
    class Meta:
        model = NotificationLog
        fields = ['user', 'booking', 'message']
