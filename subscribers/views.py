from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def subscribers(request):
    template = loader.get_template('base/index.html')
    return HttpResponse(template.render())