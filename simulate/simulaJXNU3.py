# /usr/bin/python
# encoding:utf-8
# __Author__ = Slwhy

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    name = raw_input('please input your id:')
    pwd = raw_input('please input your password:')

    headers = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',

        'rblUserType': 'Student',
        'ddlCollege': '180     ',
        'StuNum': name,  # 加上自己的学号
        'TeaNum': ' ',
        'Password': pwd,  # 自己的密码
        'login': '登录'
    }

    s = requests.session()  #创建一个会话
    url = 'http://jwc.jxnu.edu.cn/'
    login_url = 'http://jwc.jxnu.edu.cn/Default_Login.aspx?preurl='
    r = s.get(login_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    VIEWSTATE = soup.find(id='__VIEWSTATE')
    VIEWSTATE_dict = {
        '__VIEWSTATE': VIEWSTATE.get('value')
    }
    EVENTVALIDATION = soup.find(id='__EVENTVALIDATION')
    EVENTVALIDATION_dict = {
        '__EVENTVALIDATION': EVENTVALIDATION.get('value')
    }
    data = dict(headers.items() + EVENTVALIDATION_dict.items() + VIEWSTATE_dict.items())

    r = s.post(login_url, data=data)
    head_respon = r.headers
    # print r.text
    print "Login: " + str(r.status_code)
    print data
    r = s.get('http://jwc.jxnu.edu.cn/User/Default.aspx')
    print r.text
    print r.status_code




