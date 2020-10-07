from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from time import sleep

def do_geocode(geolocator,address, attempt=1, max_attempts=100):
    sleep(4)
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        print(attempt)
        if attempt <= max_attempts:
            return do_geocode(geolocator,address, attempt=attempt+1)

        raise


fin = open("civ6-wonders.csv","r")
wonders=fin.readlines()

fout = open("civ6-wonders-coords2.txt","a")

geolocator = Nominatim(user_agent="civ-wonders")

for wonder in wonders[13:]:
    wlist = wonder.split(',')
    sleep(2)
    print(wlist[1])
    location = do_geocode(geolocator,wlist[1])
    if location != None:
        outline = ""
        print(wlist[1])
        outline+=f"{wlist[1]},{location.latitude},{location.longitude},{wlist[3]}"
        print(outline)

        fout.write(outline)
