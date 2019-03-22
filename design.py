import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(225, 70)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.slaveIOLabel = QtWidgets.QLabel(self.centralwidget)
        self.slaveIOLabel.setGeometry(QtCore.QRect(5, 5, 151, 18))
        self.slaveIOLabel.setObjectName("slaveIOLabel")
        self.slaveSQLLabel = QtWidgets.QLabel(self.centralwidget)
        self.slaveSQLLabel.setGeometry(QtCore.QRect(5, 20, 151, 18))
        self.slaveSQLLabel.setObjectName("slaveSQLLabel")
        self.lastErrorLabel = QtWidgets.QLabel(self.centralwidget)
        self.lastErrorLabel.setGeometry(QtCore.QRect(5, 35, 151, 18))
        self.lastErrorLabel.setObjectName("lastErrorLabel")
        self.secondMasterLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondMasterLabel.setGeometry(QtCore.QRect(5, 50, 151, 18))
        self.secondMasterLabel.setObjectName("secondMasterLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 5, 58, 18))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 58, 18))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 35, 58, 18))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 50, 58, 18))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Replica Status"))
        self.slaveIOLabel.setText(_translate("MainWindow", "Slave IO Running:"))
        self.slaveSQLLabel.setText(_translate("MainWindow", "Slave SQL Running:"))
        self.lastErrorLabel.setText(_translate("MainWindow", "Last_Error №:"))
        self.secondMasterLabel.setText(_translate("MainWindow", "Seconds Behind Master:"))
        self.label.setText(_translate("MainWindow", "Null"))
        self.label_2.setText(_translate("MainWindow", "Null"))
        self.label_3.setText(_translate("MainWindow", "Null"))
        self.label_4.setText(_translate("MainWindow", "Null"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
