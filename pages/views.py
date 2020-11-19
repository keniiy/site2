from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def service(request):
    context = {

    }
    return render(request, 'pages/services.html', context)


def contact(request):
    context = {

    }
    return render(request, 'pages/contact-us.html', context)


def book(request):
    context = {

    }
    return render(request, 'pages/book.html', context)