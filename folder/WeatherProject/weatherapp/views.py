import urllib.request
import json
from django.shortcuts import render


def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://www.weatherapi.com/' +
                                        city + '&units=metric&appid=21cacb89bb0c4863843161528240101').read()
        list_of_data = json.loads(source)

        data = {
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "humidity": str(list_of_data['main']['humidity']) + ' %',
            'description': str(list_of_data['weather'][0]['description']),
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
