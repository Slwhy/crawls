#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy

import requests
from bs4 import BeautifulSoup
import os

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getPictUrl(picUrlList,html):
    soup = BeautifulSoup(html, "html.parser")
    try:
        img = soup.find('img')
        picUrlList.append(img.get('src'))
    except:
        print 'error'


def downPict(picUrlList):
    root = os.getcwd() + '/pic/'
    for i in range(len(picUrlList)):
        url = picUrlList[i]
        path = root + url.split('/')[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(url)
                with open(path,'wb') as f:
                    f.write(r.content)
                    #f.close
                    print '文件保存成功'
            else:
                print '文件已经存在'
        except:
            print '爬取失败'


def main():
    # http://desk.zol.com.cn/showpic/2880x1800_89000_112.html
    rootUrl = 'http://desk.zol.com.cn/showpic/2880x1800_89'
    picUrlList = []
    for i in range(100,200):
        url = rootUrl + str(i) + '_112.html'
        print url
        html = getHtmlText(url)
        getPictUrl(picUrlList,html)
    downPict(picUrlList)

main()







