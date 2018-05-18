from django.shortcuts import render,redirect,reverse

from django.http import HttpResponse, HttpResponseRedirect

from bookRecommand.models import  LoginForm
import bookRecommand
from DataBaseManagement.database import MyDataBase
from modeles.Book import Book
#=========================================
# 首页
#=========================================
def index(request):
    return render(request,'bookRecommand/bookSearch.html')

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
            request.session['user'] = form.data['username']
    return redirect(reverse(bookRecommand.views.index))

# 退出登录操作
def quitLogin(request):
    request.session['isLogin'] = False
    request.session['user'] = ''
    return redirect(reverse(bookRecommand.views.index))
#=======================================
# 搜索功能
#======================================
def search(request):
    csrfmiddlewaretoken = request.GET.get('csrfmiddlewaretoken',None)
    findCode = request.GET.get('find_code','WRD')
    searchKey = request.GET.get('searchKey',None)
    if not csrfmiddlewaretoken or not searchKey:
        return redirect(reverse(bookRecommand.views.index))
    database = MyDataBase()
    books = []
    result = database.collections.find({'bookName':{'$regex':searchKey}})
    for data in result:
        ISBN = data.get('ISBN','')

        book = Book(ISBN=data.get('ISBN',''),)
        books.append(data)
    print(len(books))
    context = {
        'books':books
    }
    return render(request,'bookRecommand/bookSearch.html',context=context)

