#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy

import requests
import os
import json
from Crypto.Cipher import AES
import base64
import re
#
# data = {
#         'params':'VTR9VH3d/ourPcEVgzKHba+sLegQNw9bJiqltYz2T0NcJifrsrSlOh1BfqQt2wZsZo5okKVeluhBQ0TNhrQChbDoq9FfyJo6BvTkKVQN6e13ytcwo+9voHSQmhbDSn71zv9/v3axqK5p8PhajmA8+1/BKowmhlOP2Ohjcf4MYjnBRpbTcirXVwGf7k5ZaNIA',
#         'encSecKey':'cc6d7e14ac1408c39a7c172b70fb1005e199f298abfb5db75919d8b17e574c95ed400947e6e0213a3f4a03e3e568bb54841bafb736906d4d6fe118097afb413ec27ad514c41d92a6f6e2fe8d97febf600651726023071d62236445d2c5bc667888e30f03000f09fefd76f28613abd90f680603cfd7a624370c736b8805225b16'
#     }
#
#
head = {

        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

}
#
# # head['Cookie'] = 'JSESSIONID-WYYY=Jgi1ax6XAkd6cNwfV6qxBbhya5s4SW00PtEcYPNYUgdOeQO%5Cf%2FyFUQo%2FAVRlqDhDV8d7D%5CSGCtdu0NYgBxn9YdoZ0WuTb9VH0Nydug%2BZ4SUn74vDPG%2F%5CD6slP%2FmuljYfIVf%2F2X%5CxlrXuCvJjw8ER4amzfEPao6x5elWf%2B2OkzmGPJ%2Bvz%3A1515500969576; _iuqxldmzr_=32; _ntes_nnid=099805196f22bf7617cf11b5a67feeff,1515499169604; _ntes_nuid=099805196f22bf7617cf11b5a67feeff; __utma=94650624.1398381638.1515499170.1515499170.1515499170.1; __utmc=94650624; __utmz=94650624.1515499170.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=94650624.6.10.1515499170'


def createSecretKey(size):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(size))))[0:16]


def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(text.encode('hex'), 16)**int(pubKey, 16)%int(modulus, 16)
    return format(rs, 'x').zfill(256)


def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext

if __name__ == '__main__':

    url = 'http://music.163.com/weapi/v1/resource/comments/A_PL_0_2015321897?csrf_token='
    # url = 'http://music.163.com/weapi/v1/resource/comments/A_PL_0_973757368?csrf_token='
    s = requests.session()
    # text = {
    #     'username': username,
    #     'password': password,
    #     'rememberLogin': 'true'
    # }
    modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    nonce = '0CoJUm6Qyw8W8jud'
    pubKey = '010001'
    text = {"rid":"A_PL_0_430509126","offset":"60","total":"false","limit":"20","csrf_token":""}
    text = json.dumps(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)

    data = {
        'params': encText,
        'encSecKey': encSecKey
    }

    r = s.post(url,data=data,headers = head)
    conte = r.text

    # re1 = re.compile('"content":"."')
    # print re1.findall(r.text)
    conte = json.loads(conte)
    comment = conte['comments']
    for i in comment:
        print json.dumps(i,encoding='utf-8',ensure_ascii=False)


