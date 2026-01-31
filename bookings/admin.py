from django.contrib import admin
from .models import Booking, NotificationLog

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'doctor',
        'medical_shop',
        'appointment_date',
        'token_number',
        'status',
        'booked_by_call',
    )
    list_filter = (
        'status',
        'appointment_date',
        'booked_by_call',
    )
    search_fields = (
        'patient__username',
        'doctor__user__username',
        'medical_shop__name',
    )
    ordering = ('appointment_date', 'token_number')

@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('user__username',)
