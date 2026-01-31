from django import forms
from .models import Carousel, Complaint

class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['title', 'image', 'is_active']


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['resolved']
