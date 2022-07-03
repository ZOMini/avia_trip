import pytz
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from trip.form import Pass_in_tripForm
from trip.models import Airport, Pass_in_trip, Trip


def index(request):
    template = 'trip/index.html'
    text = 'Это главная страница проекта Avia'
    last_trips = Trip.objects.all().order_by('time_out')
    paginator = Paginator(last_trips, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'text': text,
        'page_obj': page_obj,
    }
    return render(request, template, context)

def airport(request, airport_id):
    template = 'trip/airport.html'
    airport = Trip.objects.filter(airport_from=airport_id).order_by('time_out')
    paginator = Paginator(airport, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if len(page_obj) > 0:
        TIME_ZONE = page_obj[0].airport_from.ap_time_zone
        TIME_ZONE = pytz.timezone(TIME_ZONE)
    else:
        # page_obj = get_object_or_404(Airport ,id=airport_id)
        TIME_ZONE = pytz.timezone('UTC')
    context = {
        'TIME_ZONE' : TIME_ZONE,
        'page_obj': page_obj,
    }
    return render(request, template, context)

def in_airport(request, airport_id):
    template = 'trip/in_airport.html'
    airport = Trip.objects.filter(airport_to=airport_id).order_by('time_out')
    paginator = Paginator(airport, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if len(page_obj) > 0:
        TIME_ZONE = page_obj[0].airport_to.ap_time_zone
        TIME_ZONE = pytz.timezone(TIME_ZONE)
    else:
        TIME_ZONE = pytz.timezone('UTC')   
    context = {
        'TIME_ZONE' : TIME_ZONE,
        'page_obj': page_obj,
    }
    return render(request, template, context)

@login_required()
def order(request):
    if request.method == 'POST':
        form = Pass_in_tripForm(request.POST)
        if form.is_valid():
            order = Pass_in_trip()
            order.place = form.cleaned_data['place']
            order.trip = form.cleaned_data['trip']
            order.passenger = request.user
            order.save()
            return render(request, 'trip/text.html', {'message': 'Место приобретено!'}) 
        return render(request, 'trip/order.html', {'form': form})
    form = Pass_in_tripForm()
    return render(request, 'trip/order.html', {'form': form}) 
