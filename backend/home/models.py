from django.conf import settings
from django.db import models
class Test(models.Model):
    'Generated Model'
    test = models.SlugField(max_length=50,)
