import requests
import json
from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import JsonResponse


def appsearcher(request):
    return render(request, 'appsearcher/appsearcher.html')


def header(request):
    return render(request, 'appsearcher/header.html')


def getPlayStoreInfo(request):
    packageName = request.GET.get('id', None)
    headers = {
        "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }
    url = 'https://play.google.com/store/apps/details?id=' + packageName
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.title.text
    for e in soup.findAll('br'):
        e.extract()
    for f in soup.findAll('b'):
        f.extract()
    info = soup.find('div', {'jsname': 'sngebd'}).text
    image = soup.find('img', {'class': 'T75of sHb2Xb'})
    imgurl = image["src"]
    developer = soup.find('a', {'class': 'hrTbp R8zArc'}).text
    rating = soup.find('div', {'class': 'BHMmbe'}).text
    review = soup.find('span', {'class': 'EymY4b'}).text
    downloads = soup.findAll('span', {'class': 'htlgb'})[5]

    data = {
        'title': title,
        'image': imgurl,
        'info': info,
        'downloads': downloads,
        'rating': rating,
        'reviews': review,
        'developer': developer
    }
    new_data = json.dumps(data, ensure_ascii=False, default=str)
    return JsonResponse(new_data, safe=False)


def getIosStoreInfo(request):
    appId = request.GET.get('id', None)
    applicationName = request.GET.get('appname', None)
    headers = {
        "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }
    url = 'https://apps.apple.com/in/app/' + applicationName + "/id" + appId
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.title.text
    for e in soup.findAll('br'):
        e.extract()
    for f in soup.findAll('b'):
        f.extract()
    info = soup.find('div', {'class': 'section__description'})
    imgurl = soup.find('img')['src']
    developer = soup.find('dd', {'class': 'information-list__item__definition l-column medium-9 large-6'}).text
    rating = soup.find('span', {'class': 'we-customer-ratings__averages__display'}).text
    review = soup.find('div', {'class': 'we-customer-ratings__count small-hide medium-show'}).text

    data = {
        'title': title,
        'image': imgurl,
        'info': info,
        'rating': rating,
        'reviews': review,
        'developer': developer
    }
    new_data = json.dumps(data, ensure_ascii=False, default=str)
    return JsonResponse(new_data, safe=False)
