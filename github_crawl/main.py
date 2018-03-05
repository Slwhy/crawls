#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy

from tools_my.crawls import Crawl
from bs4 import BeautifulSoup
from tools_my.mysql import Mysql_db

db = Mysql_db('root',1002,'github')

root_url = 'https://github.com'

class Github_crawl(Crawl):

    def __init__(self):
        self.name = ''
        self.href = ''
        self.star = ''
        self.author = ''
        self.explain = ''

    def get_repo_list(self,html):

        repo_list = html.find(class_="repo-list")
        return repo_list

    def analy_div1(self,div):
        h3 = div.h3
        a = h3.a
        href = a.get('href')
        name = href[1:]
        author = href.split('/')[1]
        p = div.p
        explain = p.get_text()
        href = root_url + href
        self.href = href
        self.explain = explain
        self.name = name
        self.author = author


    def analy_div2(self,div):
        pass

    def analy_div3(self,div):
        a = div.a
        star = a.get_text()
        self.star = star

    def write(self):
        sql = '''
            insert into python (name,author,star,href)
                                    values
                        (\'%s\',\'%s\',\'%s\',\'%s\')
        '''
        db.cur.execute(sql%(self.name,self.author,self.star,self.href))



if __name__ == '__main__':
    key = raw_input("please input what you want to crawling:")
    page = input("please input the number of page you want to crawling:")
    for num in range(1,page):
        url = 'https://github.com/search?p=' + str(num) + '&q=key&type=Repositories&utf8=%E2%9C%93'
        url = url.replace('key',key)
        github_crawl = Github_crawl()
        html = github_crawl.getText(url)
        soup = BeautifulSoup(html, 'html.parser')
        repo_list = github_crawl.get_repo_list(soup)
        for item in repo_list:

            try:

                github_crawl.analy_div1(item.find(class_="col-8 pr-3"))
                github_crawl.analy_div3(item.find(class_="col-2 text-right pt-1 pr-3 pt-2"))
                github_crawl.write()
            except TypeError:
                print TabError.message

        db.con.commit()