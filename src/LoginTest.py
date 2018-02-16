from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Login import Ui_login_dialog
from TimeTrack import Ui_Dialog
from NetworkCommunicationHandler import NetworkCommunicationHandler
import logging
from PyQt5.QtWidgets import QMessageBox
from _thread import *
import select
import socket
import sys
import signal
import pickle
import struct
import argparse
import requests
import json


SERVER_HOST = '127.0.0.1'
CHAT_SERVER_NAME = 'server'


def send(channel, *args):
    buffer = pickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L",value)
    channel.send(size)
    channel.send(buffer)

def receive(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except struct.error as e:
        return ''
    buf = ""
    while len(buf) < size:
        buf = channel.recv(size - len(buf))
        return pickle.loads(buf)[0]
    
    



class LoginCredential:
    username = ""
    password = ""

class LoginResponse:
    is_logged_in = False
    message = ""
    data = None


class Project:
    id=0
    name=""
    description=""
    
class ProjectTask:
    id = 0
    project_id = 0
    name = ""
    description = ""


class Login(QDialog):
    network_communication_handler = None
    
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        ui = Ui_login_dialog()
        ui.setupUi(self)
        self.login_button.clicked.connect(self.login_handler)
        self.cancel_button.clicked.connect(self.cancel_handler)
        #self.network_credentials = ('127.0.0.1',50000)
        #self.network_communication_handler = NetworkCommunicationHandler(self.network_credentials)
        
        #self.show_log()

    def send_to_server(self, serialized_process_data):
        try:
            host = '127.0.0.1'
            port = 50000
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((host,port))
            
            login_response = LoginResponse()
            send(server_socket, serialized_process_data)
            login_response = receive(server_socket)
            
            if login_response.is_logged_in:
                
                #data = login_response.data
                self.accept()
            else:
                self.reject()
                
        except(EOFError):
            pass
        
        
    def login_handler(self):
        login_credentials = LoginCredential()
        login_credentials.username = self.username_text.text()
        login_credentials.password = self.password_text.text()
        
        try:
            resp = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username':login_credentials.username, 'password':login_credentials.password})
            s = json.loads(resp.content)
            
            if s["token"] is not None:
                self.accept()
            else:
                QMessageBox.about(self, "Access Denied", "Incorrect Username or Password.")
                self.rejet()
            #QMessageBox.about(self, "Login Messagge", s["token"])
            
        except Exception as e:
            QMessageBox.show(self, "Error", e.args[1])
        
    def cancel_handler(self):
        self.reject()
        
    def show_log(self):
        for trace_message in self.network_communication_handler.trace_messages:
            logging.debug(trace_message)
    
        
class Window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        
        
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    login = Login()
    
    if login.exec_() == QDialog.Accepted:
        Dialog = QtWidgets.QDialog()
        
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        #main_dialog.load_projects()
        Dialog.show()        
        sys.exit(app.exec_())
    else:
        QMessageBox.warning('Error', 'Bad username or password')
        
        