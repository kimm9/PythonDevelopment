from django.db import models

import datetime

# Create your models here.

#contact form model

class contactForm(models.Model):
  name = models.CharField(max_length=150)
  email = models.EmailField(max_length=250)
  topic = models.CharField(max_length=200)
  message = models.CharField(max_length=1000)
  timestamp = models.DateTimeField(
      auto_now_add=True
    )

def __unicode__(self):
  return self.email

class Meta:
  ordring = ['-timestamp']
    