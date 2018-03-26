from django.shortcuts import render, redirect
from coin.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from coin.models import Category, Page
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from coin.webhose_search import run_query


# Create your views here.
def index(request):
  #set test cookies
  request.session.set_test_cookie()
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
  #call helper function to handle cookies
  visitor_cookie_handler(request)
  context_dict['visits'] = request.session['visits']
  # get response object to add cookie info
  response = render(request, 'coin/index.html', context=context_dict)
  return response

def about(request):
  #testing cookies 
  if request.session.test_cookie_worked():
    print("Test Cookie Worked")
    request.session.delete_test_cookie()

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
    pages = Page.objects.filter(category=category).order_by('-views')
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

@login_required
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

@login_required
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

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
    else:
      
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'coin/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered,
                  })

def user_login(request):
  #if request is post, pull the relevent info
  if request.method == 'POST':
    #get username and pw given by user
    #info gained by login form
    username = request.POST.get('username')
    password = request.POST.get('password')
    #see if tis valid
    user = authenticate(username=username, password=password)
    #if user object excist, then its right
    if user:
      if user.is_active:
        #if acc is active and valid, user can login
        login(request, user)
        print(user.username)
        return HttpResponseRedirect(reverse('index'))
      else:
        #inactive acc cant be used
        return HttpResponseRedirect("CoInfo account is disabled")
    else:
      print("invalid login details: {0}, {1}".format(username, password))
      return HttpResponse("invalid login details given")\
  #the request is not http post, show login form
  else:
    #no context variables to pass to the template
    return render(request, 'coin/login.html', {})

@login_required
def user_logout(request):
  #when user logged in, log them out
  logout(request)
  #redirect them to homepage
  return HttpResponseRedirect(reverse('index'))

@login_required
def restricted(request):
  return render(request, 'coin/restricted.html', {})

#helper function
def get_server_side_cookie(request, cookie, default_val=None):
  val = request.session.get(cookie)
  if not val:
    val = default_val
  return val

def visitor_cookie_handler(request):
  #this gets the count of visits for the site
  #use cookies.get() to get visits cookie
  #if cookie exists, the value is changed to an intger (all cookies values are strings)
  #if not, default value 1
  visits = int(get_server_side_cookie(request, 'visits', '1'))

  last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
  last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

  #if its been more than a data since last visit
  if(datetime.now() - last_visit_time).days > 0:
    visits = visits + 1
    #update the last visit cookie now
    request.session['last_visit'] = str(datetime.now())
  else:
    #set the last visit cookie
    request.session['last_visit'] = last_visit_cookie  
    #update/set the visits
  request.session['visits'] = visits

def search(request):
  result_list = []

  if request.method == 'POST':
    query = request.POST['query'].strip()
    if query:
      result_list = run_query(query)
  return render(request, 'coin/search.html', {'result_list': result_list})

def track_url(request):
  page_id = None
  url = '/coin/'
  if request.method == 'GET':
    if 'page_id' in request.GET:
      page_id = request.GET['page_id']

      try:
        page = Page.objects.get(id=page_id)
        page.views = page.views + 1
        page.save()
        url = page.url
      except:
        pass
  return redirect(url)

