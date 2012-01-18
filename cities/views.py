from django.shortcuts import render_to_response
from django.db.models import Count, Sum
from cities.models import *

def index(request):
    top_cities = City.objects.select_related().order_by('-population')[:10]
    top_states = State.objects.annotate(count_cities=Count('id'), sum_population=Sum('city__population'), sum_land_area=Sum('city__land_area')).order_by('-count_cities', '-sum_population')[:10]
    return render_to_response('index.html', {
        'top_cities': top_cities,
        'top_states': top_states,
        'top_cities_summary': calculate_summary(top_cities, False),
        'top_states_summary': calculate_summary(top_states, True),
        
    })

def calculate_summary(rows, is_aggregated):
    summary = {'population': 0, 'land_area': 0}
    for row in rows:
        summary['population'] += row.population if not is_aggregated else row.sum_population
        summary['land_area']  += row.land_area  if not is_aggregated else row.sum_land_area
    return summary
