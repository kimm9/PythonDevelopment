from django.contrib import admin
from coin.models import Category, Page, Coin, Portfolio

#Customize admin Model Forms
class PageAdmin(admin.ModelAdmin):
  list_display = ['title', 'category', 'url']

#create category class to customize admin interface
class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Coin)
admin.site.register(Portfolio)