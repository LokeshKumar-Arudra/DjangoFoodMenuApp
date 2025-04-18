from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

def index(request):
    items_list = Item.objects.all()  # Extracting data from DB
    # return HttpResponse(items_list)
    context = {
        'item_list' : items_list
    }
    return render(request, 'food/index.html', context)

def item(request):
    # return HttpResponse("This is an Item vIEw")
    return HttpResponse("<h1>This is an Item vIEw</h1>")

def details(request , item_id):
    item = Items.objects.get(pk=item_id)
    context = {
        "item" : item
    }
    return render(request,'food/details.html',context)