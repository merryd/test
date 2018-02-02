#coding=utf-8

'''
Title=实现模拟发送知乎私信
Date=2018-01-26
'''
import requests
import time
import random

class SendData:
    def __init__(self):
        self.url = 'https://www.zhihu.com/api/v4/messages'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        self.cookie = {'Cookie':''}

    def Send(self,dat):
        self.html = requests.post(self.url,json=dat,cookies=self.cookie,headers=self.header)
        print(self.html.json())

if __name__ == '__main__':
    send = SendData() #实例化
    with open(r'D:\1.txt') as f:  #打开文件
        for hash in f:
            time.sleep(random.randint(15,30)) #随机等待15到30秒
            hash = hash.strip('\n') #去掉换行
            dat = {'type': "common", 'content': "666", 'receiver_hash': hash}
            send.Send(dat)
