# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Race

# Create your views here.
def index(request):
    template = loader.get_template('index.html')	        
    context = {}
    return HttpResponse(template.render(context, request))

def races(request):
    if request.method == "GET":
	race_names=[]
	race_query=Race.objects.all()
	for selection in race_query:
	    race_names+=[str(selection.race)]
    template = loader.get_template('races.html')	        
    context = {"race_names":race_names}
    return HttpResponse(template.render(context, request))

def features(request):
    template = loader.get_template('features.html')	        
    context = {}
    return HttpResponse(template.render(context, request))

def classes(request):
    template = loader.get_template('classes.html')	        
    context = {}
    return HttpResponse(template.render(context, request))

def creator(request):
    template = loader.get_template('creator.html')	        
    context = {}
    return HttpResponse(template.render(context, request))

def feats(request):
    template = loader.get_template('feats.html')	        
    context = {}
    return HttpResponse(template.render(context, request))

def spells(request):
    template = loader.get_template('spells.html')	        
    context = {}
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('contact.html')	        
    context = {}
    return HttpResponse(template.render(context, request))


