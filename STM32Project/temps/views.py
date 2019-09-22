from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):

    Listx = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    Listy = [1820, 932, 901, 934, 1290, 1330, 1320]

    return render(request, 'temps/index.html',
                  {
                      'Listx': json.dumps(Listx),
                      'Listy': json.dumps(Listy)
                  }
                )