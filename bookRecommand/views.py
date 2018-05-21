from django.shortcuts import render,redirect,reverse

from django.http import HttpResponse, HttpResponseRedirect

from Spider import loginSpider
from bookRecommand.models import  LoginForm
import bookRecommand
from DataBaseManagement.database import MyDataBase
from modeles.Book import Book
from Scheduler.scheduler import scheduled
from DataBaseManagement.database import MyDataBase
import re
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


#========================================================================
# 预登陆界面，也就是如果在首页或者其他可以看到登录按钮的页面按下登录后
# ，触发预登陆控制器，控制器将请求转发至登录界面
#=======================================================================
def preLogin(request):
    '''
        如果登录成功，给用户的session设置一个
        {
            isLogin:True,
            userName:userName,
        }
    '''

    if request.method == 'POST':
        # 获得Post过来的数据
        data = request.POST

        userName = data.get('username','')
        password = data.get('password','')

        # 验证数据是否合法,也就是是否能登录szpt图书馆
        # 如果用户什么也没填，跳转至登录页面，如果用户填了数据
        # 对数据进行验证，验证失败，跳转至登录页面（同时附加错误信息），
        # 验证成功，则判断用户是否是第一次登录，如果是第一次登录
        # 进入邮箱设置页面，设置完成时，插入该用户的信息，并将用户
        # 的登录状态设为已登录，跳转至搜索页面，如果不是第一次登录，
        # 直接跳转到搜索页面。
        if loginSpider.login(userName, password)[0]:
            # 验证成功,查看用户是否是第一次登录

            mydatabase = MyDataBase()
            if mydatabase.isFirstLogin(userName):
                userData = {
                    'userName':userName,
                    'password':password
                }
                mydatabase.userData.insert(userData)
                # 是第一次登录,跳转至邮箱设置界面,并将用户数据插入数据库
                result = render(request,'bookRecommand/setup.html')
            else:
                # 不是第一次登录
                request.session['isLogin'] = True
                request.session['userName'] = userName
                result = render(request,'bookRecommand/bookSearch.html')
            mydatabase.client.close()
            return result
        else:
            # 账号验证失败,跳转至登录界面进行登录，并给出错误信息
            context = {
                'userName':userName,
                'password':password,
                'errorMessage':'账号验证失败，请查看你的用户与密码是否可以登录深职院的图书馆系统'
            }
            return render(request,'bookRecommand/login.html',context=context)
    else:
        request.session['isLogin'] = False
        request.session['userName'] = ''
        return render(request,'bookRecommand/bookSearch.html')
