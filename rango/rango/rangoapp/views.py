from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context_dict = {'boldmessage': "this is rango message"}
  return render(request, 'rangoapp/index.html', context=context_dict)


def about(request):
  return HttpResponse("About rango! <br> <a href='/'> Main Page </a>")