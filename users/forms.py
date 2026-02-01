from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'role', 'password', 'is_active']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)  # Hash password
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with a display
    field that shows the hashed password.
    """
    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text="Raw passwords are not stored, so there is no way to see this user's password, "
                  "but you can change the password using <a href='../password/'>this form</a>."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'role', 'password', 'is_active', 'is_staff']

    def clean_password(self):
        # Always return the initial value regardless of what the user provides
        return self.initial["password"]
