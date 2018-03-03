from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render

import requests, pprint
# Create your views here.
pp = pprint.PrettyPrinter(indent=4)

def index(request):
    return render(
        request, 'index.html'
    )

def profile(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    print(geodata)
    return render(request, 'api.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'city': geodata['city'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyBZ9EO0JEsWNABWRMGtTLrteG5tTi7PguA'
        })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def api(request):
    r = requests.get('https://api-public.sandbox.gdax.com/currencies')
    currencies = r.json()
    pp.pprint(currencies)
    return render(request, 'api.html', {

        })


#     for k,v in coins[0].items():
# ...   mylist.append(v)