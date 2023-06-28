from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {})

'''def index(response, name):
    ls = ToDoList.objects.get(name = name)
    item = ls.item_set.get(id=1 )
    return HttpResponse("<h1> Day 02 %s</h1><br><br><p>%s<p> " %(ls.name, item.text))'''


def home(response):
    return render(response, "main/home.html", {})
