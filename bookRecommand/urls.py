from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^login$',views.preLogin,name='login'),   # 登录功能
    url(r'^quitLogin$',views.quitLogin,name='quitLogin'),   # 退出登录
    url(r'^searchwithpymongo$',views.search,name='search'), # 搜索功能
    url(r'^bookDetail/(?P<ISBN>\d+)/$',views.bookDetail,name='bookDetail'),
    url(r'^trueIndex$',views.trueIndex,name='trueIndex'),    # 首页的显示
    url(r'^autoBorrow$',views.autoBorrowCheck,name='autoBorrowCheck'), # 检查自动续借
    url(r'^sendMessage$',views.sendMessage,name='sendMessage'),     #插入邮箱
    url(r'^newBook$',views.newBookCheck,name='newBookCheck'), # 检查新书速递
    url(r'^addSpecialAttention$',views.addSpecialAttention,name='addSpecialAttention'), # 增加特别关注标签
    url(r'^forceBorrowBookAndNewBook$',views.forceBorrowBookAndNewBook,name='forceBorrowBookAndNewBook'),
    url(r'^ttest$',views.ttest,name='ttest')    # test2 # 用于测试的功能
]