# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimeTrack.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from threading import Timer
import time 
from PyQt5.QtWidgets import QMessageBox
from PIL import ImageGrab
from PyQt5.Qt import QListWidgetItem, QDialog
from DBHelper import DBHelper
import datetime
import socket, select
import pickle
#import codecs
import io
from io import StringIO
from ProcessData import ProcessData
from GeneralDTO import GeneralDTO
from LoginData import LoginData
import json
import jwt
import requests
import base64
# Model class to send image data to the server
class ProcessScreen:
    process_id = 0
    image_data = bytearray()


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        #self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
        

class Ui_Dialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(542, 520)
        self.lblTrackTime = QtWidgets.QLabel(self)
        self.lblTrackTime.setGeometry(QtCore.QRect(260, 20, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(55)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lblTrackTime.setFont(font)
        self.lblTrackTime.setObjectName("lblTrackTime")
        self.btnStartTimer = QtWidgets.QPushButton(self)
        self.btnStartTimer.setGeometry(QtCore.QRect(370, 490, 75, 23))
        self.btnStartTimer.setObjectName("btnStartTimer")
        self.btnStopTimer = QtWidgets.QPushButton(self)
        self.btnStopTimer.setGeometry(QtCore.QRect(450, 490, 75, 23))
        self.btnStopTimer.setObjectName("btnStopTimer")
        self.project_list = QtWidgets.QListWidget(self)
        self.project_list.setGeometry(QtCore.QRect(10, 30, 171, 451))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.project_list.setFont(font)
        self.project_list.setObjectName("project_list")
        self.task_list = QtWidgets.QListWidget(self)
        self.task_list.setGeometry(QtCore.QRect(190, 120, 331, 361))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.task_list.setFont(font)
        self.task_list.setObjectName("task_list")
        self.current_time = ""        
        
        self.repeatedTimer = RepeatedTimer(1, self.time_handler)
        self.btnStartTimer.clicked.connect(self.btnStartTimer_clicked)
        self.btnStopTimer.clicked.connect(self.btnStopTimer_clicked)
        
        #self.project_list.itemClicked().connect(self.project_list_item_clicked)
        self.project_list.currentItemChanged.connect(self.project_list_item_clicked)
        self.task_list.currentItemChanged.connect(self.task_list_item_clicked)
        
        self.startTime = 0
        self.endTime = time.time()
        self.timeElapsedInSeconds = 0
        self.timeElapsedInMinutes = 0
        self.timeElapsedInHours = 0
        self.isStarted = False
        self.isStopped = False
        self.screen_shots = 0
        self.image_data_string = ""

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        DBHelper.initialize_helper(DBHelper)
        self.current_week()

    def btnStartTimer_clicked(self):
        #self.create_process()
        self.create_process()
        self.repeatedTimer.start()
        
    def btnStopTimer_clicked(self):
        self.repeatedTimer.stop()
        self.stop_process()
    
    def show_exception(self, ex):
        err_msg = QMessageBox()
        err_msg.setIcon(QMessageBox.Critical)
        err_msg.setText(str(ex.args[0]))
        err_msg.show()            

    def prepare_data_to_send(self):
        try:
            current_calendar_week_id = 1
            
            process_data = ProcessData()
            process_data.process_id = self.current_process.id
            process_data.project_id = self.current_selected_project.id
            process_data.task_id = self.current_selected_task.id
            process_data.weekend_id = current_calendar_week_id
            process_data.user_id = 1
            process_data.start_time = self.current_process.start_time
            process_data.end_time = self.current_process.end_time
            #process_data.image_data = self.image_data
            
            return process_data
        except Exception as ex:
            self.show_exception(ex)
                

    
    def create_process(self):
        try:
            self.isStarted = True
            selected_project_id = self.current_selected_project.id
            selected_task_id = self.current_selected_task.id
            current_process_start_time = time.time()
            current_process_current_time = self.current_time
            current_process_end_time = 0
            
            self.current_process_data = DBHelper.create_process_without_orm(DBHelper,
                                            selected_task_id, 
                                            selected_project_id, 
                                            current_process_start_time, 
                                            current_process_end_time, 
                                            current_process_current_time,
                                            1
                                            )
            
            self.capture_current_Screen_test()
            
#             current_calendar_week_id = DBHelper.current_calendar_week.id
#             
            
#            process_data.process_id = self.current_process.id
#            process_data.project_id = self.current_selected_project.id
#             process_data.task_id = self.current_selected_task.id
#             process_data.weekend_id = current_calendar_week_id
#             process_data.user_id = 1
#             process_data.start_time = self.current_process.start_time
#             process_data.end_time = self.current_process.end_time
            self.current_process_data.image_data = self.image_data_string
            
            #general_dto = { "process_data" : self.current_process_data }
            #prepared_process_data = self.prepare_data_to_send()
#           

            serialized_data = json.dumps(self.current_process_data.__dict__)
            
            general_dto = {"process_data":serialized_data}
            
            
            self.send_to_server_rest(general_dto, 'http://127.0.0.1:8000/process_data/')
            #self.send_to_server(serialized_data)
            
        except Exception as ex:
            self.show_exception(ex)
         
         
    def update_process(self):
        try:
            self.current_process_data.duration = self.current_time
            self.current_process_data = DBHelper.update_process_without_orm(DBHelper, self.current_process_data)
            
            self.capture_current_Screen()
            
#             current_calendar_week_id = DBHelper.current_calendar_week.id
#             
            #process_data = ProcessData()
#             process_data.process_id = self.current_process.id
            #process_data.project_id = self.current_selected_project.id
#             process_data.task_id = self.current_selected_task.id
#             process_data.weekend_id = current_calendar_week_id
#             process_data.user_id = 1
#             process_data.start_time = self.current_process.start_time
#             process_data.end_time = self.current_process.end_time
            self.current_process_data.image_data = self.image_data
# 
            general_dto = { "process_data" : self.current_process_data }
            #prepared_process_data = self.prepare_data_to_send()
#           
            serialized_data = json.dumps(general_dto)

#             serialized_data = pickle.dumps(process_data)
            #prepared_process_data = self.prepare_data_to_send()
            #serialized_data = pickle.dumps(self.current_process_data)
            self.send_to_server_rest(serialized_data, 'http://127.0.0.1:8000/process_data/')
            #self.send_to_server(serialized_data)
            

            
        except Exception as ex:
            self.show_exception(ex)
         
    def stop_process(self):
        try:
            self.current_process_data.duration = self.current_time
            self.current_process_data.end_time = time.time()
            self.current_process_data = DBHelper.stop_process_without_orm(DBHelper, self.current_process_data)
        except Exception as ex:
            self.show_exception(ex)

    def load_projects(self):
        try:
            DBHelper.fetch_projects(DBHelper)
            projects = DBHelper.projects
            
            for project in projects:
                current_project_item = QListWidgetItem()
                current_project_item.setText(project.project_name)
                current_project_item.setData(QtCore.Qt.UserRole, project)
                self.project_list.addItem(current_project_item)
            
            self.load_tasks_for_selected_project(DBHelper.projects[0].id)
        except Exception as ex:
            self.show_exception(ex)


    def load_tasks(self):
        try:
            DBHelper.fetch_tasks(DBHelper)
            tasks = DBHelper.tasks
            
            for task in tasks:
                self.task_list.addItem(task.task_description)
        except Exception as ex:
            self.show_exception(ex)
    
    @pyqtSlot()
    def project_list_item_clicked(self):
        try:
            current_selected_project_item = self.project_list.currentItem()
            self.current_selected_project = current_selected_project_item.data(QtCore.Qt.UserRole) 
            self.load_tasks_for_selected_project(self.current_selected_project.id)
            
        except Exception as ex:
            self.show_exception(ex)
            
    @pyqtSlot()
    def task_list_item_clicked(self):
        try:
            current_selected_task_item = self.task_list.currentItem()
            self.current_selected_task = current_selected_task_item.data(QtCore.Qt.UserRole) 
            
        except Exception as ex:
            self.show_exception(ex)
    
    
    def load_tasks_for_selected_project(self, pid):
        try:
            DBHelper.fetch_tasks_by_project(DBHelper,pid) 
            tasks = DBHelper.tasks
            
            self.task_list.clear()
            
            for task in tasks:
                current_task = QListWidgetItem()
                current_task.setText(task.task_description)
                current_task.setData(QtCore.Qt.UserRole, task)
                self.task_list.addItem(current_task)
        except Exception as ex:
            self.show_exception(ex)
    



    #connections
    def capture_current_Screen_test(self):
        try:
            self.screen_shots += 1
            ts = time.time()
            file_name = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H %M %S')            
            self.current_image_name = file_name
            
            self.image_data = io.BytesIO()
            
            im = ImageGrab.grab()
            im.save(self.image_data,format="JPEG")
            im.close()
            self.image_data_string = base64.b64encode(self.image_data.getvalue())
            
             
        except Exception as ex:
            self.show_exception(ex)

    
    #connections
    def capture_current_Screen(self):
        try:
            self.screen_shots += 1
            ts = time.time()
            file_name = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H %M %S')            
            self.current_image_name = file_name
            
            self.image_data = io.BytesIO()
            
            ImageGrab.grab().save(self.image_data, 'JPEG')
             
        except Exception as ex:
            self.show_exception(ex)

    def send_to_server_rest(self, data_to_send, server_url):
        try:
            resp = requests.post(server_url, data=data_to_send)
            QMessageBox.Abort(self,resp.content)
        except Exception as e:
            QMessageBox.about(self, e.args[0])
    
    def create_process_test(self):
        self.send_to_server_rest({'username':'Dharmindar'}, 'http://127.0.0.1:8000/process_data/')        
        
    def update_process_test(self):
        self.send_to_server_rest({'username':'Dharmindar'}, 'http://127.0.0.1:8000/process_data/')        

    
    def perform_response_action(self, response_data):
        
        if response_data.has_key("login"):
            login_data = LoginData()
            login_data = response_data["Login"]
            
            if login_data.logged_in:
                pass
            


    def send_to_server(self, serialized_process_data):
        try:
            host = '127.0.0.1'
            port = 50000
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((host,port))
            server_socket.sendall(serialized_process_data)
            server_socket.close()
        except Exception as e:
            self.show_exception(e)

    #Function that increments the timer
    def time_handler(self):
        try:
            self.startTime += 1
            self.timeElapsedInSeconds = self.startTime - (self.timeElapsedInMinutes * 60) - (self.timeElapsedInHours * 60 * 60 )
            current_week_day = datetime.datetime.today().weekday()
            
            today_is_sunday = False if current_week_day < 6 else True
                
            if self.timeElapsedInSeconds >= 60:
                self.timeElapsedInMinutes += 1
                self.timeElapsedInSeconds = 0
                self.update_process()
                #self.update_process_test()
                #self.capture_current_Screen()
                
            if self.timeElapsedInMinutes >= 60:
                self.timeElapsedInHours += 1
                self.timeElapsedInMinutes = 0
                
                if today_is_sunday == True:
                    if self.sunday_hours < 24:
                        self.sunday_hours += 1
                    else:                              
                        self.btnStopTimer_clicked()
                        self.btnStartTimer_clicked()
                        self.sunday_hours = 0
                    
            self.current_time = self.timeElapsedInHours.__str__() + " : " + self.timeElapsedInMinutes.__str__() + " : " + self.timeElapsedInSeconds.__str__()
            self.lblTrackTime.setText(self.current_time)
            
        except Exception as ex:
            self.show_exception(ex)

    def current_week(self):
        date_today = datetime.date.today()
        try:
            DBHelper.current_week(DBHelper, date_today)
        except Exception as ex:
            self.show_exception(ex)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblTrackTime.setText(_translate("Dialog", "02:55:45"))
        self.btnStartTimer.setText(_translate("Dialog", "Start Timer"))
        self.btnStopTimer.setText(_translate("Dialog", "Stop Timer"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    #ui.setupUi()
    ui.load_projects()
    ui.show()
    sys.exit(app.exec_())