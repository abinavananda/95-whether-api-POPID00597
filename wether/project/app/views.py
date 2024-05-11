from django.shortcuts import render
import requests
import datetime
# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city ='india'    
    appid ='53976e29988af56b575e0e84052de623'
    URL ='http://api.openweathermap.org/data/2.5/weather'
    PARAMS ={'q':city,'appid':appid,'units':'metric'}
    r=requests.get(url=URL,params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon =res['weather'][0]['icon']
    temp =res['main']['temp']

    day = datetime.date.today()


    return render(request,'home.html',{'description':description,'icon':icon,'temp': temp,'day':day,'city':city})