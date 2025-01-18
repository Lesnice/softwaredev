"""
URL configuration for mylabs_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from labbooking import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('save-booking/', views.save_booking, name='save_booking'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('bookings/', views.get_bookings, name='get_bookings'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include the auth URLs
    path('', views.equipment_list, name='home'),
    path('', views.home, name='home'),# Add this line for the root URL
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/book/<int:equipment_id>/', views.book_equipment, name='book_equipment'),
    path('equipment/add/', views.add_equipment, name='add_equipment'),
    path('experiments/', views.experiment_list, name='experiment_list'),
    path('experiments/add/', views.add_experiment, name='add_experiment'),
    path('antibodies/', views.antibody_list, name='antibody_list'),
    path('protocols/', views.protocol_list, name='protocol_list'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('chemicals/', views.chemical_list, name='chemical_list'),
    path('chemicals/add/', views.add_chemical, name='add_chemical'),
    path('equipment/add/', views.add_equipment, name='add_equipment'),
    path('antibodies/add/', views.add_antibody, name='add_antibody'),
    path('protocols/add/', views.add_protocol, name='add_protocol'),
    path('lab-book/open/', views.open_lab_book, name='open_lab_book'),
]
