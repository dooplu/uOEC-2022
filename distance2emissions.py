def co2Emitted(distance, mass):
    maxLandDistanceinKM = 3500
    co2pertonnekmships = 4
    co2pertonnekmtrucks = 63.4
    
    if (distance > maxLandDistanceinKM):
        shipDistance = distance - maxLandDistanceinKM
        emissions = (mass / 1000) * shipDistance * co2pertonnekmships + (mass / 1000) * maxLandDistanceinKM * co2pertonnekmtrucks
        return emissions
    else:
        emissions = (mass / 1000) * distance * co2pertonnekmtrucks
        return emissions