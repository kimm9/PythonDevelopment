from django.shortcuts import render
from django.http import HttpResponse
from coin.models import Category

# Create your views here.
def index(request):
  # Get the Database for a list of All categories
  #order the Categories in descending order by likes 
  # get top 5 only or all is less than 5
  # put the list in context_dict

  category_list = Category.objects.order_by('-likes')[:5]
  context_dict = {'categories': category_list}
  return render(request, 'coin/index.html', context=context_dict)

def about(request):
  context_dict = {'boldmessage': "this is about coin message from the developer"}
  return render(request, 'coin/about.html', context=context_dict)