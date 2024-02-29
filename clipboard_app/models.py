from django.db import models

# Create your models here.

class Clipboard(models.Model):
  title = models.CharField(max_length = 255,null=True,blank=True)
  paste = models.TextField(null=True,blank=True)