from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from qumcum_app.models import Item
import json
from django.http.response import JsonResponse

checker = 'false'

def index(request):
    return HttpResponse("Hello, World!")


def item_list(request):
    items = Item.objects.all()
    for item in items:
        item.quantity = 0

    if request.method == 'POST':
        total_price = 0
        for item in items:
            quantity = int(request.POST.get(f"quantity_{item.name}"))
            item.quantity = quantity
            total_price += item.price * item.quantity
        
        if total_price > 0:
            checker = 'true'
            return render(request, 'completed_purchace.html')
            
    return render(request, 'item_list.html', {'items': items})


# def completed_purchace(request):
#     if request.method == 'POST':
        
#         return render(request, 'item_list.html')
    

def check(request):
    if request.method == 'POST':
        if checker == 'true':
            tmp_cheker = checker
            checker = 'False'
            return JsonResponse({'tmp_ckecker':tmp_cheker})
        else:
            return JsonResponse({'ckecker':checker})