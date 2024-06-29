from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request, 'app/home.html')


def product_detail_page(request):
    return render(request, 'app/detail.html')