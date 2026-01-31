from django.contrib import admin
from .models import Carousel, Complaint

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title',)

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'resolved', 'created_at')
    list_filter = ('resolved',)
    search_fields = ('user__username',)
