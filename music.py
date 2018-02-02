#coding=utf-8
from tornado import web,ioloop,httpserver
from model import models

class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        #self.write('我的音乐网站')
        self.render('index.html')

class QueryHandler(web.RequestHandler):
    def post(self, *args, **kwargs):
        query = self.get_argument('query')
        #查到的数据存入数据库
        music_info = 

application = web.Application([
    (r"/", MainPageHandler),
    (r"/query", QueryHandler),
])


if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8000)
    ioloop.IOLoop.current().start()
