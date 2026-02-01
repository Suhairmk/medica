from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout



class CustomLoginView(auth_views.LoginView):

    template_name = 'auth/login.html'

    def dispatch(self, request, *args, **kwargs):
        print("✅ CustomLoginView dispatch called")
        return super().dispatch(request, *args, **kwargs)
    def get_success_url(self):
            user = self.request.user
            role = getattr(user, 'role', None)

            print("🔥 get_success_url called")
            print("User:", user.username, "Role:", role)

            if role == 'SUPERADMIN':
                return '/superadmin/'

            elif role == 'SHOP':
                return '/medical-shop/'

            elif role == 'DOCTOR':
                return '/doctor/'

            elif role == 'PATIENT':
                return '/'
            return '/'
