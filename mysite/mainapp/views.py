from django.shortcuts import render


def index(request):
    return render(request, "mainapp/home.html")


def generic(request):
    return render(request, "mainapp/generic.html")