from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from users.decorators import role_required
from bookings.models import Booking

@role_required('SHOP')
def dashboard(request):
    shop = request.user.medical_shop
    bookings = Booking.objects.filter(medical_shop=shop)

    context = {
        'today_bookings': bookings.filter(
            appointment_date=request.today
        ),
        'total_bookings': bookings.count(),
    }
    return render(request, 'medical_shop/dashboard.html', context)


from doctors.models import Doctor
from .models import DoctorShopConnection

@role_required('SHOP')
def send_doctor_request(request, doctor_id):
    shop = request.user.medical_shop
    doctor = Doctor.objects.get(id=doctor_id)

    DoctorShopConnection.objects.get_or_create(
        medical_shop=shop,
        doctor=doctor
    )
    return redirect('medical_shop:doctor_list')

@role_required('SHOP')
def doctor_schedule(request, doctor_id):
    shop = request.user.medical_shop
    bookings = Booking.objects.filter(
        medical_shop=shop,
        doctor_id=doctor_id
    ).order_by('appointment_date', 'token_number')

    return render(request, 'medical_shop/doctor_schedule.html', {'bookings': bookings})

from doctors.models import Doctor
from .models import DoctorShopConnection
from users.decorators import role_required

@role_required('SHOP')
def doctor_list(request):
    shop = request.user.medical_shop
    doctors = Doctor.objects.all()

    for doctor in doctors:
        connection = DoctorShopConnection.objects.filter(
            medical_shop=shop,
            doctor=doctor
        ).first()

        doctor.connection_status = connection.status if connection else None

    return render(
        request,
        'medical_shop/doctor_list.html',
        {'doctors': doctors}
    )
