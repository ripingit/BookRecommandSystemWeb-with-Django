# 自动续借爬虫
import datetime
from lxml.html import etree
import requests
from Spider import loginSpider
from Spider.models import Book
import re

headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,
    'Accept-Encoding' : 'gzip, deflate' ,
    'Accept-Language' : 'zh-CN,zh;q=0.9' ,
    'Cache-Control' : 'max-age=0' ,
    'Connection' : 'keep-alive' ,
    'Cookie' : 'UM_distinctid=1633a80bb95339-096e7ba2edcff7-444a022e-144000-1633a80bb9644f; yunsuo_session_verify=197473425a5828dc39985afe6c86cdd6' ,
    'Host' : 'opac.szpt.edu.cn:8991' ,
    'Upgrade-Insecure-Requests' : '1' ,
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' ,
}

# 输入一个日期字符串（不需要标准格式），
# 获得某本书的还书日期距离今天还有多少天
def getBorrowDayDifference(date):
    '''
    获得某本书的日期与当前日期的天数差距
    :param date: 另一本书的日期（不用固定格式）
    '''
    year = date[0:4]
    month = date[4:6]
    day = date[6:]
    dates = '{year}-{month}-{day}'.format(year=year,month=month,day=day)
    day1 = datetime.datetime.now()
    day2 = datetime.datetime.strptime(dates,'%Y-%m-%d')
    return (day2-day1).days+1

# 输入借阅页面的response，
# 获得某一个用户所借阅的所有书籍
def getBorrowBooks(response):
    '''
    获得该名用户所有的当前的借阅的书，并返回
    所有书籍
    :param url:
    :return:
    '''
    selector = etree.HTML(response.text)
    href = selector.xpath('//td[@class="td1" and contains(./preceding-sibling::td[1]/text(),"外借")]/a/@href')[0]
    hrefStartIndex = href.find('\'')
    hrefEndIndex = href.rfind('\'')
    href = href[hrefStartIndex+1:hrefEndIndex]
    print(href)

    booksResponse = requests.get(url=href,headers=headers)
    booksResponse.encoding = 'utf-8'
    booksSelector = etree.HTML(booksResponse.text)

    books = booksSelector.xpath('//tr')
    borrowBooks = []
    booksKey = ['No','著者','题名','出版年','应还日期','分馆','索书号']
    for book in books:
        try:
            inputKey = book.xpath('.//input[@type="checkbox"]/@name')
            bookDetailList = book.xpath('.//td[@class="td1"]//text()')
            author = bookDetailList[1]
            bookName = bookDetailList[2]
            publishYear = bookDetailList[3]
            repayYear = bookDetailList[4]
            branchLibrary = bookDetailList[5]
            index = bookDetailList[6]
            remainingDay = getBorrowDayDifference(repayYear)
            inputKey = inputKey[0]
            bookDetail = Book.BorrowBook(name=bookName,publishYear=publishYear,repayYear=repayYear
                                         ,branchLibray=branchLibrary,index=index,remainingDay=remainingDay,
                                         inputKey=inputKey,author=author)
            borrowBooks.append(bookDetail)
        except:
            continue
    return {'borrowBooks':borrowBooks,'booksResponse':booksResponse}

# 输入一个关于该用户所有书籍的借阅列表，
# 获得某一个用户所借阅所有还书日期小于等于7天的
def getUrgentBorrowBooks(bookDetailList):
    '''
    :param bookDetailList: 该名读者所借阅的全部书籍
    :return: 返回所有remainingDay 小于等于7天的书籍
    '''
    result = []
    for book in bookDetailList:
        if int(book.remainingDay) <= 7:
            result.append(book)
    return result

# 对紧急书籍进行续借，
# 同时发送邮箱通知用户，
# 如果续借失败，
# 发送失败信息给用户





# 传入一个列表和借阅页面的response，对该列表内的所有书籍进行续借,
# 返回续借成功和失败的书籍  [success],[fails]
# 本质上借阅书籍就是一次HTTP的post操作，所以下面的操作需要得到
# post的网址以及进行post时的headers和cookies和data
def autoBorrow(response,bookDetailList):
    #==================================
    # 初始化需要post的data
    borrowData  = {
        'func': 'bor-renew-all',
        'renew_selected': 'Y',
        'adm_library': 'SZY50',
        # 'c001304693000010': 'Y',
    }
    for book in bookDetailList:
        borrowData[book.inputKey] = 'Y'
    print(borrowData)

    #======================================
    # 获得要进行续借post操作的url
    selector = etree.HTML(response.text)
    s = ','.join(selector.xpath('//script//text()'))
    m = re.search('function collectData.*?var strData =(.*?);',s,flags=re.S)
    # 用于续借post的url
    href = (m.group(1)[2:-1])

    response = requests.post(url=href,data=borrowData,headers=headers)
    response.encoding = 'utf-8'
    print(response.text)

    selector = etree.HTML(response.text)


    fails = []
    successes = []

    failBorrowBooks = selector.xpath('//table[contains(./tr/th[last()]/text(),"未能续借的原因")]//tr')
    for failBooks in failBorrowBooks[1:]:
        bookDetail = failBooks.xpath('.//td//text()')
        name = bookDetail[1]
        repayDay = bookDetail[3]
        branchLibrary = bookDetail[5]
        book = Book.BorrowBook(name=name,repayYear=repayDay,branchLibray=branchLibrary)
        fails.append(book)

    successBorrowBooks = selector.xpath('//table[not(contains(./tr/th[last()]/text(),"未能续借的原因"))]//tr')
    for sucessBooks in successBorrowBooks[3:]:
        bookDetail = sucessBooks.xpath('.//td//text()')
        name = bookDetail[1]
        repayDay = bookDetail[3]
        branchLibrary = bookDetail[5]
        book = Book.BorrowBook(name=name, repayYear=repayDay, branchLibray=branchLibrary)
        successes.append(book)
    return successes,fails
if __name__ == "__main__":
    response = loginSpider.login('16240011','19970904')[1]
    r = getBorrowBooks(response)
    l = r['borrowBooks']
    response = r['booksResponse']
    print(getUrgentBorrowBooks(l))
    a = []
    a.append(l[0])
    a.append(l[6])

    l = (autoBorrow(response,a))
    print('续借成功的书籍')
    for i in l[0]:
        print(i)
    print('续借失败的书籍')
    for i in l[1]:
        print(i)
