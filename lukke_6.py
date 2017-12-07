#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:18:02 2017

@author: s_halnes

Nissen har hovedkvarter i Oslo. Han har fått en liste fra Yr med alle verdens viktige steder 
utenfor Norge. Hvor mange av hovedstedene (Stadtype=Hovedstad i filen) kan han levere til på 24t, 
dersom sleden flyr med en hastighet på X-15 (7,274 km/h).

Nissen har ikke plass til alt for mange gaver i sleden, så han må innom Oslo mellom hvert besøk. 
Han trenger ingen pause og velger selvfølgelig de hovedstedene som er nærmest.

Listen inneholder ikke Oslo, men Nissen vet at Oslo har lat/long: 59.911491/10.757933.

Svar: antall hovedsteder Nissen rekker å besøke
"""
from math import radians, cos, sin, asin, sqrt
# Distance between two lat/lng coordinates in km using the Haversine formula
def getDistanceFromLatLng(lat1, lng1, lat2, lng2, miles=False): # use decimal degrees
  r=6371 # radius of the earth in km
  lat1=radians(lat1)
  lat2=radians(lat2)
  lat_dif=lat2-lat1
  lng_dif=radians(lng2-lng1)
  a=sin(lat_dif/2.0)**2+cos(lat1)*cos(lat2)*sin(lng_dif/2.0)**2
  d=2*r*asin(sqrt(a))
  if miles:
    return d * 0.621371 # return miles
  else:
    return d # return km
# Copyright 2016, Chris Youderian, SimpleMaps, http://simplemaps.com/resources/location-distance
# Released under MIT license - https://opensource.org/licenses/MIT
    
    
oslo_lat = 59.911491
oslo_long = 10.757933
ttw_list = []
velocity = 7274

with open('verda.txt', 'r') as file:
    data = file.readlines()
    hovedstad = set()
    for row in data:
        line = row.split('\t')
        if line[6] == 'Hovedstad' and line[1] not in hovedstad:
            ttw_list.append(2*getDistanceFromLatLng(oslo_lat, oslo_long, float(line[12]), float(line[13]))/velocity)
            hovedstad.add(line[1])
ttw_list.sort()
counter = 0
total_time = 0
while total_time < 24:
    total_time += ttw_list.pop(0)
    if total_time < 24:
        counter += 1
print(counter)

    
