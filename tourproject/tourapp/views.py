from django.shortcuts import render
from .models import Places, Team


# Create your views here.
def demo(request):
    o=Places.objects.all()
    t=Team.objects.all()

    return render(request ,"index.html",{"res":o,"out":t})



