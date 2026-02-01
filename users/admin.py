from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, PatientProfile
from .forms import UserCreateForm

class CustomUserAdmin(BaseUserAdmin):
    add_form = UserCreateForm  # Use your custom form for creating users
    model = User

    list_display = ('username', 'email', 'phone', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active')

    search_fields = ('username', 'email', 'phone')

    # Fields for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'role', 'password', 'is_active', 'is_staff'),
        }),
    )

    # Fields for editing an existing user
    fieldsets = (
        (None, {'fields': ('username', 'email', 'phone', 'role', 'password', 'is_active', 'is_staff')}),
    )

admin.site.register(User, CustomUserAdmin)


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'gender')
    list_filter = ('gender',)
    search_fields = ('user__username',)
