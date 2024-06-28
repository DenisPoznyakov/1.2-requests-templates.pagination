from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open (settings.BUS_STATION_CSV, newline='', encoding='utf8') as csvfile:
        bus_stations_list = []
        reader = csv.DictReader(csvfile)
        data = list(row for row in reader)
        for row in data:
            bus_stations_list.append(row['Name'])
            print(row)
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(data, 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page.object_list,
            'page': page,
        }
    return render(request, 'stations/index.html', context)