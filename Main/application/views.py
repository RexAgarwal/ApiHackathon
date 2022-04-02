import json
from django.shortcuts import render, redirect

def home(request):
    return render(request, "application/home.html")


def Get(request):
    headers = {'Content-Type': 'application/json', 'Authorization': 'Basic XXXXXXXXXX='}
    body = { "Tenant" : "devED" }
    response = request.POST('https://newsdata.io/api/1/news?apikey=pub_606798203427a7e9bdc661bab3d700a35947').json()
    print(response)
    # Parse message as json
    # response = json.loads(response['Message'])
    
    dict={
        'response' : response,
    }
    return render(request, 'application/home.html', dict)


