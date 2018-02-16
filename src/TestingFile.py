#########################################################
## customize Title bar
## dotpy.ir
## iraj.jelo@gmail.com
#########################################################
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import os

path = os.path.dirname(os.path.abspath(__file__)) 

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
            border-bottom: 1px solid #45494A;
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
        close.setIcon(QtGui.QIcon(os.path.join(path,'images/close_button.jpg')))
        self.minimize.setMinimumHeight(10)
        close.setMinimumHeight(10)
        self.maximize.setMinimumHeight(10)
        label=QtWidgets.QLabel(self)
        label.setText("LogTick")
        self.setWindowTitle("LogTick")
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
        self.m_titleBar= TitleBar(self)
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









if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    box = Frame()
    box.setGeometry(QtCore.QRect(0, 0, 541, 521))
    

    
    task_list = QtWidgets.QListWidget(box)
    task_list.setGeometry(QtCore.QRect(210, 100, 321, 321))
    font = QtGui.QFont()
    font.setPointSize(12)
    task_list.setFont(font)
    task_list.setStyleSheet("background-color: rgb(69, 73, 74);\n"
                            "alternate-background-color: rgb(191, 255, 191);\n"
                            "border: 0px solid #CFDDEA;\n"
                            "border-radius: 10px;")
    task_list.setFrameShape(QtWidgets.QFrame.Panel)
    task_list.setFrameShadow(QtWidgets.QFrame.Sunken)
    task_list.setLineWidth(0)
    task_list.setObjectName("task_list")    
    
    
    lblTrackTime = QtWidgets.QLabel(box)
    lblTrackTime.setGeometry(QtCore.QRect(220, 10, 301, 81))
    lblTrackTime.setText("10:25:55")
    font = QtGui.QFont()
    font.setFamily("Digital-7 Italic")
    font.setPointSize(72)
    font.setBold(False)
    font.setItalic(True)    
    font.setWeight(50)
    lblTrackTime.setFont(font)
    lblTrackTime.setStyleSheet("color: rgb(129, 123, 113);\n"
                               "font: italic 72pt \"Digital-7 Italic\";")
    lblTrackTime.setObjectName("lblTrackTime")
    btnStopTimer = QtWidgets.QPushButton(box)
    btnStopTimer.setGeometry(QtCore.QRect(440, 440, 81, 71))
    btnStopTimer.setStyleSheet("background-color: rgb(52, 58, 64);\n"
                               "border: 0px solid #CFDDEA;\n"
                               "border-radius: 10px;")
    btnStopTimer.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(os.path.join(path,"images/stop_button.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon.addPixmap(QtGui.QPixmap(os.path.join(path,"images/stop_button.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
    btnStopTimer.setIcon(icon)
    btnStopTimer.setIconSize(QtCore.QSize(70, 70))
    btnStopTimer.setObjectName("btnStopTimer")
    project_list = QtWidgets.QListWidget(box)
    project_list.setGeometry(QtCore.QRect(10, 100, 191, 321))
    font = QtGui.QFont()
    font.setPointSize(13)
    project_list.setFont(font)
    project_list.setStyleSheet("background-color: rgb(69, 73, 74);\n"
                               "alternate-background-color: rgb(191, 255, 191);\n"
                               "border: 0px solid #CFDDEA;\n"
                               "border-radius: 10px;")
    project_list.setFrameShape(QtWidgets.QFrame.Panel)
    project_list.setFrameShadow(QtWidgets.QFrame.Sunken)
    project_list.setLineWidth(1)
    project_list.setAlternatingRowColors(True)
    project_list.setObjectName("project_list")
    btnStartTimer = QtWidgets.QPushButton(box)
    btnStartTimer.setGeometry(QtCore.QRect(340, 440, 91, 71))
    btnStartTimer.setStyleSheet("background-color: rgb(52, 58, 64);\n"
                                "border: 0px solid #CFDDEA;\n"
                                "border-radius: 10px;")
    btnStartTimer.setText("")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(os.path.join(path,"images/start_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon1.addPixmap(QtGui.QPixmap(os.path.join(path,"images/start_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
    btnStartTimer.setIcon(icon1)
    btnStartTimer.setIconSize(QtCore.QSize(70, 70))
    btnStartTimer.setObjectName("btnStartTimer")

    
    box.move(60,60)
    
    l=QtWidgets.QVBoxLayout(box.contentWidget())
    l.setContentsMargins(0, 0, 0, 0)
    edit=QtWidgets.QLabel("""I would've did anything for you to show you how much I adored you
But it's over now, it's too late to save our loveJust promise me you'll think of me
Every time you look up in the sky and see a star 'cuz I'm  your star.""")
    #l.addWidget(edit)
    
    
    
    box.show()
    app.exec_()