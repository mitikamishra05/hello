from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('this is my home')
def about(request):
    return HttpResponse('this is my about')
def services(request):
    return HttpResponse('this is my services')
def contact(request):
    return HttpResponse('this is my contact')