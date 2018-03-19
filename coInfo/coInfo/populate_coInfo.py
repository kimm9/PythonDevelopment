import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'coInfo.settings')

import django
django.setup()

from coin.models import Category, Page

def populate():

  cryptocurrency_pages = [ 
  {"title": "Coindesk", 
  "url":"https://www.coindesk.com/",
  "views": 100
  },
  {"title": "CCN", 
  "url":"https://www.ccn.com/",
  "views": 200
  },
  {"title": "The Merkle", 
  "url":"http://themerkle.com/",
  "views": 300
  }
  ]
  ethereum_pages = [ 
  {"title": "Ethnews", 
  "url":"https://www.ethnews.com/",
  "views": 130
  },
  {"title": "Ethereum on Cointelegraph", 
  "url":"https://cointelegraph.com/tags/ethereum",
  "views": 230
  },
  {"title": "Ethereum on CCN", 
  "url":"https://www.ccn.com/tag/ethereum/",
  "views": 99
  }
  ]
  bitcoin_pages = [ 
  {"title": "Newsbtc", 
  "url":"http://www.newsbtc.com/",
  "views": 120
  },
  {"title": "Bitcoinwarrior", 
  "url":"https://bitcoinwarrior.net/",
  "views": 140
  },
  {"title": "Coindesk", 
  "url":"https://www.coindesk.com/",
  "views": 280
  }
  ]

  cats = {
  "Cryptocurrencies" : {"pages": cryptocurrency_pages, "views": 128, "likes": 64},
  "Ethereum" : {"pages": ethereum_pages, "views": 64, "likes": 32},
  "Bitcoin" : {"pages": bitcoin_pages, "views": 32, "likes": 16}
  }

  # If you want to add more catergories or pages,
  # add them to the dictionaries above.
  # The code below goes through the cats dictionary, then adds each category,
  # and then adds all the associated pages for that category.
  # if you are using Python 2.x then use cats.iteritems() see
  # http://docs.quantifiedcode.com/python-anti-patterns/readability/
  # for more information about how to iterate over a dictionary properly.

  for cat, cat_data in cats.items():
    c = add_cat(cat, cat_data)
    for p in cat_data["pages"]:
      add_page(c, p["title"], p["url"], p["views"])

  for c in Category.objects.all():
    for p in Page.objects.filter(category=c):
      print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
  p = Page.objects.get_or_create(category=cat, title=title, views=views)[0]
  p.url=url
  p.views=views
  p.save()
  return p

def add_cat(name, cat_data):
  c = Category.objects.get_or_create(name=name)[0]
  c.likes=cat_data["likes"]
  c.views=cat_data["views"]
  c.save()
  return c

if __name__ == '__main__':
  print("Starting coInfo population script...")
  populate()












