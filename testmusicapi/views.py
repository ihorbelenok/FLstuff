from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def test_view(request):

    response = requests.get("http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=ukraine&limit=10&api_key=5cec56e2d7c52f5deacb9e8ad4fad74c&format=json")
    if response.status_code==200:
        data = response.json()
        artists = []

        for i in range(len(data['topartists']['artist'])):
            info_responce = requests.get("http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&mbid=%s&api_key=5cec56e2d7c52f5deacb9e8ad4fad74c&format=json"%data['topartists']['artist'][i]['mbid'])
            info_data = info_responce.json()

            artist = {"name": data['topartists']['artist'][i]['name'],
                      "url": data['topartists']['artist'][i]['url'],
                      "img": data['topartists']['artist'][i]['image'][3]["#text"],
                      "listeners": data['topartists']['artist'][i]['listeners'],
                      "info": info_data['artist']['bio']['content']}
            artists.append(artist)


    return render(request, 'country.html', {"artists":artists})