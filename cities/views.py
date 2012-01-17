from django.shortcuts import render_to_response
from cities.models import *

def index(request):
    top_cities = City.objects.all().order_by('-population')[:10]
    return render_to_response('index.html', {
        'top_cities':  top_cities,
        'top_cities_summary': calculate_summary(top_cities, True)
        
    })

def calculate_summary(rows, is_aggregated):
    summary = {'population': 0, 'land_area': 0}
    for row in rows:
        summary['population'] += row.population
        summary['land_area'] += row.land_area
    return summary
