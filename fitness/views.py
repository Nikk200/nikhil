from django.shortcuts import render

from fitness.models import Excercise

# Create your views here.


def home(request):
    objectss = Excercise.objects.all()


    return render(request, 'index.html', {'objectss' : objectss})

