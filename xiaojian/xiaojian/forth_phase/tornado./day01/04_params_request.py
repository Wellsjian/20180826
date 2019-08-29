import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('<a href="/python">hello tornado</a>')
        # arg = self.get_argument('day')
        # self.write(arg)
        # arg1 = self.get_arguments('day')
        # print(arg)
        # print(arg1)
        self.write('<br>')
        # try:
        #     args1 = self.get_query_argument('day')
        #     args = self.get_query_arguments('day')
        # except Exception as e:
        #     args1=None
        #     print(e)
        args = self.get_query_argument('day', None)

        self.write('%s'%args)
        # print(args1)
        print(args)


    def post(self, *args, **kwargs):
        self.write('hello post')
        arg = self.get_body_argument('day', None)
        print(arg)
        args = self.get_body_arguments('day')
        print(args)

        headers = self.request.headers
        print(type(headers))
        ct = headers.get('Content-Type', None)
        my = headers.get('myheaders', None)
        you = headers.get('youheaders', None)
        print(ct, my, you)

class PythonHandler(RequestHandler):
    #重写方法, 获取动态设置URL中的参数
    def initialize(self, hello):
        self.hello = hello
    def get(self, *args, **kwargs):
        # with open('config') as obj:
        #     data = obj.read()
        self.write('<h1>'+self.hello+'</h1>')

    def post(self, *args, **kwargs):
        pass

# 定义一个变量  来代表端口号
define('port', type=int, default=8888, multiple=False)
# 解析文件 从指定文件中读取配置
parse_config_file('config')
# 创建application对象, 对服务器进行若干设置, 包括路由列表等

app = Application([('/', IndexHandler), ('/python', PythonHandler, {'hello':'您好'})])

# 创建服务端server程序
server = HTTPServer(app)

# 服务端监听段端口
server.listen(options.port)

# 启动服务程序 在当前进程中启动服务
IOLoop.current().start()