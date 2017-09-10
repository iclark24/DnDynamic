
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Feature(models.Model):
    feature = models.CharField(max_length=4000,default="None")
    effect = models.CharField(max_length=4000,default="None")
    homebrew = models.BooleanField(default=True)
    def __str__(self):
        return self.feature

class Race(models.Model):
    race = models.CharField(max_length=4000,default="None")
    flavour = models.CharField(max_length=4000,default="None")
    strbonus = models.IntegerField(default=0)
    dexbonus = models.IntegerField(default=0)
    intbonus = models.IntegerField(default=0)
    wisbonus = models.IntegerField(default=0)
    chabonus = models.IntegerField(default=0)
    conbonus = models.IntegerField(default=0)
    ageadult = models.IntegerField(default=0)
    agemax = models.IntegerField(default=0)
    alignment = models.CharField(max_length=4000,default="None")
    heightavg = models.FloatField(default=0)
    size = models.CharField(max_length=4000,default="None")
    speed = models.IntegerField(default=0)
    lang1 = models.CharField(max_length=4000,default="None")
    lang2 = models.CharField(max_length=4000,default="None")
    lang3 = models.CharField(max_length=4000,default="None")
    feature1 = models.ForeignKey(Feature,related_name='feature1',unique=False,default=1)
    feature2 = models.ForeignKey(Feature,related_name='feature2',unique=False,default=1)
    feature3 = models.ForeignKey(Feature,related_name='feature3',unique=False,default=1)
    feature4 = models.ForeignKey(Feature,related_name='feature4',unique=False,default=1)
    toolprof1 = models.CharField(max_length=4000,default="None")
    toolprof2 = models.CharField(max_length=4000,default="None")
    toolprof3 = models.CharField(max_length=4000,default="None")
    weaponprof1 = models.CharField(max_length=4000,default="None")
    weaponprof2 = models.CharField(max_length=4000,default="None")
    weaponprof3 = models.CharField(max_length=4000,default="None")
    homebrew = models.BooleanField(default=True)
    def __str__(self):
        return self.race


