from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city'].upper()
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=3fd771286ca32ce58f893cc4f6935582').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinates": str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
            "temperature": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        data = {}
        city = ''
    return render(request, "weather/index.html", {'data': data, 'city': city})