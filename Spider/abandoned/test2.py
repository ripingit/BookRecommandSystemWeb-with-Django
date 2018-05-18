url = 'https://translate.google.cn/translate_tts?' \
      'ie=UTF-8&' \
      'q=%E6%B1%82%E8%A7%A3%E9%B8%A1%E5%85%94%E5%90%8C%E7%AC%BC%E9%97%AE%E9%A2%98&' \
      'tl=zh-CN&' \
      'total=1&' \
      'idx=0&' \
      'textlen=8&' \
      'tk=931598.544600&' \
      'client=t&' \
      'prev=input&' \
# url = 'https://translate.google.cn/translate_tts?' \
#       'ie=UTF-8&' \
#       'q=%E6%B1%82%E8%A7%A3%E9%B8%A1%E5%85%94%E5%90%8C%E7%AC%BC%E9%97%AE%E9%A2%98&' \
#       'tl=zh-CN&' \
#       'total=1&' \
#       'idx=0&' \
#       'textlen=8&' \
#       'tk=931598.544600&' \
#       'client=t&' \
#       'prev=input'
headers = {
      'Accept-Encoding' : 'identity;q=1, *;q=0' ,
      'chrome-proxy' : 'frfr' ,
      'Range' : 'bytes=0-' ,
      'Referer' : 'https://translate.google.cn/' ,
      'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36' ,
}
import requests
response = requests.get(url=url,headers=headers)
file = open('a.mpeg','wb')
file.write(response.content)
file.flush()