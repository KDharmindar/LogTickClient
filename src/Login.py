# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from TimeTrack import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from myMainWindow import Ui_myMainWindow
from PyQt5.Qt import QWidget, QDialog

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(351, 117)
        login_dialog.username_text = QtWidgets.QLineEdit(login_dialog)
        login_dialog.username_text.setGeometry(QtCore.QRect(90, 20, 251, 20))
        login_dialog.username_text.setObjectName("username_text")
        login_dialog.password_text = QtWidgets.QLineEdit(login_dialog)
        login_dialog.password_text.setGeometry(QtCore.QRect(90, 50, 251, 20))
        login_dialog.password_text.setObjectName("password_text")
        login_dialog.username_label = QtWidgets.QLabel(login_dialog)
        login_dialog.username_label.setGeometry(QtCore.QRect(30, 20, 50, 12))
        login_dialog.username_label.setObjectName("username_label")
        login_dialog.password_label = QtWidgets.QLabel(login_dialog)
        login_dialog.password_label.setGeometry(QtCore.QRect(30, 50, 50, 12))
        login_dialog.password_label.setObjectName("password_label")
        login_dialog.login_button = QtWidgets.QPushButton(login_dialog)
        login_dialog.login_button.setGeometry(QtCore.QRect(180, 80, 75, 23))        
        login_dialog.login_button.setObjectName("login_button")
        login_dialog.cancel_button = QtWidgets.QPushButton(login_dialog)
        login_dialog.cancel_button.setGeometry(QtCore.QRect(260, 80, 75, 23))
        login_dialog.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(login_dialog)
        QtCore.QMetaObject.connectSlotsByName(login_dialog)
        
        
        #self.login_button.clicked.connect(self.login_button_clicked)
        #self.cancel_button.clicked.connect(self.cancel_button_clicked)       
    
    
    def show_exception(self, ex):
        err_msg = QMessageBox()
        err_msg.setIcon(QMessageBox.Critical)
        err_msg.setText(str(ex.args[0]))
        err_msg.show()            
    
        
    def login_button_clicked(self):
        pass
        
    def login(self, username, password):
        return True

    def cancel_button_clicked(self):
        pass

    def retranslateUi(self, login_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_dialog.setWindowTitle(_translate("login_dialog", "Login"))
        login_dialog.username_label.setText(_translate("login_dialog", "Username"))
        login_dialog.password_label.setText(_translate("login_dialog", "Password"))
        login_dialog.login_button.setText(_translate("login_dialog", "Login"))
        login_dialog.cancel_button.setText(_translate("login_dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_login_dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


