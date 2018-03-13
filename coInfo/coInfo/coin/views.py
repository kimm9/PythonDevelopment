from django.shortcuts import render
from django.http import HttpResponse
from coin.models import Category, Page

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

def show_category(request, category_name_slug):
  #create a context dict which we pass to template rendering 
  context_dict = {}

  try:
    #find a category name slug
    #if we cant, the .get() method raises a DoesNotExist Exception
    # .get() method returns one model instance or raises an exception
    category = Category.objects.get(slug=category_name_slug)
    #retrieve all of the associated pages
    #note that filter function will return a list of page objects or an empty list
    pages = Page.objects.filter(category=category)
    #adds our results list to the template context under name pages
    context_dict['pages'] = pages
    #add category object from the database to the context dictionary
    context_dict['category'] = category
  except Category.DoesNotExist:
    #this runs when no specified category is found
    #do nothing
    context_dict['category'] = None
    context_dict['pages'] = None
  #render response
  return render(request, 'coin/category.html', context_dict)



