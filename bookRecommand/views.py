from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from bookRecommand.models import  LoginForm

#=========================================
# 首页
#=========================================
def index(request):
    isLogin = request.session.get('isLogin', False)
    user = request.session.get('user',None)
    data = {
        'isLogin' : isLogin,
        'user' : user
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
            request.session['isLogin'] = True
            request.session['user'] = form.data['user']
            return HttpResponseRedirect('/bookSystem')
        else:
            return render(request, 'bookRecommand/login.html')
    else:
        return render(request,'bookRecommand/login.html')

#=======================================
# 自动续借功能
#=======================================
