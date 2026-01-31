from django.shortcuts import redirect, render

# Create your views here.
from users.decorators import role_required
from bookings.models import Booking

@role_required('DOCTOR')
def dashboard(request):
    doctor = request.user.doctor_profile
    bookings = Booking.objects.filter(doctor=doctor)

    return render(request, 'doctors/dashboard.html', {
        'today_bookings': bookings.filter(
            appointment_date=request.today
        )
    })



from medical_shop.models import DoctorShopConnection

@role_required('DOCTOR')
def connection_requests(request):
    doctor = request.user.doctor_profile
    requests = DoctorShopConnection.objects.filter(
        doctor=doctor,
        status='PENDING'
    )
    return render(request, 'doctors/connection_requests.html', {'requests': requests})

@role_required('DOCTOR')
def update_connection(request, connection_id, status):
    connection = DoctorShopConnection.objects.get(id=connection_id)
    connection.status = status
    connection.save()
    return redirect('doctors:connection_requests')

from users.decorators import role_required
from bookings.models import Booking

@role_required('DOCTOR')
def patient_history(request, patient_id):
    doctor = request.user.doctor_profile

    history = Booking.objects.filter(
        doctor=doctor,
        patient_id=patient_id,
        status='CONSULTED'
    ).order_by('-appointment_date')

    return render(
        request,
        'doctors/patient_history.html',
        {'history': history}
    )

