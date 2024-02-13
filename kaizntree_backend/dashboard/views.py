from django.shortcuts import render
from .models import Item

def item_dashboard(request):
    items = Item.objects.all()
    return render(request, 'dashboard/item_dashboard.html', {'items': items})