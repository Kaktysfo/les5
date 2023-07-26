from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def top_sellers_view(request):
    return render(request, 'top-sellers.html')

def product_detail_view(request, product_id):
    return render(request, 'product_detail.html', {'product_id': product_id})