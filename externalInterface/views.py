from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import json
import Spider.loginSpider
import Spider.googleSpider
import base64
import DataBaseManagement.mysqlDatabaseComment
from wordcloud import  *
import io
import PIL.Image
# Create your views here.

# 这里是用于给java的后端提供接口的Django App


# 用于登录的接口
def login(request:HttpRequest):
    if request.method == "GET":
        # 获得get过来的数据
        data = request.GET

        userName = data.get('userName','')
        password = data.get('password','')

        isOk = Spider.loginSpider.login(userName,password)[0]

        if(isOk):
            result = {'status':True,'errorMsg':''}
        else:
            result = {'status':False,'errorMsg':'登录失败，检查你的用户名和密码是否正确'}

        return HttpResponse(json.dumps(result), content_type="application/json")

# 用于获取语音验证码的接口
def getVoiceVerificationCode(request:HttpRequest):
    if request.method == "GET":
        getData = request.GET

        content = getData.get('content',None)
        print('content',content)

        # 对得到的content进行base64解密
        content = base64.b64decode(content).decode('UTF-8')

        print('解密后:',content)

        if content:
            # 音频字节流
            bitContent = Spider.googleSpider.GoogleSpider().getAudio(content)
            return HttpResponse(bitContent,content_type='audio/mpeg')
    errorResult = {'status':False,'errorMsg':'请求语音验证码出错'}
    return HttpResponse(json.dumps(errorResult),content_type='application/json')

# 用于获取词云,从mysql数据库中取数据
def getWordCloud(request:HttpRequest):
    if request.method == "GET":
        getData = request.GET

        ISBN = getData.get('ISBN','0')
        # 获得该书的所有评论
        comments = DataBaseManagement.mysqlDatabaseComment.DatabaseComment().query(ISBN)

        # 生成词云
        wordCloud = WordCloud(font_path='simfang.ttf',background_color='white',margin=2).generate(comments)
        '''
        :type :WordCloud
        '''
        imageByteArr = io.BytesIO()

        wordCloud.to_image().save(imageByteArr,format='JPEG')
        imageByteArr = imageByteArr.getvalue()

        return HttpResponse(imageByteArr,content_type='image/jpeg')
    errorResult = {'status':False,'errorMsg':'请求词云出错'}
    return HttpResponse(json.dumps(errorResult),content_type='application/json')


# 用于自动续借的接口
def autoBorrow(request:HttpRequest)->HttpResponse:
    pass
