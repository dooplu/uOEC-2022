from geopy.geocoders import Nominatim
from geopy import distance as dist

def co2Emitted(home, shipper, mass):
    maxLandDistanceinKM = 3500
    co2pertonnekmships = 4
    co2pertonnekmtrucks = 63.4

    geolocator = Nominatim('default_user_agent')
    origin = geolocator.geocode(shipper)
    origin = (origin.longitude,origin.latitude)
    destination = geolocator.geocode(home)
    destination = (destination.longitude, destination.latitude)

    distance = dist.distance(origin, destination).kilometers
    
    if (distance > maxLandDistanceinKM):
        shipDistance = distance - maxLandDistanceinKM
        emissions = (mass / 1000) * shipDistance * co2pertonnekmships + (mass / 1000) * maxLandDistanceinKM * co2pertonnekmtrucks
        return emissions
    else:
        emissions = (mass / 1000) * distance * co2pertonnekmtrucks
        return emissions