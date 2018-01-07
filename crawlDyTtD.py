#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy


import requests
from bs4 import BeautifulSoup
import os
import json
import codecs
import cPickle as pickle        #可将内存中的数据序列化为字符串，写入磁盘



def getHtmlText(url):
    try:
        r = requests.get(url,timeout=20)
        r.encoding = r.apparent_encoding
        #print r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        print 'requests error'

def getMovieUrlList(html,dict1):
    count = 0
    soup = BeautifulSoup(html,'html.parser')
    for ul in soup.find_all('ul'):
        for a in ul.find_all('a'):
            url = 'http://www.dytt8.net/'
            url = url + str(a.get('href'))
            html = getHtmlText(url)
            soup = BeautifulSoup(html,'html.parser')
            print soup.find(style="WORD-WRAP: break-word")
            # name = a.get_text()
            # dict1[name] = url
            # count = count + 1
            #dictInfor = json.dumps(dict1, encoding="UTF-8", ensure_ascii=False)
    print count



def writeMovieHtmlUrl(dict1):
    count = 1
    f = codecs.open('C:\Users\zjp\Desktop\shaoli\scarpy\movie.txt', 'wb', 'utf-8')
    for key in dict1:
        #print  key
        f.write(unicode(count) +u'\t' + key + u'\t\t\t\t\t' + dict1[key] + u"\r\n")
        count = count + 1
    f.close()

if __name__ == '__main__':
    #'http://www.dytt8.net/html/gndy/jddy/20171113/55535.html'
    #'/html/gndy/jddy/20171113/55535.html'
    url = 'http://www.dytt8.net/'
    dict1 = {}
    html = getHtmlText(url)
    getMovieUrlList(html,dict1)
    #writeMovieHtmlUrl(dict1)



