# This project accpets coordinates and ouputs locations to a map with pinpoint marker, real 12 hour weather forecast with icons.
# Current setup has the coordinates of Major Cities in England, Netherlands, and Belgium - outputs their locations and simplified 12 hour weather forecast
# Note: This project is part of an educational course on Udemy. Reference= https://www.udemy.com/course/the-python-pro-course/

# Imports
from folium import Map, Marker, Popup
from geo import Geopoint

# Set Latitude and Longitude Values
london= [51.5,-0.1]
liverpool= [53.4,-3]
manchester=[53.5,-2.3] 
amsterdam=[52.4,4.9]
rotterdam=[51.9,4.5]
den_haag=[52.1,4.3]
antwerpen=[51.2,4.4]
brussels=[50.9,4.4]
gent=[51.1,3.7]

locations = [london,liverpool,manchester,amsterdam,rotterdam,den_haag,antwerpen,brussels,gent]

# Folium Map Instance
mymap = Map(location = [52,2],zoom_start=7)  #[52,2] is center of the map

for lat, lon in locations:
    # Create a Geopoint Instance
    geopoint = Geopoint(latitude =  lat, longitude = lon)
    forecast = geopoint.get_weather()

    popup_content = f"""
    {forecast[0][0][-8:-6]}h: {round(forecast[0][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[1][0][-8:-6]}h: {round(forecast[1][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[2][0][-8:-6]}h: {round(forecast[2][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[3][0][-8:-6]}h: {round(forecast[3][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    """

    popup = Popup(popup_content, max_width=400)
    popup.add_to(geopoint)
    geopoint.add_to(mymap)

# Save the Map Instance Into a HTML file
mymap.save("map.html")
