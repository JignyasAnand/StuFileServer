from django.db import models

class KeyVal(models.Model):
    key = models.TextField()
    validity = models.IntegerField()

class UrlConts(models.Model):
    url=models.TextField()
    conts=models.TextField()