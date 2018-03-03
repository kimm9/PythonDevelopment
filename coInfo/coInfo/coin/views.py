from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context_dict = {'boldmessage': "this is coin message"}
  return render(request, 'coin/index.html', context=context_dict)

def about(request):
  return HttpResponse("About coInfo! <br> <a href='/'> Main Page </a>")