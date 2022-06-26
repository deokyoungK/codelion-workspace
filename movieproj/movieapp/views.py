from django.shortcuts import render
import requests
import json
from .form import searchForm
import my_settings

api_id = my_settings.api_id

def index(request):
    if request.method == 'POST':
        searchform = searchForm(request.POST)
        searchword = request.POST.get('searchword')
        print(searchword)
        if searchform.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+api_id+'&query='+(searchword)+'&page=1'
            response = requests.get(url)
            
            jsdata = response.text
            pydata = json.loads(jsdata)
            pydata = pydata['results']
            return render(request,'search.html',{'pydata':pydata})
    else:
        searchform = searchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key='+api_id
        response = requests.get(url)
        
        jsdata = response.text
        pydata = json.loads(jsdata)
        pydata = pydata['results']

    return render(request,'index.html', {'pydata':pydata,'searchform':searchform})



def detail(request,movie_id):

    url = 'https://api.themoviedb.org/3/movie/'+movie_id+'?api_key='+api_id
    response = requests.get(url)

    jsdata = response.text
    pydata = json.loads(jsdata)
    return render(request,'detail.html',{'pydata':pydata})


