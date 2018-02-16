# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimeTrackNew.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 520)
        self.lblTrackTime = QtWidgets.QLabel(Dialog)
        self.lblTrackTime.setGeometry(QtCore.QRect(260, 20, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(55)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lblTrackTime.setFont(font)
        self.lblTrackTime.setObjectName("lblTrackTime")
        self.btnStartTimer = QtWidgets.QPushButton(Dialog)
        self.btnStartTimer.setGeometry(QtCore.QRect(370, 490, 75, 23))
        self.btnStartTimer.setObjectName("btnStartTimer")
        self.btnStopTimer = QtWidgets.QPushButton(Dialog)
        self.btnStopTimer.setGeometry(QtCore.QRect(450, 490, 75, 23))
        self.btnStopTimer.setObjectName("btnStopTimer")
        self.project_list = QtWidgets.QListWidget(Dialog)
        self.project_list.setGeometry(QtCore.QRect(10, 30, 171, 451))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.project_list.setFont(font)
        self.project_list.setObjectName("project_list")
        self.task_list = QtWidgets.QListWidget(Dialog)
        self.task_list.setGeometry(QtCore.QRect(190, 120, 331, 361))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.task_list.setFont(font)
        self.task_list.setObjectName("task_list")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblTrackTime.setText(_translate("Dialog", "02:55:45"))
        self.btnStartTimer.setText(_translate("Dialog", "Start Timer"))
        self.btnStopTimer.setText(_translate("Dialog", "Stop Timer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

