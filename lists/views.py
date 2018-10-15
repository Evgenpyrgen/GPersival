from django.shortcuts import render, redirect
from lists.models import Item, List


def home_page(request):
    """Домашняя страница"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/единственный-список-в-мире/')
    return render(request, 'home.html')


def view_list(request):
    """новый список"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    """новый список"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/единственный-список-в-мире/')
