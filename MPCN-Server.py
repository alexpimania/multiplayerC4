import tornado.ioloop
import tornado.httpserver
import tornado.websocket
import tornado.web
import time
import json
import random

PATH = "/home/pimania/MPCN"
clients = {}

def getClientInfo(client):
    clientSessionSize = 0
    clientSessionId = clients[client]["sessionId"]
    clientsInSession = []
    
    for searchClient in clients:
        if clients[searchClient]["sessionId"] == clientSessionId:
            clientSessionSize += 1
            clientsInSession.append(searchClient)
            
    return [clientSessionSize, clientSessionId, clientsInSession]

def deleteUser(client):
    clientSessionId, clientSessionSize, clientsInSession = getClientInfo(client)
    
    for client in clientsInSession:
        client.write_message("
        del clients[client]
    
    
class WShandler(tornado.websocket.WebSocketHandler):
    def open(self):
        pass

    def on_message(self, argsJSON):
        args = json.loads(argsJSON)
        functionArg = args["function"]
        sessionIdArg = args["sessionId"]
        valueArg = args["value"]
        
        if functionArg == "createSession":
            id = generateId() 
        elif function == "joinSession":
            
        elif function == "sendMessage":
            
        elif function == "placeTile":
            
    def on_close(self):
        deleteUser(self)
            
            

def make_app():
    return tornado.web.Application([
        (r"/ws/", WShandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
