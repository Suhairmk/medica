from django.shortcuts import redirect, render

# Create your views here.
from django.db.models import Max

from bookings.models import Booking
from users.decorators import role_required
from .forms import BookingForm
from doctors.models import DoctorLeave

@role_required('SHOP')
def create_booking(request):
    form = BookingForm(request.POST or None)

    if form.is_valid():
        booking = form.save(commit=False)

        # 🚫 Doctor Leave Check
        if DoctorLeave.objects.filter(
            doctor=booking.doctor,
            date=booking.appointment_date
        ).exists():
            form.add_error(None, 'Doctor is not available on this date')
            return render(request, 'bookings/booking_form.html', {'form': form})

        # 🔢 Token generation
        last_token = Booking.objects.filter(
            doctor=booking.doctor,
            appointment_date=booking.appointment_date
        ).aggregate(Max('token_number'))['token_number__max'] or 0

        booking.token_number = last_token + 1
        booking.estimated_time = booking.doctor.user.doctor_profile.consultation_fee
        booking.save()

        return redirect('medical_shop:dashboard')

    return render(request, 'bookings/booking_form.html', {'form': form})

from .forms import BookingStatusForm

def update_booking_status(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    form = BookingStatusForm(request.POST or None, instance=booking)

    if form.is_valid():
        form.save()
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'bookings/status_form.html', {'form': form})

@role_required('DOCTOR')
def patient_history(request, patient_id):
    doctor = request.user.doctor_profile
    history = Booking.objects.filter(
        doctor=doctor,
        patient_id=patient_id,
        status='CONSULTED'
    ).order_by('-appointment_date')

    return render(request, 'doctors/patient_history.html', {'history': history})


