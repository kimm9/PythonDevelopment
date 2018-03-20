from django.shortcuts import render
from coin.forms import CategoryForm, PageForm
from django.http import HttpResponse
from coin.models import Category, Page

# Create your views here.
def index(request):
  # Get the Database for a list of All categories
  # order the Categories in descending order by likes 
  # get top 5 only or all is less than 5
  # put the list in context_dict

  category_list = Category.objects.order_by('-likes')[:5]
  page_list = Page.objects.order_by('-views')[:5]
  context_dict = {
  'categories': category_list,
  'pages': page_list
  }
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
    print(pages)
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

def add_category(request):
  form = CategoryForm()

  if request.method == 'POST':
    form = CategoryForm(request.POST)
    #is it valid?
    if form.is_valid():
      #save the new cat to db
      cat = form.save(commit=True)
      print(cat, cat.slug)
      return index(request)
    else:
      #supplied form contained errors 
      print(form.errors)
  return render(request, 'coin/add_category.html', {'form': form})

def add_page(request, category_name_slug):
  try:
      category = Category.objects.get(slug=category_name_slug)
  except Category.DoesNotExist:
    category = None

  form = PageForm()
  if request.method == 'POST':
    form = PageForm(request.POST)
    if form.is_valid():
      if category:
        page = form.save(commit=False)
        page.category = category
        page.views = 0 
        page.save()
        print('this is page form', page)
        return show_category(request, category_name_slug)
    else:
      print(form.errors)

  context_dict = {'form': form, 'category': category}
  return render(request, 'coin/add_page.html', context_dict)

