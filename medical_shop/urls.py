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

app_name = 'medical_shop'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Doctors
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/request/<int:doctor_id>/', views.send_doctor_request, name='send_doctor_request'),

    # Doctor schedule
    path('doctor/<int:doctor_id>/schedule/', views.doctor_schedule, name='doctor_schedule'),
]
