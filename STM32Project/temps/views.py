from django.shortcuts import render
from django.http import HttpResponse
import json
import time

from .models import TempData

# Create your views here.

def index(request):

    # Listx = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # Listy = [18.20, 93.2, 9.01, 93.4, 12.90, 13.30, 13.20]

    AllData = TempData.objects.all()

    Listx = []
    Listy = []
    for cc in AllData:
        Listx.append(str(cc.time))
        Listy.append(str(cc.tmp))

    return render(request, 'temps/index.html',
                  {
                      'Listx': json.dumps(Listx),
                      'Listy': json.dumps(Listy)
                  }
                )