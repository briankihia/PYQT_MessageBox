# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popUp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(200, 160, 141, 41))
        self.button1.setObjectName("button1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button1.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "PushButton"))


    def show_popup(self):
        # first we create an instance of the class(imported it at top of page) then call some methods on it and changing some attributes of it
        msg = QMessageBox()
        # this is the message of the pop up window
        msg.setWindowTitle("Tutorial text")
        msg.setText("This is main text")
        # PyQt has built in Icons ie. warning, Information, Caution, Question
        msg.setIcon(QMessageBox.Warning)
        # Changing the buttons in the box to state different things
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        # also we want to change the default button for the messageBox
        msg.setDefaultButton(QMessageBox.Cancel)
        # adding a line of text that shows beneath the initial one on the messaging box
        msg.setInformativeText("Informaive text")

        # now we add detail text
        # and how to link up those buttons to know which is being clicked
        # whatever text we put here is hidden unless the button is clicked
        msg.setDetailedText("details")

        # now to know which button is being clicked when were getting out of the program or when going through the message box
        # to do this we create another function popup_button

        msg.buttonClicked.connect(self.popup_button)

        # if we wanna show a message box
        x = msg.exec_()

    # i is going to be the widget that we clicked
    def popup_button(self,i):
        # when any button is clicked in the message box the show_popup function triggers whatever button is clicked and calls this method and passes the button that was clicked 
        # so we first go to the above function and add an event listener
        # to see what button has been clicked we print it out first
        print(i.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())