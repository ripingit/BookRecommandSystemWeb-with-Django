from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    data = {
        'title':'django test',
        'content':'hi man'
    }
    return render(request,'bookRecommand/index.html',context=data)

def detail(request,**kwargs):
    data = {
        'postnumber':kwargs['pk']
    }
    return render(request,'bookRecommand/detail.html',context=data)