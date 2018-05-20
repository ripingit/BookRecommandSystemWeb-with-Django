import requests
url = 'https://icanhazip.com/'
protey = {
    'https':'119.28.152.208:80'
}
response = requests.get(url=url,proxies=protey)
print(response.text)