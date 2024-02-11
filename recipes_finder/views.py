from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Recipe Finder!</h1>")

def about(request):
    return HttpResponse("<h1>This is a Recipe Finder app for users to find a recipe by entering some ingredients. </h1>")