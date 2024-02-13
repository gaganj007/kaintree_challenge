from django.urls import path
from .views import item_dashboard

urlpatterns = [
    path('item-dashboard/', item_dashboard, name='item-dashboard'),
]