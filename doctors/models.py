

# Create your models here.
from django.db import models
from users.models import User

class Specialisation(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    qualification = models.CharField(max_length=255)
    specialisation = models.ForeignKey(Specialisation, on_delete=models.SET_NULL, null=True)
    experience_years = models.PositiveIntegerField()
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()


class DoctorLeave(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('doctor', 'date')

