from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

@login_required
def redirect_after_login(request):
    print("Redirecting after login...")
    user = request.user
    print(f"Redirecting user {user.username} with role {user.role}")
    if user.role == 'SUPERADMIN':
        return redirect('/superadmin/')

    elif user.role == 'SHOP':
        return redirect('/medical-shop/')

    elif user.role == 'DOCTOR':
        return redirect('/doctor/')

    elif user.role == 'PATIENT':
        return redirect('/')

    # If user's role isn't set or recognized, log them out and send
    # them back to the login page so an admin can fix their account.
    logout(request)
    
    print("User has no role assigned, logging out.")
    return redirect('/login/?error=no_role')


class CustomLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.role == 'SUPERADMIN':
            return '/superadmin/'

        elif user.role == 'SHOP':
            return '/medical-shop/'

        elif user.role == 'DOCTOR':
            return '/doctor/'

        elif user.role == 'PATIENT':
            return '/'

        return super().get_success_url()