#======================================
# 进行登录操作
#======================================
def login(request):
    return render(request,'bookRecommand/login.html')

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
    findCode = request.GET.get('find_code','AllKeyButNotCatalog')
    searchKey = request.GET.get('searchKey',None)
    sortKey = request.GET.get('sort','Year-Rating-Person')
    page = int(request.GET.get('page',0))
    year = request.GET.get('year',None)     # 用于检索条件的年份显示
    years = {}             # 用于侧边栏的年份显示

    if not csrfmiddlewaretoken or not searchKey:
        return redirect(reverse(bookRecommand.views.index))


    database = MyDataBase()
    books = []

    # 判断查询码，构建查询字典
    if findCode == 'AllKeyButNotCatalog':
        findData = {'$or':[
            {'bookName':{'$regex':searchKey,'$options':'i'}},
            {'content': {'$regex': searchKey, '$options': 'i'}},
            {'author': {'$regex': searchKey, '$options': 'i'}},
            {'ISBN': {'$regex': searchKey, '$options': 'i'}},
            {'publishYear': {'$regex': searchKey, '$options': 'i'}},
            {'index': {'$regex': searchKey, '$options': 'i'}},
            {'publisher': {'$regex': searchKey, '$options': 'i'}},
            {'systemNumber': {'$regex': searchKey, '$options': 'i'}}
        ]}
    elif findCode == 'AllKey':
        findData = {'$or':[
            {'catalog': {'$regex': searchKey, '$options': 'i'}},
            {'bookName':{'$regex':searchKey,'$options':'i'}},
            {'content': {'$regex': searchKey, '$options': 'i'}},
            {'author': {'$regex': searchKey, '$options': 'i'}},
            {'ISBN': {'$regex': searchKey, '$options': 'i'}},
            {'publishYear': {'$regex': searchKey, '$options': 'i'}},
            {'index': {'$regex': searchKey, '$options': 'i'}},
            {'publisher': {'$regex': searchKey, '$options': 'i'}},
            {'systemNumber':{'$regex': searchKey, '$options': 'i'}}
        ]}
    elif findCode == 'CatalogKey':
        findData = {'catalog': {'$regex': searchKey, '$options': 'i'}}
    elif findCode == 'BookNameKey':
        findData = {'bookName': {'$regex': searchKey, '$options': 'i'}}
    elif findCode == 'BookAuthorKey':
        findData = {'author': {'$regex': searchKey, '$options': 'i'}}
    elif findCode == 'BookPublisherKey':
        findData = {'publisher': {'$regex': searchKey, '$options': 'i'}}
    elif findCode == 'ISBNKey':
        findData = {'ISBN': {'$regex': searchKey, '$options': 'i'}}
    elif findCode == 'IndexKey':
        findData = {'index': {'$regex': searchKey, '$options': 'i'}}
    elif findCode == 'SystemNumberKey':
        findData = {'systemNumber':{'$regex': searchKey, '$options': 'i'}}
    else:
        findData = {'$or':[
            {'bookName':{'$regex':searchKey,'$options':'i'}},
            {'content': {'$regex': searchKey, '$options': 'i'}},
            {'author': {'$regex': searchKey, '$options': 'i'}},
            {'ISBN': {'$regex': searchKey, '$options': 'i'}},
            {'publishYear': {'$regex': searchKey, '$options': 'i'}},
            {'index': {'$regex': searchKey, '$options': 'i'}},
            {'publisher': {'$regex': searchKey, '$options': 'i'}},
            {'systemNumber': {'$regex': searchKey, '$options': 'i'}}
        ]}

    # 如果使用年份作为缩小范围
    if year != None:
        findData['publishYear'] = int(year)

    # 判断排序方法
    if sortKey == 'Year-Rating-Person':
        print('按照年份-评分-评论人数降序排序')
        result = database.collections.find(findData).\
            sort([('publishYear', -1),('ratingAverage', -1),('ratingNumberRaters', -1)]).\
            skip(page * 10).\
            limit(10)
    elif sortKey == 'Rating-Year-Person':
        print('按照评分-年份-评论人数降序排序')
        result = database.collections.find(findData).\
            sort([('ratingAverage', -1),('publishYear', -1),('ratingNumberRaters', -1)]).\
            skip(page * 10).\
            limit(10)
    elif sortKey == 'Person-Year-Rating':
        print('按照评论人数-年份-评分-降序排序')
        result = database.collections.find(findData).\
            sort([('ratingNumberRaters', -1),('publishYear', -1),('ratingAverage', -1)]).\
            skip(page * 10).\
            limit(10)
    else:
        print('else的情况')
        result = database.collections.find(findData).\
            sort([('publishYear', -1),('ratingAverage', -1),('ratingNumberRaters', -1)]).\
            skip(page * 10).\
            limit(10)

    count = 0
    for data in result:
        ratingGraphic = []
        for i in range(0,5):
            if i < data.get('ratingAverage',-1)//2:
                 ratingGraphic.append([count,'true'])
            else:
                ratingGraphic.append([count,'false'])
            count += 1
        # 缩短书名
        bookName = data.get('bookName', '')
        bookName = bookName.split()[0]

        book = Book(ISBN=data.get('ISBN',''),
                    bookName=bookName,
                    bookUrl=data.get('bookUrl',''),
                    author=data.get('author',''),
                    content=data.get('content',''),
                    publishYear=data.get('publishYear',-1),
                    bookIndex=data.get('index',''),
                    publisher=data.get('publisher',''),
                    catalog=data.get('catalog',''),
                    douBanId=data.get('douBanId',''),
                    doubanRating=data.get('ratingAverage',-1),
                    doubanRatingPerson=data.get('ratingNumberRaters',-1),
                    doubanSummary=data.get('doubanSummary',''),
                    seriesTitle=data.get('seriesTitle',''),
                    systemNumber=data.get('systemNumber',''),
                    ratingGraphic=ratingGraphic)
        books.append(book)
        years[book.publishYear] = years.get(book.publishYear,0)+1

    # 本次搜索一共有多少条记录
    totalCount = result.count()
    # 总页数
    totalPage = totalCount//10

    # 分页的范围
    start = 0 if page-5<0 else page-5
    end = totalPage if page+5>totalPage else page+5
    pageRange = range(start,end)

    database.client.close()

    context = {
        'findCode':findCode,
        'books':books,
        'searchKey':searchKey,
        'page':page,
        'csrf':csrfmiddlewaretoken,
        'totalCount':totalCount,
        'totalPage':totalPage,
        'range':pageRange,
        'years':years.keys()
    }
    return render(request,'bookRecommand/bookSearch.html',context=context)

