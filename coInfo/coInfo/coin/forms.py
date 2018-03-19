from django import forms 
from coin.models import Category, Page

class CategorForm(forms.ModelForm):
  name = forms.CharField(max_length=128, help_text="Please Enter the Category Name.")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
  likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
  slug = forms.CharField(widget=forms.HiddenInput(), required=False)
  # an inline class to provide additional info on the form

  class Meta:
    # provide a relationship b/w the modelform and modle
    model = Category
    fields = ('name',)

class PageForm(forms.ModelForm):
  title = forms.CharField(max_length=128, help_text="Enter the Title of the page")
  url = forms.URLField(max_length=200, help_text="Enter the URL of the page")
  views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

  class Meta:
    #provide a relation between the modelform and model
    model = Page
    exclude = ('category',)