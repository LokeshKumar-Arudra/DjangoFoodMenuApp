from django.urls import path
from . import views

app_name = 'food' # this is a namespace for the app

urlpatterns = [
    path('food/', views.index, name='index'),
    path('item/', views.item, name='item'),
    # food/1 or 2 .....
    path('food/<int:item_id>/',views.details , name='details'),
    path('',views.home,name='home')
]
