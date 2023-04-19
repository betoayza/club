from django.shortcuts import render

# Create your views here.


def subscribers(request):
    return render(request, 'children/subscribers.html', {})


def home(request):
    return render(request, 'children/index.html', {})


def contact(request):
    return render(request, 'children/contact.html', {})


def about(request):
    return render(request, 'children/about.html', {})
