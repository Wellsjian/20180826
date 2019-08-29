import tornado
# from setuptools.command.setopt import config_file
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, url, RequestHandler


#创建Application对象, 配置路由列表和视图处理函数
class PythonHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.write('hello python')
        self.write('<br>')
        day = kwargs.get('day', '')
        title = kwargs.get('title', '')
        if day:
            self.write('第几天: '+day)
        if title:
            self.write('<br>')
            self.write('讲解课程: '+title)

    def post(self, *args, **kwargs):
        pass

app = Application([url("/python", PythonHandler),
                   url('/python/(?P<day>[a-zA-Z0-9]+)', PythonHandler),
                   url('/python/(?P<day>[a-zA-Z0-9]+)/(?P<title>[a-zA-Z]+)', PythonHandler),
                    ])

#定义变量
define('port', type=int, default=8888, multiple=False)

#解析文件
parse_config_file('config')
#创建服务端server程序
server = HTTPServer(app)

#服务器监听端口
server.listen(options.port)

#启动服务程序
IOLoop.current().start()
