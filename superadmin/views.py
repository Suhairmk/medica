

# Create your views here.
from django.shortcuts import redirect, render
from django.utils import timezone
from users.decorators import role_required
from medical_shop.models import MedicalShop
from doctors.models import Doctor
from bookings.models import Booking

@role_required('SUPERADMIN')
def dashboard(request):
    context = {
        'total_shops': MedicalShop.objects.count(),
        'total_doctors': Doctor.objects.count(),
        'total_bookings': Booking.objects.count(),
        'today_bookings': Booking.objects.filter(
            appointment_date__exact=timezone.localdate()
        ).count(),
    }
    return render(request, 'superadmin/dashboard.html', context)


from medical_shop.models import MedicalShop
from medical_shop.forms import MedicalShopForm

@role_required('SUPERADMIN')
def medical_shop_list(request):
    shops = MedicalShop.objects.all()
    return render(request, 'superadmin/medical_shop_list.html', {'shops': shops})

@role_required('SUPERADMIN')
def medical_shop_verify(request, shop_id):
    shop = MedicalShop.objects.get(id=shop_id)
    shop.is_verified = True
    shop.save()
    return redirect('superadmin:medical_shop_list')


from .models import Carousel
from .forms import CarouselForm

@role_required('SUPERADMIN')
def carousel_list(request):
    carousels = Carousel.objects.all()
    return render(request, 'superadmin/carousel_list.html', {'carousels': carousels})

@role_required('SUPERADMIN')
def carousel_create(request):
    form = CarouselForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('superadmin:carousel_list')
    return render(request, 'superadmin/carousel_form.html', {'form': form})
