from django import template
from coin.models import Category

register = template.Library()

@register.inclusion_tag('coin/cats.html')
def get_category_list():
  return {'cats': Category.objects.all()}

