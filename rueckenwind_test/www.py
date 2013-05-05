from rw.www import RequestHandler, get


class Main(RequestHandler):
    @get('/')
    def index(self):
        self.finish(template='index.html')


    @get('/error')
    def error(self):
        a = "123"
        raise Exception
