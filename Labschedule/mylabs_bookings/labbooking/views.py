from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Equipment, Booking, Experiment, Antibody, Protocol, Chemical
from django.utils import timezone
from django.http import HttpResponse
from .forms import ChemicalForm, EquipmentForm, AntibodyForm, ProtocolForm, ExperimentForm, BookingForm
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('equipment_list')
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'booking/signup.html', {'form': form})

def chemical_list(request):
    chemicals = Chemical.objects.all()
    return render(request, 'booking/chemical_list.html', {'chemicals': chemicals})

@login_required
def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'booking/equipment_list.html', {'equipments': equipments})

@login_required
def book_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.equipment = equipment
            booking.user = request.user  # Assuming the user is logged in
            booking.save()
            return redirect('equipment_list')
    else:
        form = BookingForm()

    return render(request, 'booking/book_equipment.html', {'form': form, 'equipment': equipment})

@login_required
def experiment_list(request):
    experiments = Experiment.objects.filter(user=request.user)
    return render(request, 'booking/experiment_list.html', {'experiments': experiments})

@login_required
def add_experiment(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            experiment = form.save(commit=False)
            experiment.user = request.user
            experiment.save()
            return redirect('experiment_list')
    else:
        form = ExperimentForm()
    return render(request, 'booking/add_experiment.html', {'form': form})

@login_required
def antibody_list(request):
    antibodies = Antibody.objects.all()
    return render(request, 'booking/antibody_list.html', {'antibodies': antibodies})

@login_required
def protocol_list(request):
    protocols = Protocol.objects.all()
    return render(request, 'booking/protocol_list.html', {'protocols': protocols})

def add_chemical(request):
    if request.method == 'POST':
        form = ChemicalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chemical_list')
    else:
        form = ChemicalForm()
    return render(request, 'booking/add_chemical.html', {'form': form})

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'booking/add_equipment.html', {'form': form})

def add_antibody(request):
    if request.method == 'POST':
        form = AntibodyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('antibody_list')
    else:
        form = AntibodyForm()
    return render(request, 'booking/add_antibody.html', {'form': form})

def add_protocol(request):
    if request.method == 'POST':
        form = ProtocolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('protocol_list')
    else:
        form = ProtocolForm()
    return render(request, 'booking/add_protocol.html', {'form': form})

def open_lab_book(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experiment_list')
    else:
        form = ExperimentForm()
    return render(request, 'booking/open_lab_book.html', {'form': form})
def home(request):
    # Get the current date
    today = timezone.now().date()

    # Filter bookings for the current day
    bookings = Booking.objects.filter(start_time__date=today)

    return render(request, 'booking/base.html', {'bookings': bookings})
def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')  # Redirect to the equipment list after saving
    else:
        form = EquipmentForm()

    return render(request, 'booking/add_equipment.html', {'form': form})
# View to render the calendar template
def calendar_view(request):
    return render(request, 'booking/calendar.html')

# View to get bookings in JSON format for the calendar
def get_bookings(request):
    bookings = Booking.objects.all()
    bookings_data = [{
        'id': booking.id,
        'title': f'{booking.title} - {booking.user.get_full_name()}',  # Add user name to title
        'start': booking.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
        'end': booking.end_time.strftime('%Y-%m-%dT%H:%M:%S'),
    } for booking in bookings]

    return JsonResponse(bookings_data, safe=False)
@csrf_exempt
def save_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        start = datetime.fromisoformat(data.get('start'))
        end = datetime.fromisoformat(data.get('end'))

        booking = Booking.objects.create(
            user=request.user,  # Assuming the user is logged in
            title=title,
            start_time=start,
            end_time=end
        )

        return JsonResponse({'success': True, 'id': booking.id})
    
    return JsonResponse({'success': False})