import tornado.ioloop
import tornado.httpserver
import tornado.websocket
import tornado.web
import time
import json
import random

PATH = "/home/pimania/MPCN"
clients = {}
sessions = {}

def generateId():
    return hash(time.time())

class WShandler(tornado.websocket.WebSocketHandler):
    def open(self):
        pass

    def on_message(self, argsJSON):
        args = json.loads(argsJSON)
        functionArg = args["function"]
        sessionIdArg = args["sessionId"]
        valueArg = args["value"]
        
        if functionArg == "createSession":
            id = generateId() #TODO
        elif function == "joinSession":

        elif function == "sendMessage":
            
        elif function == "placeTile":
            
    def on_close(self):
        if len(sessions["sessionId"]) == 2:
            del sessions["sessionId"][self]
            

def make_app():
    return tornado.web.Application([
        (r"/ws/", WShandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
