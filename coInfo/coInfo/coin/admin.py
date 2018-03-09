from django.contrib import admin
from coin.models import Category, Page, Coin, Portfolio

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Coin)
admin.site.register(Portfolio)