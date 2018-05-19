from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^login$',views.login,name='login'),   # 登录功能
    url(r'^quitLogin$',views.quitLogin,name='quitLogin'),   # 退出登录
    url(r'^searchwithpymongo$',views.search,name='search'), # 搜索功能
    url(r'^test$',views._test,name='test'),  # 用于测试的功能
]