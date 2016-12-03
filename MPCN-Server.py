import tornado.ioloop
import tornado.web
import time

class InitialiseConnection(tornado.web.RequestHandler):
    def get(self):
        currentTime = time.time()
        hashedTime = hash(currentTime + random.random() + random.random())
        self.write(str(hashedTime))
        
        
def make_app():
    return tornado.web.Application([
        (r"/getNewSessionCode/", InitialiseConnection),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
