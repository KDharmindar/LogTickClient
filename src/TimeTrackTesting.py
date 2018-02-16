# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimeTrackTesting.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.Qt import QDialog



class TitleBar(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        css = """
        QWidget{
            Background: #403F3A;
            color:white;
            font:12px bold;
            font-weight:bold;
            border-radius: 1px;
            height: 11px;
        }
        QDialog{
            Background-image:url('img/titlebar bg.png');
            font-size:12px;
            color: black;

        }
        QToolButton{
            Background:#403F3A;
            font-size:11px;
        }
        QToolButton:hover{
            Background: #45494A;
            font-size:11px;
        }
        """
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css)
        self.minimize=QtWidgets.QToolButton(self)
        self.minimize.setIcon(QtGui.QIcon('img/min.png'))
        self.maximize=QtWidgets.QToolButton(self)
        self.maximize.setIcon(QtGui.QIcon('img/max.png'))
        close=QtWidgets.QToolButton(self)
        close.setIcon(QtGui.QIcon('img/close.png'))
        self.minimize.setMinimumHeight(10)
        close.setMinimumHeight(10)
        self.maximize.setMinimumHeight(10)
        label=QtWidgets.QLabel(self)
        label.setText("Window Title")
        self.setWindowTitle("Window Title")
        hbox=QtWidgets.QHBoxLayout(self)
        hbox.addWidget(label)
        hbox.addWidget(self.minimize)
        hbox.addWidget(self.maximize)
        hbox.addWidget(close)
        hbox.insertStretch(1,500)
        hbox.setSpacing(0)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Fixed)
        self.maxNormal=False
        close.clicked.connect(self.close)
        self.minimize.clicked.connect(self.showSmall)
        self.maximize.clicked.connect(self.showMaxRestore)

    def showSmall(self):
        box.showMinimized()

    def showMaxRestore(self):
        if(self.maxNormal):
            box.showNormal()
            self.maxNormal= False
            self.maximize.setIcon(QtGui.QIcon('img/max.png'))
            print('1')
        else:
            box.showMaximized()
            self.maxNormal=  True
            print('2')
            self.maximize.setIcon(QtGui.QIcon('img/max2.png'))

    def close(self):
        box.close()

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            box.moving = True
            box.offset = event.pos()

    def mouseMoveEvent(self,event):
        if box.moving: box.move(event.globalPos()-box.offset)

class Frame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.m_mouse_down= False
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        css = """
        QFrame{
            Background:  #403F3A;
            color:white;
            font:13px ;
            font-weight:bold;
            }
        """
        self.setStyleSheet(css)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.m_titleBar= TitleBar()
        self.m_content= QtWidgets.QWidget(self)
        vbox=QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.m_titleBar)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        layout=QtWidgets.QVBoxLayout()
        layout.addWidget(self.m_content)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(0)
        vbox.addLayout(layout)
        # Allows you to access the content area of the frame
        # where widgets and layouts can be added

    def contentWidget(self):
        return self.m_content

    def titleBar(self):
        return self.m_titleBar

    def mousePressEvent(self,event):
        self.m_old_pos = event.pos()
        self.m_mouse_down = event.button()== Qt.LeftButton

    def mouseMoveEvent(self,event):
        x=event.x()
        y=event.y()

    def mouseReleaseEvent(self,event):
        m_mouse_down=False



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 520)
        #Dialog.setWindowOpacity(1.0)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.lblTrackTime = QtWidgets.QLabel(Dialog)
        self.lblTrackTime.setGeometry(QtCore.QRect(220, 10, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Digital-7 Italic")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblTrackTime.setFont(font)
        self.lblTrackTime.setStyleSheet("color: rgb(129, 123, 113);\n"
"font: italic 72pt \"Digital-7 Italic\";")
        self.lblTrackTime.setObjectName("lblTrackTime")
        self.btnStartTimer = QtWidgets.QPushButton(Dialog)
        self.btnStartTimer.setGeometry(QtCore.QRect(340, 440, 91, 71))
        self.btnStartTimer.setStyleSheet("background-color: rgb(52, 58, 64);\n"
"border: 0px solid #CFDDEA;\n"
"border-radius: 10px;")
        self.btnStartTimer.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Users/Dharmindar-PC/Desktop/font/start-colored.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../../../../../Users/Dharmindar-PC/Desktop/font/start-colored.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnStartTimer.setIcon(icon)
        self.btnStartTimer.setIconSize(QtCore.QSize(70, 70))
        self.btnStartTimer.setObjectName("btnStartTimer")
        self.btnStopTimer = QtWidgets.QPushButton(Dialog)
        self.btnStopTimer.setGeometry(QtCore.QRect(440, 440, 81, 71))
        self.btnStopTimer.setStyleSheet("background-color: rgb(52, 58, 64);\n"
"border: 0px solid #CFDDEA;\n"
"border-radius: 10px;")
        self.btnStopTimer.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../Users/Dharmindar-PC/Desktop/font/pause-colored.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../../../../../Users/Dharmindar-PC/Desktop/font/pause-colored.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnStopTimer.setIcon(icon1)
        self.btnStopTimer.setIconSize(QtCore.QSize(70, 70))
        self.btnStopTimer.setObjectName("btnStopTimer")
        self.task_list = QtWidgets.QListWidget(Dialog)
        self.task_list.setGeometry(QtCore.QRect(210, 100, 321, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.task_list.setFont(font)
        self.task_list.setStyleSheet("background-color: rgb(69, 73, 74);\n"
"alternate-background-color: rgb(191, 255, 191);\n"
"border: 0px solid #CFDDEA;\n"
"border-radius: 10px;")
        self.task_list.setFrameShape(QtWidgets.QFrame.Panel)
        self.task_list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.task_list.setLineWidth(0)
        self.task_list.setObjectName("task_list")
        self.project_list = QtWidgets.QListWidget(Dialog)
        self.project_list.setGeometry(QtCore.QRect(10, 100, 191, 321))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.project_list.setFont(font)
        self.project_list.setStyleSheet("background-color: rgb(69, 73, 74);\n"
"alternate-background-color: rgb(191, 255, 191);\n"
"border: 0px solid #CFDDEA;\n"
"border-radius: 10px;")
        self.project_list.setFrameShape(QtWidgets.QFrame.Panel)
        self.project_list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.project_list.setLineWidth(1)
        self.project_list.setAlternatingRowColors(True)
        self.project_list.setObjectName("project_list")

        self.retranslateUi(Dialog)
        self.project_list.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LogTick"))
        self.lblTrackTime.setText(_translate("Dialog", "02:55:45"))
    






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #Dialog = QtWidgets.QDialog()
    Dialog = TitleBar()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    
    
    box = Frame()
    box.move(60,60)
    l = QtWidgets.QVBoxLayout(box.contentWidget())
    l.setContentsMargins(0, 0, 0, 0)
    l.addWidget(Dialog)
    box.show()
    #Dialog.show()
    sys.exit(app.exec_())

