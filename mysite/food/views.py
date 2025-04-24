from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
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
    item = Item.objects.get(pk=item_id)
    context = {
        "item" : item
    }
    return render(request,'food/details.html',context)

def home(request):
    return HttpResponse("<h1><i>Welcome to Food Menu page</i></h1>")

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index') 
    return render(request,'food/item-form.html', {'form' : form})

def update_item(request , id):
    item = Item.objects.get(pk=id) # Model.objects.get()
    form = ItemForm(request.POST or None , instance=item) # instance is used to pass the prefilled data
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html', {'item': item, 'form' : form}) 
    # in this line we are passing "item" as a key value pair to render it in item-form.html 

def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item': item})
