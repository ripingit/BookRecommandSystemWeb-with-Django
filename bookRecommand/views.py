from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

from bookRecommand.models import  LoginForm


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

#======================================
# 进行登录操作
#======================================
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse('恭喜你，登录成功了')
        else:
            return render(request, 'bookRecommand/login.html')
    else:
        return render(request,'bookRecommand/login.html')
