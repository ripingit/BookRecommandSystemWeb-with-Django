url = 'https://frodo.douban.com/api/v2/book/1770782/reviews?rtype=review&start=0&count=30&version=0&order_by=hot&channel=ali_market&os_rom=android&apikey=0dad551ec0f84ed02907ff5c42e8ec70&udid=c0e187b56f9b6034daa8773f89776acd1e0c80cd&_sig=zYEnZoWd4hnui38FzgKUUzxtOMI%3D&_ts=1526037509'
# 0dad551ec0f84ed02907ff5c42e8ec70
# 0dad551ec0f84ed02907ff5c42e8ec70
#
# c0e187b56f9b6034daa8773f89776acd1e0c80cd
# c0e187b56f9b6034daa8773f89776acd1e0c80cd
headers = {
    'User-Agent' : 'api-client/1 com.douban.frodo/5.25.0(133) Android/19 product/sagit vendor/Xiaomi  model/MI 6   rom/android  network/wifi' ,
    'Host' : 'frodo.douban.com' ,
    'Connection' : 'Keep-Alive' ,
    'Accept-Encoding' : 'gzip' ,
}
import requests
response = requests.get(url,headers=headers,verify=False)
response.encoding = 'utf-8'
print(response.json())