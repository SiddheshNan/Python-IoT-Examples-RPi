from tornado import websocket, web, ioloop
import json

cl = []

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("templates/index.html")

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_message(self, message):
        print (message)
        for c in cl:
            #message = json.dumps(message)
            c.write_message(message)

    def on_close(self):
        if self in cl:
            cl.remove(self)

class ApiHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        self.finish()
        id = self.get_argument("id")
        value = self.get_argument("value")
        data = {"id": id, "value" : value}
        data = json.dumps(data)
        for c in cl:
            c.write_message(data)

    @web.asynchronous
    def post(self):
        pass

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/api', ApiHandler),
    (r'/css/(.*)', web.StaticFileHandler, {'path': './static/css'}),
    (r'/js/(.*)', web.StaticFileHandler, {'path': './static/js'}),
    (r'/(favicon.ico)', web.StaticFileHandler, {'path': '../'}),
    (r'/(rest_api_example.png)', web.StaticFileHandler, {'path': './static'}),
    (r'/(css.css)', web.StaticFileHandler, {'path': './templates'})
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()