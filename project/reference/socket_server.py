__author__ = 'wwxiang'
 
 
import socket
import os
REtype = ('image/jpg','text/html')
work = os.getcwd()
'''
    注明：暂时还只支持本地文件的响应，没有添加对网络地址的响应，如某个网站上的js文件，或者其他网络的处理
    http://www.cnblogs.com/vamei/archive/2012/10/31/2747885.html  
    discuss     
'''
#用于描述服务端
class PYTHONSERVER:
    def __init__(self,HOST='',PORT = 8085):
        self.so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.so.bind((HOST,PORT))
        while True:
            self.so.listen(3)
            self.conn,addr = self.so.accept()
            request = self.conn.recv(1024).decode()
            self.analysisClientRequest(request)
        pass
    def analysisClientRequest(self,request):
        request = request.split('\r\n',1)
        # 处理request
        # 分解出method请求方法类型，url请求地址，type请求协议类型
        method = request[0].split(' ')
        aother = request[1].split('\r\n')
        self.__method = method[0]
        self.__url = method[1]
        self.__type = method[2]
        clientSend = aother.pop()
        # 装载从客户端发送过来的头部，并且转换为一个dic，headers
        headers = '{'
        for node in aother:
            if not len(node):
                continue
            node = node.split(':')
            headers += '\''+node[0]+'\':\''+node[1]+'\','
        headers = headers[:-1]
        headers += '}'
        self.__headers = eval(headers)
        if len(clientSend):
            self.__data = clientSend
        self.handler()
        pass
    def sendServerResponse(self,add):
        #处理url请求的具体类型，并发送数据
        typehead = self.__headers['Accept'].split(',')[0]
        typehead = typehead.strip()
        sendHead = ['HTTP/1.x 200 OK']
        for HEAD in REtype:
            if typehead == HEAD:
                sendHead.append('Content-Type:'+HEAD)
        sendHead.append('\r\n\n')
        try:
            with open(add,'rb') as fs:
                reply = fs.read()
        except:
            sendHead[0] = 'HTTP/1.x 200 Not Find'
            reply = '<html><head></head><body><h1>Not Find</h1></body></html>'.encode(encoding='utf-8')
            pass
        sendHead = ' \n'.join([he for he in sendHead])
        self.conn.sendall(sendHead.encode(encoding='utf-8') + reply)
        pass
    def handler(self):
        # 根据请求的方法类型，进行分别处理
        if self.__method == 'GET':
            if not self.__url == '/favicon.ico':
                add = work + self.__url
                self.sendServerResponse(add)
            pass
        elif self.__method == 'POST':
            if not self.__url == '/favicon.ico':
                print(self.__data)
                add = work + self.__url
                self.sendServerResponse(add)
            pass
    pass
http = PYTHONSERVER()
