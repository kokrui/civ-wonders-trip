from geopy.geocoders import Nominatim

fin = open("civ6-wonders.csv","r")
wonders=fin.readlines()

fout = open("civ6-wonders-coords.txt","w")

geolocator = Nominatim(user_agent="travel_to_wonders")

for wonder in wonders[1:]:
    wlist = wonder.split(',')
    location = geolocator.geocode(wonder[1])

    outline = ""
    outline+=f"{wlist[1]},{location.latitude},{location.longitude},{wlist[3]}"
    print(outline)
    break
