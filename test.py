# import requests
#
# url = 'https://m.wanplus.com/match/49269.html#data'
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'max-age=0',
#     'cookie': 'wanplus_token=20050060cf342f633fecd83642f7291a; wanplus_storage=lf4m67eka3o; wanplus_sid=da0507b65c4bf79a2aa8ee870bcd3a0c; wanplus_csrf=_csrf_tk_1676322; wp_pvid=1304659945; wp_info=ssid=s8708766685; gameType=1',
#     'referer': 'https://m.wanplus.com/schedule/42611.html',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
# }
# response = requests.get(url=url,headers=headers)
# print(response.text)

from wordcloud import *
from matplotlib import pyplot as plt

from wordcloud import *
from matplotlib import pyplot as plt
# 读取西游记文件
# f = open(u'西游记.txt','r',encoding='utf-8').read()

# 生成WordCloud对象
wordcloud=WordCloud(font_path='WordCloudUntitled/simhei.ttf',background_color='white',width=1000,height=860,margin=2).generate("asdasdasdasdsadasdas")

# 使用plt库的imshow方法显示词云图像
plt.imshow(wordcloud)
# 取消坐标轴的显示
plt.axis('off')
plt.show()