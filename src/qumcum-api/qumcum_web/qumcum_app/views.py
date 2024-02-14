from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from qumcum_app.models import Item
import json
from django.http.response import JsonResponse

purchase_flag = 'false'

def index(request):
    return HttpResponse("Hello, World!")

def item_list(request):
    items = Item.objects.all()
    global purchase_flag
    for item in items:
        item.quantity = 0

    if request.method == 'POST':
        total_price = 0
        for item in items:
            quantity = int(request.POST.get(f"quantity_{item.name}"))
            item.quantity = quantity
            total_price += item.price * item.quantity
        
        if total_price > 0:
            purchase_flag = 'true'
            return render(request, 'completed_purchace.html')
            
    return render(request, 'item_list.html', {'items': items})


def completed_purchase(request):
    if request.method == 'POST':
        
        return render(request, 'item_list.html')
    

def purchase_status(request):
    global purchase_flag
    #if request.method == 'POST':
    if purchase_flag == 'true':
        tmp_purchase_flag = purchase_flag
        purchase_flag = 'false'
        return JsonResponse({'purchase_flag':tmp_purchase_flag})
    else:
        return JsonResponse({'purchase_flag':purchase_flag})