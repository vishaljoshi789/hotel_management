from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
import datetime

# Create your views here.

def home(request):
    return render(request, 'mainapp/home.html')

def booking(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        ctx = form.save()
        return redirect('payment', room_no=ctx.room_no)
    context = {
        'form': form
    }
    return render(request, 'mainapp/booking.html', context)

def rooms_info(request):
    rooms = []
    for i in range(1, 101):
        try:
            room = Booking.objects.get(room_no=i)
            rooms.append({'status': "Booked By "+ room.name, 'room_no': i, "booked": True})
        except:
            rooms.append({'status': 'Room is available', 'room_no': i, "booked": False})
    context = {
        'rooms': rooms
    }
    return render(request, 'mainapp/rooms_info.html', context)

def payment(request, room_no):
    room =  Booking.objects.get(room_no=room_no)
    check_in = room.checkin
    check_out = room.checkout
    # check_in = datetime.date(checkin[0], checkin[1], checkin[2])
    # check_out = datetime.date(checkout[0], checkout[1], checkout[2])
    day = check_out - check_in
    days = day.days
    room_price = 1500
    if room.ac:
        room_price+=200
    if room.wifi:
        room_price+=100
    total_price = room_price * days
    context = {
        'room': room,
        'room_price': room_price,
        'total_price': total_price,
        'days' : days
    }
    return render(request, 'mainapp/payment.html', context)

def edit_room(request, room_no):
    room = Booking.objects.get(room_no=room_no)
    form = BookingForm(request.POST or None, instance=room)
    if form.is_valid():
        ctx = form.save()
        return redirect('payment', room_no=ctx.room_no)
    context = {
        'form': form
    }
    return render(request, 'mainapp/booking.html', context)

def remove_room(request, room_no):
    room = Booking.objects.get(room_no=room_no)
    room.delete()
    return redirect('rooms_info')

def book_room(request, room_no):
    form = BookingForm(request.POST or None, initial={'room_no': room_no})
    if form.is_valid():
        ctx = form.save()
        return redirect('payment', room_no=ctx.room_no)
    context = {
        'form': form
    }
    return render(request, 'mainapp/booking.html', context)

def restro(request):
    return render(request, 'mainapp/restro.html')