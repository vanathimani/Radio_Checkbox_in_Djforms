from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def Registeration(request):
    ERFO=RegiForm() 
    d={'ERFO':ERFO}

    if request.method=='POST':
        DRFO= RegiForm(request.POST)

        if DRFO.is_valid():
            return HttpResponse(str(DRFO.cleaned_data))




    return render(request,'Registeration.html',d)