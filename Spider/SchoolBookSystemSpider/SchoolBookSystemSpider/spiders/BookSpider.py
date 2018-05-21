# -*- coding: utf-8 -*-

from lxml.html import etree
import scrapy
import requests
import re

from ..items import Book


class BookSpider(scrapy.Spider):
    name = 'BookSpider'

    def __init__(self):
        self.file = open('logaa.txt','w+',encoding='utf-8')
        self.file2 = open('logbb.txt','w+',encoding='utf-8')
        self.file.write('Scrapy被执行了')
        self.file.flush()
        # 计算机类图书的中图分类法
        self.bookNumber = {'TP3': '计算技术、计算机技术', 'TP30': '一般性问题', 'TP301': '理论、方法', 'TP301.1': '自动机理论', 'TP301.2': '形式语言理论', 'TP301.4': '可计算性理论', 'TP301.5': '计算复杂性理论', 'TP301.6': '算法理论', 'TP302': '设计与性能分析', 'TP302.1': '总体设计、系统设计', 'TP302.2': '逻辑设计', 'TP302.4': '制图', 'TP302.7': '性能分析、功能分析', 'TP302.8': '容错技术', 'TP303': '总体结构、系统构造', 'TP304': '材料', 'TP305': '制造、装配、改造', 'TP306': '调整、测试、校验', 'TP307': '检修、维护', 'TP308': '机房', 'TP309': '安全保密', 'TP309.1': '计算机设备安全', 'TP309.2': '数据安全', 'TP309.3': '数据备份与恢复', 'TP309.5': '计算机病毒与防治', 'TP309.7': '加密与解密', 'TP31': '计算机软件', 'TP311': '程序设计、软件工程', 'TP311.1': '程序设计', 'TP311.11': '程序设计方法', 'TP311.12': '数据结构', 'TP311.13': '数据库理论与系统', 'TP311.5': '软件工程', 'TP311.51': '程序设计自动化', 'TP311.52': '软件开发', 'TP311.54': '软件移植', 'TP311.56': '软件工具、工具软件', 'TP312': '程序语言、算法语言', 'TP313': '汇编程序', 'TP314': '编译程、解释程序', 'TP315': '管理程序、管理系统', 'TP316': '操作系统', 'TP316.1': '分时操作系统', 'TP316.2': '实时操作系统', 'TP316.3': '批处理', 'TP316.4': '分布式操作系统、并行式操作系统', 'TP316.5': '多媒体操作系统', 'TP316.6': 'DOS操作系统', 'TP316.7': 'Windows操作系统', 'TP316.8': '网络操作系统', 'TP316.81': 'UNIX操作系统', 'TP316.82': 'XENIX操作系统', 'TP316.83': 'NOVELL操作系统', 'TP316.84': 'OS/2操作系统', 'TP316.86': 'Windows NT操作系统', 'TP316.89': '其他', 'TP316.9': '中文操作系统', 'TP317': '程序包（应用软件）', 'TP317.1': '办公自动化系统', 'TP317.2': '文字处理软件', 'TP317.3': '表处理软件', 'TP317.4': '图像处理软件', 'TP319': '专用应用程序', 'TP32': '一般-计算器和计算机', 'TP321': '非电子计算机', 'TP322': '分析计算机(穿孔卡计算机)', 'TP323': '电子计算器', 'TP33': '电子数字计算机（不连续作用电子计算机）', 'TP331': '基本电路', 'TP331.1': '逻辑电路', 'TP332': '运算器、控制器（CPU）', 'TP332.1': '逻辑部件', 'TP332.2': '运算器', 'TP332.3': '控制器、控制台', 'TP333': '存贮器', 'TP333.1': '内存贮器(主存贮器)总论', 'TP333.2': '外存贮器(辅助存贮器)总论', 'TP333.3': '磁存贮器及其驱动器', 'TP333.4': '光存贮器及其驱动器', 'TP333.5': '半导体集成电路存贮器', 'TP333.6': '起导体存贮器', 'TP333.7': '只读(ROM)存贮器', 'TP333.8': '随机存取存贮器', 'TP334': '外部设备', 'TP334.1': '终端设备', 'TP334.2': '输入设备', 'TP334.3': '输入设备', 'TP334.4': '输入输出控制器', 'TP334.5': '外存储器', 'TP334.7': '接口装置、插件', 'TP334.8': '打印装置', 'TP334.9': '其他', 'TP335': '信息转换及其设备', 'TP336': '总线、通道', 'TP337': '仿真器', 'TP338': '各种电子数字计算机', 'TP338.1': '微型计算机', 'TP338.2': '小型计算机', 'TP338.3': '中型计算机', 'TP338.4': '大型计算机、巨型计算机', 'TP338.6': '并行计算机', 'TP338.7': '陈列式计算机', 'TP338.8': '分布式计算机', 'TP34': '电子模拟计算机（连续作用电子计算机)', 'TP342': '运算放大器和控制器', 'TP343': '存贮器', 'TP344': '输入器、输出器', 'TP346': '函数发生器', 'TP347': '延时器', 'TP348': '各种电子模拟计算机', 'TP35': '混合电子计算机', 'TP352': '数字-模拟计算机', 'TP353': '模拟-数字计算机', 'TP36': '微型计算机', 'TP37': '多媒体技术与多媒体计算机', 'TP38': '其他计算机', 'TP381': '激光计算机', 'TP382': '射流计算机', 'TP383': '超导计算机', 'TP384': '分子计算机', 'TP387': '第五代计算机', 'TP39': '计算机的应用', 'TP391': '信息处理(信息加工）', 'TP391.1': '文字信息处理', 'TP391.11': '汉字信息编码', 'TP391.12': '汉字处理系统', 'TP391.13': '表格处理系统', 'TP391.14': '文字录入技术', 'TP391.2': '翻译机', 'TP391.3': '检索机', 'TP391.4': '模型识别与装置', 'TP391.41': '图像识别及其装置', 'TP391.42': '声音识别及其装置', 'TP391.43': '文字识别及其装置', 'TP391.5': '诊断机', 'TP391.6': '教学机', 'TP391.7': '机器辅助技术', 'TP391.72': '机器辅助设计(CAD)、辅助制图', 'TP391.73': '机器辅助制造(CAM)', 'TP391.75': '机器辅助计算(CAC)', 'TP391.76': '机器辅助测试（CAT）', 'TP391.77': '机器辅助分析（CAA）', 'TP391.8': '控制机', 'TP391.9': '计算机仿真机', 'TP393': '计算机网络', 'TP393.0': '一般性问题', 'TP393.02': '计算机网络结构与设计', 'TP393.03': '网络互连技术', 'TP393.04': '通信规程、通信协议', 'TP393.05': '网络设备', 'TP393.06': '计算机网络测试、运行', 'TP393.07': '计算机网络管理', 'TP393.08': '计算机网络安全', 'TP393.09': '计算机网络应用程序', 'TP393.1': '局部网(LAN)、城域网（MAN）', 'TP393.11': '以太网', 'TP393.12': '令牌网', 'TP393.13': 'DQDB网（分布队列双总线网络）', 'TP393.14': 'FDDI网（高速光纤环网）', 'TP393.15': 'ATM局域网', 'TP393.17': '无线局域网', 'TP393.18': '校园网、企业网（Ineranet）', 'TP393.2': '广域网（WAN）', 'TP393.3': '洲际网络', 'TP393.4': '国际互联网', 'TP399': '在其他方面的应用'}

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'opac.szpt.edu.cn:8991',
            'Referer': 'http://opac.szpt.edu.cn:8991/F',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }
        self.cookies = {
            'yunsuo_session_verify': 'd21eb089dde2f05fd34ee94b269914f2'
        }

    def start_requests(self):
        self.totalCount = 0

        # 获取秘钥
        self.secretKey = self.getSecretKey()

        # 要搜索的图书的分类号
        searchNumber = ['TP317.5','TP317.6','TP301.5', 'TP301.2', 'TP302.2', 'TP302.7', 'TP302.8', 'TP303', 'TP305', 'TP307', 'TP306', 'TP308', 'TP309.2', 'TP309.3', 'TP309.5', 'TP309.7', 'TP311.51', 'TP311.11', 'TP311.12', 'TP311.13', 'TP311.52', 'TP311.56', 'TP313', 'TP316.1', 'TP315', 'TP314', 'TP316.2', 'TP316.3', 'TP312', 'TP316.4', 'TP316.6', 'TP316.81', 'TP316.83', 'TP316.9', 'TP316.84', 'TP316.86', 'TP316.89', 'TP317.2', 'TP317.1', 'TP317.3', 'TP316.7', 'TP319', 'TP331.1', 'TP323', 'TP332.2', 'TP332.3', 'TP333.1', 'TP333.2', 'TP333.3', 'TP332.1', 'TP333.5', 'TP333.4', 'TP334.1', 'TP334.3', 'TP334.2', 'TP334.7', 'TP334.8', 'TP335', 'TP336', 'TP338.2', 'TP338.3', 'TP338.4', 'TP338.7', 'TP338.6', 'TP338.8', 'TP37', 'TP381', 'TP387', 'TP391.12', 'TP391.2', 'TP391.14', 'TP391.3', 'TP391.13', 'TP391.42', 'TP391.43', 'TP391.6', 'TP391.41', 'TP391.72', 'TP391.76', 'TP391.73', 'TP391.75', 'TP391.9', 'TP393.03', 'TP393.02', 'TP393.06', 'TP393.07', 'TP393.08', 'TP393.11', 'TP393.09', 'TP393.18', 'TP393.2', 'TP399', 'TP393.4','TP301.6']

        for key,value in self.bookNumber.items():
            if key not in searchNumber:
                searchNumber.append(key)

        Tp311_138_searchNumber = ['TP311.138C', 'TP311.138H', 'TP311.138D', 'TP311.138F', 'TP311.138A', 'TP311.138I', 'TP311.138N', 'TP311.138P', 'TP311.138M', 'TP311.138O', 'TP311.138R', 'TP311.138T', 'TP311.138U', 'TP311.138S', 'TP311.138V']
        TP311_56_searchNumber = ['TP311.561','TP311.56%2FB', 'TP311.56%2FD', 'TP311.56%2FA', 'TP311.56%2FE', 'TP311.56%2FG', 'TP311.56%2FC', 'TP311.56%2FF', 'TP311.56%2FH', 'TP311.56%2FJ', 'TP311.56%2FO', 'TP311.56%2FK', 'TP311.56%2FN', 'TP311.56%2FM', 'TP311.56%2FL', 'TP311.56%2FQ', 'TP311.56%2FP', 'TP311.56%2FR', 'TP311.56%2FS', 'TP311.56%2FT', 'TP311.56%2FW', 'TP311.56%2FY', 'TP311.56%2FZ', 'TP311.56%2FX']

        TP312searchNumber = ['TP312H', 'TP312G', 'TP312B', 'TP312D', 'TP312I', 'TP312E', 'TP312L', 'TP312F', 'TP312M', 'TP312A', 'TP312O', 'TP312R', 'TP312S', 'TP312P', 'TP312U', 'TP312V', 'TP312W', 'TP312X']

        TP312JAsearchNumber = ['TP312JA%2FE', 'TP312JA%2FA', 'TP312JA%2FB', 'TP312JA%2FG', 'TP312JA%2FH', 'TP312JA%2FC', 'TP312JA%2FF', 'TP312JA%2FD', 'TP312JA%2FK', 'TP312JA%2FJ', 'TP312JA%2FM', 'TP312JA%2FL', 'TP312JA%2FO', 'TP312JA%2FN', 'TP312JA%2FP', 'TP312JA%2FQ', 'TP312JA%2FS', 'TP312JA%2FR', 'TP312JA%2FT', 'TP312JA%2FX', 'TP312JA%2FW', 'TP312JA%2FZ', 'TP312JA%2FY']

        TP391_41searchNumber = ['TP391.414','TP391.413','TP391.412','TP391.411','TP391.41%2FB', 'TP391.41%2FA', 'TP391.41%2FE', 'TP391.41%2FC', 'TP391.41%2FD', 'TP391.41%2FG', 'TP391.41%2FF', 'TP391.41%2FH', 'TP391.41%2FK', 'TP391.41%2FJ', 'TP391.41%2FM', 'TP391.41%2FN', 'TP391.41%2FP', 'TP391.41%2FO', 'TP391.41%2FL', 'TP391.41%2FQ', 'TP391.41%2FS', 'TP391.41%2FR', 'TP391.41%2FT', 'TP391.41%2FX', 'TP391.41%2FW', 'TP391.41%2FY', 'TP391.41%2FZ']

        TP393_09searchNumber = ['TP393.092.2','TP393.09%2FE', 'TP393.09%2FB', 'TP393.09%2FA', 'TP393.09%2FC', 'TP393.09%2FF', 'TP393.09%2FD', 'TP393.09%2FH', 'TP393.09%2FG', 'TP393.09%2FJ', 'TP393.09%2FN', 'TP393.09%2FK', 'TP393.09%2FL', 'TP393.09%2FM', 'TP393.09%2FP', 'TP393.09%2FR', 'TP393.09%2FQ', 'TP393.09%2FT', 'TP393.09%2FS', 'TP393.09%2FW', 'TP393.09%2FX', 'TP393.09%2FY', 'TP393.09%2FZ']

        TP393_4searchNumber = ['TP393.409','TP393.4%2FE', 'TP393.4%2FC', 'TP393.4%2FA', 'TP393.4%2FF', 'TP393.4%2FD', 'TP393.4%2FG', 'TP393.4%2FH', 'TP393.4%2FB', 'TP393.4%2FK', 'TP393.4%2FJ', 'TP393.4%2FL', 'TP393.4%2FN', 'TP393.4%2FM', 'TP393.4%2FO', 'TP393.4%2FQ', 'TP393.4%2FP', 'TP393.4%2FR', 'TP393.4%2FS', 'TP393.4%2FT', 'TP393.4%2FW', 'TP393.4%2FX', 'TP393.4%2FY', 'TP393.4%2FZ']

        TP312C_searchNumber = ['TP312C%2FE', 'TP312C%2FA', 'TP312C%2FD', 'TP312C%2FF', 'TP312C%2FG', 'TP312C%2FB', 'TP312C%2FH', 'TP312C%2FC', 'TP312C%2FJ', 'TP312C%2FK', 'TP312C%2FM', 'TP312C%2FL', 'TP312C%2FO', 'TP312C%2FP', 'TP312C%2FN', 'TP312C%2FQ', 'TP312C%2FR', 'TP312C%2FS', 'TP312C%2FT', 'TP312C%2FW', 'TP312C%2FY', 'TP312C%2FZ', 'TP312C%2FX']

        TP311_5searchNumber = ['TP311.5%2FE', 'TP311.5%2FA', 'TP311.5%2FG', 'TP311.5%2FD', 'TP311.5%2FB', 'TP311.5%2FC', 'TP311.5%2FH', 'TP311.5%2FF', 'TP311.5%2FJ', 'TP311.5%2FK', 'TP311.5%2FL', 'TP311.5%2FN', 'TP311.5%2FM', 'TP311.5%2FR', 'TP311.5%2FS', 'TP311.5%2FQ', 'TP311.5%2FP', 'TP311.5%2FT', 'TP311.5%2FW', 'TP311.5%2FX', 'TP311.5%2FY', 'TP311.5%2FZ']

        TP311_5NsearchNumber = ['TP311.51','TP311.52','TP311.53','TP311.54','TP311.55']

        TP312BA_searchNumber = ['TP312BA%2FE', 'TP312BA%2FG', 'TP312BA%2FD', 'TP312BA%2FF', 'TP312BA%2FA', 'TP312BA%2FH', 'TP312BA%2FC', 'TP312BA%2FB', 'TP312BA%2FM', 'TP312BA%2FK', 'TP312BA%2FN', 'TP312BA%2FJ', 'TP312BA%2FL', 'TP312BA%2FQ', 'TP312BA%2FO', 'TP312BA%2FP', 'TP312BA%2FR', 'TP312BA%2FS', 'TP312BA%2FT', 'TP312BA%2FZ', 'TP312BA%2FW', 'TP312BA%2FX', 'TP312BA%2FY']

        searchNumber += Tp311_138_searchNumber + TP311_56_searchNumber + TP312searchNumber + TP312JAsearchNumber + TP391_41searchNumber + TP393_09searchNumber + TP393_4searchNumber + TP312C_searchNumber + TP311_5searchNumber + TP311_5NsearchNumber+TP312BA_searchNumber

        # searchNumber = TP312JAsearchNumber


        for number in searchNumber:
            # for i in range(65,92):
            #     s = number+chr(i)
            url = 'http://opac.szpt.edu.cn:8991/F/{}?func=find-b&find_code=CAL&request={}%3F&jump=1&pag=now'.format(self.secretKey,number)
            yield scrapy.Request(url, callback=self.parseBookListNew, headers=self.headers,
                                 cookies=self.cookies,meta={'searchNumber':number,'nowJump':1})
    # 获取秘钥
    def getSecretKey(self):
        keyUrl = 'http://opac.szpt.edu.cn:8991/F'
        response = requests.get(url=keyUrl)
        response.encoding = 'utf-8'

        selector = etree.HTML(response.text)
        secretKey = selector.xpath('//form/@action')[0]

        startIndex = secretKey.find('/F/') + 3

        secretKey = secretKey[startIndex:]
        return secretKey

    # 获取当前jumps数
    def getJumps(self,url):
        m = re.search('jump=(.*?)&',url)
        return int(m.group(1))
    # 获得最大记录数
    def getMaxJump(self,selector):
        s = (''.join(selector.xpath('//div[@id="hitnum"]/text()'))).strip().replace(' ', '')
        m = re.search('of(\d+?)\(', s)
        return int(m.group(1))
    # 判断是否是第一页
    def isNoOne(self,url):
        m = re.search('jump=(\d+)', url)
        page = int(m.group(1))
        if page == 1:
            return True
        else:
            return False



    # 新的爬取一页的方法
    def parseBookListNew(self, response):
        selector = etree.HTML(response.text)
        if self.isNoOne(response.url):
            # 下面获取每本图书的url入口
            items = selector.xpath('//table[@class="items"]//td[@class="col2"]')
            for item in items:
                # 书名
                bookName = (item.xpath('.//div[@class="itemtitle"]/a/text()'))[0].strip()
                # 索书号
                index = item.xpath('.//td[@class="content" and contains(preceding-sibling::td[1]/text(),"索书号")]/text()')[0].strip()
                # 出版社
                publisher = item.xpath('.//td[@class="content" and contains(preceding-sibling::td[1]/text(),"出版社")]/text()')[0].strip()
                # 出版年份
                publishYear = item.xpath('.//td[@class="content" and contains(preceding-sibling::td[1]/text(),"年份")]/text()')[0].strip()
                # 书籍详情页面的url
                bookUrl = item.xpath('.//div[@class="itemtitle"]/a/@href')[0].strip()
                # 进入书籍详情页面获取每本书的详情信息
                yield scrapy.Request(url=bookUrl,headers=self.headers,cookies=self.cookies,callback=self.parseBookDetailNew,
                                    meta={
                                        'bookName': bookName,
                                        'index' : index,
                                        'publisher' : publisher,
                                        'publishYear' : publishYear,
                                        'bookUrl' : bookUrl
                                    })
                break
    def parseBookDetailNew(self, response):
        meta = response.meta
        selector = etree.HTML(response.text)
        # 书名
        bookName = ''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"题名")]//text()')).strip()
        # 出版社
        publisher = ''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"出版发行")]//text()')).strip()
        # 索书号
        index = ''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"索书号")]//text()')).strip()
        # 出版年份
        publishYear = ''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"出版发行")]//text()')).split(',')[1].strip()
        try:
            publishYear = int(publishYear)
        except:
            publishYear = -1
        # 摘要
        content = ''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"摘要")]//text()')).strip()
        # 书籍Url
        bookUrl = response.url
        # 作者
        author = ''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"个人著者")]//text()')).strip()
        # ISBN码
        ISBN  = (''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"ISBN")]//text()')).strip()).split('\xa0')[0].replace('-','')
        # 系统号
        systemNumber = selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"系统号")]//text()')[0].strip()
        item = Book(_id=ISBN,ISBN=ISBN,bookName=bookName,bookUrl=bookUrl,author=author,content=content,publishYear=publishYear,index=index,publisher=publisher,systemNumber=systemNumber)

        # 交给pipline来写入数据库
        yield item

        nextPage = self.getNextPage(response)

        if nextPage:
            yield scrapy.Request(url=nextPage,headers=self.headers,cookies=self.cookies,callback=self.parseBookDetailNew)


    def getNextPage(self,response):
        selector = etree.HTML(response.text)
        html = selector.xpath('//script[contains(text(),"下一条记录")]/text()')[0]
        selector = etree.HTML(html)
        try:
            return (selector.xpath('//a/@href')[0])
        except:
            return None