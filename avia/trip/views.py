from django.core.paginator import Paginator
from django.shortcuts import render
from trip.models import Airport, Trip


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
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)

def in_airport(request, airport_id):
    template = 'trip/in_airport.html'
    airport = Trip.objects.filter(airport_to=airport_id).order_by('time_out')
    paginator = Paginator(airport, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)
