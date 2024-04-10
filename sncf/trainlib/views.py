from django.shortcuts import render
from django.http import HttpResponse
from .models import train
from .models import ville 

import datetime

def index(request) :
    context = {"trains" : train.objects.all(),
        "publication" : datetime.datetime.now(),
    }
    return render(request, "trainlib/index.html", context)

