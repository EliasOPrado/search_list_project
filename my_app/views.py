import requests
from django.shortcuts import render
#Will import %20 after each word for the search adding to the url
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from . import models

BASE_PROJECT_LIST_URL = 'https://losangeles.craigslist.org/search/bbb?query={}'

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    #Pull information from the search bar
    search = request.POST.get('search')
    #Gets the Search class model and retrieves the search form to the database
    #models.Search.objects.create(search=search)
    #will add the search within the url ''bbb?query={HERE}''
    final_url = BASE_PROJECT_LIST_URL.format(quote_plus(search))
    #soup = BeautifulSoup(data, features='html.parser')

    print(final_url)
    response = requests.get(final_url)
    data = response.text
    print(data)


    frontend_stuff = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', frontend_stuff)