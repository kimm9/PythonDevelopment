from .forms import ContactView
from django.contrib import messages 
from django.shortcuts import render,redirect

# Create your views here.
def contact(request):
  if request.method == 'POST':
    form = ContactView(request.POST)
    if form.is_valid():
      our_form = form.save(commit=False)
      our_form.save()
      messages.add_message(
        request, messages.INFO,'Your msg has been sent, Thanks'
        )
      return redirect('/')
  else:
      form = ContactView()
  return render(request,'contact.html', {'form': form,})
