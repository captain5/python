#!/usr/bin/env python3
__author__ = 'tcstory'
from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

'''
http://stackoverflow.com/questions/24928908/python3-type-str-doesnt-support-the-buffer-api
I'm trying to convert python2 to python3，i have an error : use this command "telnet localhost 5005 "to connect the program, but when i try to login, one problem was reported.
python3 Type str doesn't support the buffer API
telnet localhost 5005
'''


PORT=5005
NAME='TestChat'

class EndSession(Exception): pass

class CommandHandler:
    '''
    Simple command handler similar to cmd.Cmd from the standard library
    '''

    def unknown(self, session, cmd):
        'Respond to an unknown command'
        session.push('Unkonw command: {0}\r\n'.format(cmd).encode())

    def handle(self, session, line):
        'Handle a received line from a given session'
        if not line.strip():
            return
        #Split off the command
        parts = line.split(' ', 1)
        cmd = parts[0]
        try:
            line=parts[1].strip()
        except IndexError:
            line=''
        #Try to find a handler
        meth=getattr(self,'do_'+cmd,None)
        try:
            #Assume it's callable
            meth(session,line)
        except TypeError:
            #If it isn't ,respond to the unknown command
            self.unknown(session,cmd)

class Room(CommandHandler):
    '''
    A generic environment that may contain one or more users(sessions).it takes care of basic command handling and broadcasting.
    '''
    def __init__(self,server):
        self.server=server
        self.sessions=[]

    def add(self,session):
        'A session(user) has entered the room'
        self.sessions.append(session)

    def remove(self,session):
        'A session (user) has left the room'
        self.sessions.remove(session)

    def broadcast(self,line):
        'Send a line to all sessions in the room'
        for session in self.sessions:
            session.push(line.encode())

    def do_logout(self,session,line):
        'Respond to the logout command'
        raise EndSession

class LoginRoom(Room):
    '''
    A room meant for a single person who has just connected
    '''

    def add(self,session):
        Room.add(self,session)
        #When a user enters,greet him/her
        self.broadcast('Welcome to {0}\r\n'.format(self.server.name))

    def unknown(self, session, cmd):
        #All unknown commands (anything except login or logout)
        #results in a prodding
        session.push('Please log in\nUse "login <nick>"\r\n'.encode())

    def do_login(self,session,line):
        name=line.strip()
        #Make sure the user has entered a name
        if not name:
            session.push('Please enter a name\r\n'.encode())
        #Make sure that the name isn't in use
        elif name in self.server.users:
            session.push('The name {0} is taken.\r\n'.format(name).encode())
            session.push('Please try again.\r\n'.encode())
        else:
            #The name is OK,os it is stored in the session.and
            #the user is moved into the main room
            session.name=name
            session.enter(self.server.main_room)

class ChatRoom(Room):
    '''
    A room meant for multiple users who can chat with the others in the room
    '''

    def add(self,session):
        #Notify everyone that a new user has entered
        self.broadcast('{0} has entered the room.\r\n'.format(session.name))
        self.server.users[session.name]=session
        Room.add(self,session)

    def remove(self,session):
        Room.remove(self,session)
        #Notify everyone that a user has left
        self.broadcast('{0} has left the room.\r\n'.format(session.name))

    def do_say(self,session,line):
        self.broadcast('{0}: '+line+'\r\n'.format(session.name))

    def do_look(self,session,line):
        'Handles the look command,used to see who is in a room'
        session.push('The following are in this room:\r\n'.encode())
        for other in self.sessions:
            session.push('{0}\r\n'.format(other.name).encode())

    def do_who(self,session,line):
        'Handles the who command ,used to see who is logged in'
        session.push('The following are logged in:\r\n'.encode())
        for name in self.server.users:
            session.push('{0}\r\n'.format(name))

class LogoutRoom(Room):
    '''
    A simple room for a single user.Its sole purpose is to remove the user's name from the server
    '''

    def add(self,session):
        #When a session (user) enters the LogoutRoom it is deleted

        try:
            del self.server.users[session.name]
        except KeyError:
            pass

class ChatSession(async_chat):
    '''
    A single session,which takes care of the communication with a single user
    '''

    def __init__(self,server,sock):
        # async_chat.__init__(self,sock)
        super().__init__(sock)
        self.server=server
        self.set_terminator('\r\n')
        self.data=[]
        self.name=None
        #All sessions begin in a separate LoginRoom
        self.enter(LoginRoom(server))

    def enter(self,room):
        # Remove self from current room and add self to next room....
        try:
            cur=self.room
        except AttributeError:pass
        else:
            cur.remove(self)
        self.room=room
        room.add(self)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line=''.join(self.data)
        self.data=[]
        try:
            self.room.handle(self,line)
        except EndSession:
            self.handle_close()

    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))

class ChatServer(dispatcher):
    '''
    A chat server with a single room
    '''

    def __init__(self,port,name):
        super().__init__()
        # dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.name=name
        self.users={}
        self.main_room=ChatRoom(self)

    def handle_accept(self):
        conn,addr=self.accept()
        ChatSession(self,conn)

if __name__=='__main__':
    s=ChatServer(PORT,NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print()
