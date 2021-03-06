from django.shortcuts import render
from .models import *
import folium
import folium.features
import geocoder


def general(request):
    
    ukrain = geocoder.osm('UA')
    
    m = folium.Map(location = [ukrain.latlng[0], ukrain.latlng[1]], zoom_start = 7)
    
    kiev = geocoder.osm('Kiev')
    kharkiv = geocoder.osm('Kharkiv')
    odessa = geocoder.osm('Odessa')
    lviv = geocoder.osm('Lviv')
    zhytomyr = geocoder.osm('Zhytomyr')
    khmelnytskyi = geocoder.osm('Khmelnytskyi')
    ivano_frankivsk = geocoder.osm('Ivano-Frankivsk')
    vinnitsa = geocoder.osm('Vinnitsa')
    zaporizhzhia = geocoder.osm('Zaporizhzhia')
    сhernihiv = geocoder.osm('Chernihiv') 
    
    folium.Marker(
        [kiev.latlng[0], kiev.latlng[1]],
        popup = 'Improve "туса"',
        tooltip = 'Дізнатися більше про івент.'
    ).add_to(m)
    
    folium.Marker(
        [kharkiv.latlng[0], kharkiv.latlng[1]],
        popup = 'Матч "Металіст - Динамо"',
        tooltip = 'Дізнатися більше про івент.'
    ).add_to(m)
    
    folium.Marker(
        [odessa.latlng[0], odessa.latlng[1]],
        popup = '"Цікавинки в історії Одеси"',
        tooltip = 'Дізнатися більше про івент.'
    ).add_to(m)
    
    folium.Marker(
        [lviv.latlng[0], lviv.latlng[1]],
        popup = '"Кавова" прогулянка',
        tooltip = 'Дізнатися більше про івент.'
    ).add_to(m)
    
    folium.Marker(
        [zhytomyr.latlng[0], zhytomyr.latlng[1]],
        popup = 'Екстремальний відпочинок',
        tooltip = 'Дізнатися більше про івент.'
    ).add_to(m)
    
    folium.Marker(
        [khmelnytskyi.latlng[0], khmelnytskyi.latlng[1]],
        popup = 'Чортове колесо',
        tooltip = 'Дізнатися більше про івент.'
    ).add_to(m)
    
    folium.Marker(
        [ivano_frankivsk.latlng[0], ivano_frankivsk.latlng[1]],
        popup = 'Фото зустріч',
        tooltip = 'Дізнатися більше про івент.'
    ).add_to(m)
    
    folium.Marker(
        [vinnitsa.latlng[0], vinnitsa.latlng[1]],
        popup = 'Фонтани',
        tooltip = 'Дізнатися більше про івент.'
    ).add_to(m)
    
    folium.Marker(
        [zaporizhzhia.latlng[0], zaporizhzhia.latlng[1]],
        popup = '"Запорозька Січ"',
        tooltip = 'Дізнатися більше про івент.'
    ).add_to(m)
    
    
    folium.Marker(
        [сhernihiv.latlng[0], сhernihiv.latlng[1]],
        popup = 'Подорож Черніговом',
        tooltip = 'Дізнатися більше про івент.'
    ).add_to(m)
    

    m = m._repr_html_()

    context = {
        'title': 'Знайди івент для себе',
        'map': m,
    }
    
    return render(
        request,
        'jorneyisa/map.html',
        context
    )


def showtable(request):
    event = Events.objects.all()
    context = {
        'title': 'Список івентів',
        'events': event
    }
    return render(
        request,
        'jorneyisa/table.html',
        context
    )
