#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy
'''
  功能：  爬取笔趣阁网站的小说内容
'''


import requests
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        r = requests.get(url,timeout=20)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        print 'requests error'



if __name__ == '__main__':
    url = 'https://www.qu.la/book/3137/'          #笔趣阁元尊小说的网址
    #url = 'http://www.farpop.com/0_4/'
    html = getHtmlText(url)
    urlList = [ ]
    root_url = 'https://www.qu.la'
    html = getHtmlText(url)
    soup = BeautifulSoup(html,'html.parser')
    print  "***********目录*************"
    for i in soup.find_all('dd'):
        #print i                                 #打印整个标签
        try:
            a = i.a
            if a.get('style') == "":
                print '\t\t\t\t\t\t\t\t\t\t\t\t',
                print a.text
                url = root_url + a.get('href')
                urlList.append(url)
        except:
            print 'fail'
    num = raw_input('please input the num of chapter you want:')
    n = eval(num)
    if n >103:
        n = n-1
    html = getHtmlText(urlList[n-1])
    soup = BeautifulSoup(html,'html.parser')
    # print soup.text
    h = soup.h1
    print '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',
    print h.text
    content = soup.find(id = 'content')
    cont_str = content.text
    for i in content.children:
        if type(i) != type(content):
            print i