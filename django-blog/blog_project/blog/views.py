from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render, redirect

from blog.models import Post
from blog.forms import PostForm
# Create your views here.

def encode_url(url):
  return url.replace(' ', '_')

def index(request):
  latest_posts = Post.objects.all().order_by('-created_at')
  popular_posts = Post.objects.order_by('-views')[:5] # top five posts by popularity

  print (popular_posts[1].title)
  t = loader.get_template('blog/index.html')
  contest_dict = {'latest_posts': latest_posts, 'popular_posts': popular_posts,
  }

  for post in latest_posts:
    post.url = encode_url(post.title)

  for popular_post in popular_posts:
    popular_post.url = encode_url(popular_post.title)

  c = Context(contest_dict)

  return HttpResponse(t.render(c))

def post(request, post_url):
  single_post = get_object_or_404(Post, title=post_url.replace('_',' '))
  single_post.views += 1 # increment the number of views
  single_post.save() # and save it
  t = loader.get_template('blog/post.html')
  c = Context({'single_post': single_post,})
  return HttpResponse(t.render(c))

def add_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save(commit=True)
      return redirect(index)
    else:
      print(form.errors)
  else:
    form = PostForm()
  return render(request, 'blog/add_post.html', {'form': form})





