from django.contrib import admin
from .models import MedicalShop, DoctorShopConnection

@admin.register(MedicalShop)
class MedicalShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone', 'is_verified', 'is_active')
    list_filter = ('city', 'is_verified', 'is_active')
    search_fields = ('name', 'city', 'phone')
    ordering = ('name',)

@admin.register(DoctorShopConnection)
class DoctorShopConnectionAdmin(admin.ModelAdmin):
    list_display = ('medical_shop', 'doctor', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = (
        'medical_shop__name',
        'doctor__user__username',
    )
