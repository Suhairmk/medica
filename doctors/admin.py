from django.contrib import admin
from .models import Doctor, Specialisation, DoctorLeave

@admin.register(Specialisation)
class SpecialisationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'specialisation',
        'experience_years',
        'consultation_fee',
        'is_verified',
    )
    list_filter = ('specialisation', 'is_verified')
    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
    )

@admin.register(DoctorLeave)
class DoctorLeaveAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'reason')
    list_filter = ('date',)
    search_fields = ('doctor__user__username',)
