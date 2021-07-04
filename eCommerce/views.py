from django.shortcuts import render
import requests


def index(request):
    url = "https://jsonplaceholder.typicode.com/users"
    ur2 = "https://jsonplaceholder.typicode.com/photos"
    r = requests.get(url)
    r2 = requests.get(ur2)
    json = r.json()
    json2 = r2.json()
    return render(request, 'Index.html', {
        'title': "Jaguarete - Ecommerce",
        'products': json,
        'photos': json2
    })
def about(request):
    return render(request,'About.html', {
        'title': "About"
    })

