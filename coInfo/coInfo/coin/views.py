from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context_dict = {'boldmessage': "this is coin message"}
  return render(request, 'coin/index.html', context=context_dict)

def about(request):
  context_dict = {'boldmessage': "this is about coin message from the developer"}
  return render(request, 'coin/about.html', context=context_dict)