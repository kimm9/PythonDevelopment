from django.shortcuts import render
from django.http import HttpResponse
from coin.models import Category

# Create your views here.
def index(request):
  # Get the Database for a list of All categories
  #order the Categories in descending order by likes 
  context_dict = {'boldmessage': "this is coin message"}
  return render(request, 'coin/index.html', context=context_dict)

def about(request):
  context_dict = {'boldmessage': "this is about coin message from the developer"}
  return render(request, 'coin/about.html', context=context_dict)