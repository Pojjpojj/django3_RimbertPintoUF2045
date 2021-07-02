from django.shortcuts import render
from Portfolio import models
# Create your views here.
def verGaleria(request):
    portfolios = models.Image.objects.filter(status='activa')
    return render(request,'portfolio/index.html',{"portfolios":portfolios})