from django.urls import path
from . import views

app_name = 'food' # this is a namespace for the app

urlpatterns = [
    path('food/', views.index, name='index'),
    path('item/', views.item, name='item'),
    # food/1 or 2 .....
    path('food/<int:item_id>/',views.details , name='details'),
    path('',views.home,name='home'),
    #add item 8000/food/add/
    path('food/add/',views.create_item, name='create_item'),
    # update item 8000/food/update/1/
    path('food/update/<int:id>/',views.update_item, name='update_item'),

]
