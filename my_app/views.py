import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    #Pull information from the search bar
    search = request.POST.get('search')
    print(search)
    frontend_stuff = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', frontend_stuff)