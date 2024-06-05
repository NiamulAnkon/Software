from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 791, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")

        self.tsknmlab = QtWidgets.QLabel(self.centralwidget)
        self.tsknmlab.setGeometry(QtCore.QRect(40, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tsknmlab.setFont(font)
        self.tsknmlab.setAlignment(QtCore.Qt.AlignCenter)
        self.tsknmlab.setObjectName("tsknmlab")

        self.tsctglab = QtWidgets.QLabel(self.centralwidget)
        self.tsctglab.setGeometry(QtCore.QRect(150, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tsctglab.setFont(font)
        self.tsctglab.setAlignment(QtCore.Qt.AlignCenter)
        self.tsctglab.setObjectName("tsctglab")

        self.tskdeslab = QtWidgets.QLabel(self.centralwidget)
        self.tskdeslab.setGeometry(QtCore.QRect(300, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tskdeslab.setFont(font)
        self.tskdeslab.setAlignment(QtCore.Qt.AlignCenter)
        self.tskdeslab.setObjectName("tskdeslab")

        self.tskprplab = QtWidgets.QLabel(self.centralwidget)
        self.tskprplab.setGeometry(QtCore.QRect(420, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tskprplab.setFont(font)
        self.tskprplab.setAlignment(QtCore.Qt.AlignCenter)
        self.tskprplab.setObjectName("tskprplab")

        self.stslab = QtWidgets.QLabel(self.centralwidget)
        self.stslab.setGeometry(QtCore.QRect(570, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stslab.setFont(font)
        self.stslab.setAlignment(QtCore.Qt.AlignCenter)
        self.stslab.setObjectName("stslab")

        self.tskname = QtWidgets.QLineEdit(self.centralwidget)
        self.tskname.setGeometry(QtCore.QRect(20, 110, 113, 20))
        self.tskname.setObjectName("tskname")

        self.tskctg = QtWidgets.QLineEdit(self.centralwidget)
        self.tskctg.setGeometry(QtCore.QRect(150, 110, 113, 20))
        self.tskctg.setObjectName("tskctg")

        self.tskprp = QtWidgets.QLineEdit(self.centralwidget)
        self.tskprp.setGeometry(QtCore.QRect(420, 110, 113, 20))
        self.tskprp.setObjectName("tskprp")

        self.sts = QtWidgets.QLineEdit(self.centralwidget)
        self.sts.setGeometry(QtCore.QRect(560, 110, 113, 20))
        self.sts.setObjectName("sts")

        self.tskdes = QtWidgets.QLineEdit(self.centralwidget)
        self.tskdes.setGeometry(QtCore.QRect(290, 110, 113, 20))
        self.tskdes.setObjectName("tskdes")

        self.foools = QtWidgets.QPushButton(self.centralwidget)
        self.foools.setGeometry(QtCore.QRect(300, 180, 111, 31))
        self.foools.setObjectName("foools")
        self.foools.clicked.connect(self.add_tasks_fools)

        self.tasklist = QtWidgets.QListWidget(self.centralwidget)
        self.tasklist.setGeometry(QtCore.QRect(0, 240, 801, 361))
        self.tasklist.setObjectName("tasklist")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Making to-do list to sohw of"))
        self.tsknmlab.setText(_translate("MainWindow", "Task Name"))
        self.tsctglab.setText(_translate("MainWindow", "Task Catageory"))
        self.tskdeslab.setText(_translate("MainWindow", "Task Des"))
        self.tskprplab.setText(_translate("MainWindow", "Task purpose"))
        self.stslab.setText(_translate("MainWindow", "Status"))
        self.foools.setText(_translate("MainWindow", "Add task fools"))
    def add_tasks_fools(self):
        taks_name = self.tskname.text()
        task_categeory = self.tskctg.text()
        task_purpose = self.tskprp.text()
        task_status = self.sts.text()
        task_description = self.tskdes.text()
        info = f"Task Name: {taks_name} Task Catageory: {task_categeory}, Task Purpose: {task_purpose} Task Description: {task_description} Task Status: {task_status}"
        self.tasklist.addItem(info)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
