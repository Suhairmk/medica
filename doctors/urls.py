"""
URL configuration for medica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Clinic connection requests
    path('connections/', views.connection_requests, name='connection_requests'),
    path('connections/<int:connection_id>/<str:status>/', views.update_connection, name='update_connection'),

    # Patient history
    path('patient/<int:patient_id>/history/', views.patient_history, name='patient_history'),
]


