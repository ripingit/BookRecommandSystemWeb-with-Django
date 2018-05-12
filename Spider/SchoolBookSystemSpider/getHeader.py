import requests
import re
file = open('C:\\Users\\Administrator\\Desktop\\pythonFile.txt','r+',encoding='utf-8')

def getHeaders():
    for line in file:
        m = re.match('(.*?):(.*?)\n',line)
        print('\''+m.group(1).strip()+'\'',':','\''+m.group(2).strip()+'\'',',')
def getCookie():
    m = re.findall('(\S*?)=(.*?);',file.read())
    for key,value in m:
        print('\''+key.strip()+'\'',':','\''+value.strip()+'\'',',')
if __name__ == "__main__":
    # getHeaders()
    getCookie()