
from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def leadership(request):
    return render(request, 'core/leadership.html')


def projects(request):
    return render(request, 'core/projects.html')


def academics(request):
    return render(request, 'core/academics.html')


def gallery(request):
    return render(request, 'core/gallery.html')


def contact(request):
    return render(request, 'core/contact.html')
