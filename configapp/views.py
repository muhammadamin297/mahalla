from django.shortcuts import render, get_object_or_404
from .models import Viloyat, Tuman, Mahalla

# Create your views here.


def home_view(request):
    return render(request, 'home.html')

def viloyat_list(request):
    viloyatlar = Viloyat.objects.all()
    return render(request, 'viloyat_list.html', {'viloyatlar': viloyatlar})

def tuman_list(request, viloyat_id):
    tumanlar = Tuman.objects.all()
    return render(request, 'tuman_list.html', {'tumanlar': tumanlar})

def mahalla_list(request, tuman_id):
    mahallalar = Mahalla.objects.all()
    return render(request, 'mahalla.html', {'mahallalar': mahallalar})