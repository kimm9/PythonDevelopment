from django.contrib import admin
from coin.models import Category, Page, Coin, Portfolio

#Customize admin Model Forms
class PageAdmin(admin.ModelAdmin):
  list_display = ['title', 'category', 'url']

# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(Coin)
admin.site.register(Portfolio)