#=======================================
# 书籍详情页面的显示
# 根据ISBN号找到书名
#========================================
def bookDetail(request,ISBN):
    database = MyDataBase()

    data = database.collections.find_one({'ISBN':ISBN})
    #=================================================
    # 下面是一本书的详细信息
    #=================================================
    ratingGraphic = []
    count = 0
    for i in range(0, 5):
        if i < data.get('ratingAverage', -1) // 2:
            ratingGraphic.append([count, 'true'])
        else:
            ratingGraphic.append([count, 'false'])
        count += 1
    # 缩短书名
    bookName = data.get('bookName', '')
    bookName = bookName.split()[0]
    book = Book(ISBN=data.get('ISBN', ''),
                bookName=bookName,
                bookUrl=data.get('bookUrl', ''),
                author=data.get('author', ''),
                content=data.get('content', ''),
                publishYear=data.get('publishYear', -1),
                bookIndex=data.get('index', ''),
                publisher=data.get('publisher', ''),
                catalog=data.get('catalog', ''),
                douBanId=data.get('douBanId', ''),
                doubanRating=data.get('ratingAverage', -1),
                doubanRatingPerson=data.get('ratingNumberRaters', -1),
                doubanSummary=data.get('doubanSummary', ''),
                seriesTitle=data.get('seriesTitle', ''),
                systemNumber=data.get('systemNumber', ''),
                ratingGraphic=ratingGraphic)
    database.client.close()
    context = {
        'book':book
    }
    return render(request,'bookRecommand/bookDetail.html',context=context)

#========================================
# 真正的首页
#========================================
def trueIndex(request):
    return render(request,'bookRecommand/index.html')

#===========================================
# 设置自动续借
# 由客户端Ajax请求
#===========================================
def autoBorrow(request):
    data = request.POST
    sched = scheduled.borrowSched
    userName = data.get('userName')
    password = data.get('password')
    key = data.get('key')

    # 恢复自动续借功能
    if key=='resumed':
        pass
    else:
        # 暂停自动续借功能
        pass

    return HttpResponse('succeed')

import json
#======================================
# 用于测试
#=======================================
def _test(request):
    _json = {'succeed':True}
    return HttpResponse(json.dumps(_json),content_type="application/json")
def ttest(request):
    return render(request, 'bookRecommand/setup.html')

#============================================
#  当用户开启自动续借时的验证
#+==========================================
def autoBorrowCheck(request):
    result = False

    database = MyDataBase()
    if database.hasEmail(userName=request.session.get('userName',None)):
        result = True
    _json = {'succeed':result}

    if result:
        data = database.userData.find_one({'userName':request.session.get('userName')})
        userName = data.get('userName')
        password = data.get('password')
        email = data.get('email')
        # 表示开启自动续借的功能
        scheduled.addAutoBorrow(userName,password,(email,))

    return HttpResponse(json.dumps(_json),content_type="application/json")
#============================================
#  当用户开启新书速递时的验证
#+==========================================
def newBookCheck(request):
    result = False

    database = MyDataBase()
    if database.hasEmail(userName=request.session.get('userName',None)) and database.hasTags(userName=request.session.get('userName',None)):
        result = True
    _json = {'succeed':result}

    if result:
        # 表示用户开启新书速递功能，在这基础上，会开启邮件通知用户，如果用户的特别关注名单上有东西
        pass

    database.client.close()
    return HttpResponse(json.dumps(_json),content_type="application/json")

#=========================================
# 为用户设置邮箱
#+=======================================
def sendMessage(request):
    data = request.GET
    email = data.get('email',None)
    userName = request.session.get('userName',None)
    if userName and email:
        mydatabase = MyDataBase()
        mydatabase.userData.update({'userName':userName},{'$set':{'email':email}})
        mydatabase.client.close()
    return render(request,'bookRecommand/setup.html')