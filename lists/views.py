from django.shortcuts import render
from django.http.response import HttpResponse

def home_page(request):
    '''Домашняя страница'''
    return HttpResponse('<html><title>To-Do lists</title></html>')