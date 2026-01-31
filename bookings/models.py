from django.db import models

# Create your models here.
from django.db import models
from users.models import User
from medical_shop.models import MedicalShop
from doctors.models import Doctor

class Booking(models.Model):
    STATUS_CHOICES = (
        ('BOOKED', 'Booked'),
        ('CONSULTED', 'Consulted'),
        ('ABSENT', 'Absent'),
        ('CANCELLED', 'Cancelled'),
    )

    booked_by_call = models.BooleanField(default=False)

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    medical_shop = models.ForeignKey(MedicalShop, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    appointment_date = models.DateField()
    token_number = models.PositiveIntegerField()
    estimated_time = models.TimeField()

    description = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='BOOKED')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['appointment_date', 'token_number']
        unique_together = ('doctor', 'appointment_date', 'token_number')

    def __str__(self):
        return f"{self.patient.username} - {self.doctor}"




class NotificationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
