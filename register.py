import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import data_class as dc

dp = sqlite3.connect("Store_dataBase.db")
cr = dp.cursor()

class Ui_registration_window(object):
    def setupUi(self, registration_window):
        registration_window.setObjectName("registration_window")
        registration_window.resize(1000, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../pyqt5/MATELRIAL/IMG/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        registration_window.setWindowIcon(icon)
        registration_window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(registration_window)
        self.centralwidget.setObjectName("centralwidget")
        self.register_background_label = QtWidgets.QLabel(self.centralwidget)
        self.register_background_label.setGeometry(QtCore.QRect(-10, -3, 1011, 90))
        self.register_background_label.setStyleSheet("background-color:rgb(6, 160, 170);")
        self.register_background_label.setText("")
        self.register_background_label.setObjectName("register_background_label")
        self.register_alreadyhasaccount_label = QtWidgets.QLabel(self.centralwidget)
        self.register_alreadyhasaccount_label.setGeometry(QtCore.QRect(430, 650, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.register_alreadyhasaccount_label.setFont(font)
        self.register_alreadyhasaccount_label.setStyleSheet("background-color: TRANSPARENT;\n"
"color:rgb(6, 160, 170);")
        self.register_alreadyhasaccount_label.setObjectName("register_alreadyhasaccount_label")
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../pyqt5/MATELRIAL/IMG/icons8-home-1000.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.register_name_label = QtWidgets.QLabel(self.centralwidget)
        self.register_name_label.setGeometry(QtCore.QRect(280, 340, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.register_name_label.setFont(font)
        self.register_name_label.setStyleSheet("background-color: TRANSPARENT;\n"
"color: rgb(6, 160, 170);")
        self.register_name_label.setObjectName("register_name_label")
        self.register_account_label = QtWidgets.QLabel(self.centralwidget)
        self.register_account_label.setGeometry(QtCore.QRect(480, 180, 150, 150))
        self.register_account_label.setText("")
        self.register_account_label.setPixmap(QtGui.QPixmap("../../../../pyqt5/MATELRIAL/IMG/account.jpg"))
        self.register_account_label.setScaledContents(True)
        self.register_account_label.setObjectName("register_account_label")
        self.register_b3b3Logo_label = QtWidgets.QLabel(self.centralwidget)
        self.register_b3b3Logo_label.setGeometry(QtCore.QRect(30, 7, 80, 80))
        self.register_b3b3Logo_label.setStyleSheet("background-color: transparent;")
        self.register_b3b3Logo_label.setText("")
        self.register_b3b3Logo_label.setPixmap(QtGui.QPixmap("../../../../pyqt5/MATELRIAL/IMG/Logo.jpg"))
        self.register_b3b3Logo_label.setScaledContents(True)
        self.register_b3b3Logo_label.setObjectName("register_b3b3Logo_label")
        self.register_signin_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.register_signin_pushButton.setGeometry(QtCore.QRect(630, 660, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.register_signin_pushButton.setFont(font)
        self.register_signin_pushButton.setStyleSheet("background-color: TRANSPARENT;\n"
"color:rgb(6, 160, 170);")
        self.register_signin_pushButton.setObjectName("register_signin_pushButton")
        self.register_name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.register_name_lineEdit.setGeometry(QtCore.QRect(390, 340, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(13)
        self.register_name_lineEdit.setFont(font)
        self.register_name_lineEdit.setStyleSheet("background-color:white;\n"
"border: 5px solid rgb(6, 160, 170);\n"
"color: rgb(6, 160, 170);\n"
"border-radius:10px;\n"
"padding-left:10px;")
        self.register_name_lineEdit.setText("")
        self.register_name_lineEdit.setObjectName("register_name_lineEdit")
        self.register_email_label = QtWidgets.QLabel(self.centralwidget)
        self.register_email_label.setGeometry(QtCore.QRect(290, 390, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.register_email_label.setFont(font)
        self.register_email_label.setStyleSheet("background-color: TRANSPARENT;\n"
"color: rgb(6, 160, 170);")
        self.register_email_label.setObjectName("register_email_label")
        self.register_email_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.register_email_lineEdit.setGeometry(QtCore.QRect(390, 390, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(13)
        self.register_email_lineEdit.setFont(font)
        self.register_email_lineEdit.setStyleSheet("background-color:white;\n"
"border: 5px solid rgb(6, 160, 170);\n"
"color: rgb(6, 160, 170);\n"
"border-radius:10px;\n"
"padding-left:10px;")
        self.register_email_lineEdit.setText("")
        self.register_email_lineEdit.setObjectName("register_email_lineEdit")
        self.register_address_label = QtWidgets.QLabel(self.centralwidget)
        self.register_address_label.setGeometry(QtCore.QRect(250, 440, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.register_address_label.setFont(font)
        self.register_address_label.setStyleSheet("background-color: TRANSPARENT;\n"
"color: rgb(6, 160, 170);")
        self.register_address_label.setObjectName("register_address_label")
        self.register_password_label = QtWidgets.QLabel(self.centralwidget)
        self.register_password_label.setGeometry(QtCore.QRect(230, 490, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.register_password_label.setFont(font)
        self.register_password_label.setStyleSheet("background-color: TRANSPARENT;\n"
"color: rgb(6, 160, 170);")
        self.register_password_label.setObjectName("register_password_label")
        self.register_address_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.register_address_lineEdit.setGeometry(QtCore.QRect(390, 440, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(13)
        self.register_address_lineEdit.setFont(font)
        self.register_address_lineEdit.setStyleSheet("background-color:white;\n"
"border: 5px solid rgb(6, 160, 170);\n"
"color: rgb(6, 160, 170);\n"
"border-radius:10px;\n"
"padding-left:10px;")
        self.register_address_lineEdit.setText("")
        self.register_address_lineEdit.setObjectName("register_address_lineEdit")
        self.register_password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.register_password_lineEdit.setGeometry(QtCore.QRect(390, 490, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(13)
        self.register_password_lineEdit.setFont(font)
        self.register_password_lineEdit.setStyleSheet("background-color:white;\n"
"border: 5px solid rgb(6, 160, 170);\n"
"color: rgb(6, 160, 170);\n"
"border-radius:10px;\n"
"padding-left:10px;")
        self.register_password_lineEdit.setText("")
        self.register_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_password_lineEdit.setObjectName("register_password_lineEdit")
        self.register_female_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.register_female_radioButton.setGeometry(QtCore.QRect(600, 550, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.register_female_radioButton.setFont(font)
        self.register_female_radioButton.setStyleSheet("background-color: TRANSPARENT;\n"
"color: rgb(6, 160, 170);")
        self.register_female_radioButton.setObjectName("register_female_radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(registration_window)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.register_female_radioButton)
        self.register_male_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.register_male_radioButton.setGeometry(QtCore.QRect(470, 550, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.register_male_radioButton.setFont(font)
        self.register_male_radioButton.setStyleSheet("background-color: TRANSPARENT;\n"
"color: rgb(6, 160, 170);")
        self.register_male_radioButton.setObjectName("register_male_radioButton")
        self.buttonGroup.addButton(self.register_male_radioButton)
        self.register_gender_label = QtWidgets.QLabel(self.centralwidget)
        self.register_gender_label.setGeometry(QtCore.QRect(260, 540, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.register_gender_label.setFont(font)
        self.register_gender_label.setStyleSheet("background-color: TRANSPARENT;\n"
"color:rgb(6, 160, 170);")
        self.register_gender_label.setObjectName("register_gender_label")
        self.register_register_pushButton = QtWidgets.QPushButton(self.centralwidget,  clicked= lambda: register_button_action())
        self.register_register_pushButton.setGeometry(QtCore.QRect(500, 590, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.register_register_pushButton.setFont(font)
        self.register_register_pushButton.setStyleSheet("\n"
"background-color:rgb(5, 159, 169);\n"
"color: white;\n"
"border-radius:25px;\n"
"")
        self.register_register_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.register_register_pushButton.setObjectName("register_register_pushButton")
        registration_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(registration_window)
        self.statusbar.setObjectName("statusbar")
        registration_window.setStatusBar(self.statusbar)

        self.retranslateUi(registration_window)
        QtCore.QMetaObject.connectSlotsByName(registration_window)

        def register_button_action():
            customer_obj = dc.customer("","","","","")
            user_obj = dc.user("","","","")
            user_obj.user_name = self.register_name_lineEdit.text()
            if self.register_female_radioButton.isChecked():
                     user_obj.user_gender = 'F'
            if self.register_male_radioButton.isChecked():
                     user_obj.user_gender = 'M'
            user_obj.user_password = self.register_password_lineEdit.text()
            user_obj.user_email = self.register_email_lineEdit.text()
            customer_address = self.register_address_lineEdit.text()
            temp = customer_obj.registration(user_obj, customer_address)
            if temp == 0:
                msg = QtWidgets.QMessageBox() 
                msg.setIcon(QtWidgets.QMessageBox.Critical) 
                msg.setText(f"Make Sure That You Fill All Fields") 
                msg.setWindowTitle("Error") 
                retval = msg.exec_()
            else:
                msg = QtWidgets.QMessageBox() 
                msg.setIcon(QtWidgets.QMessageBox.Information) 
                msg.setText(f"Registration Successfully") 
                msg.setWindowTitle("Info") 
                retval = msg.exec_()

    def retranslateUi(self, registration_window):
        _translate = QtCore.QCoreApplication.translate
        registration_window.setWindowTitle(_translate("registration_window", "B3B3 - Registration"))
        self.register_alreadyhasaccount_label.setText(_translate("registration_window", "Already has account!"))
        self.register_name_label.setText(_translate("registration_window", "Name"))
        self.register_signin_pushButton.setText(_translate("registration_window", "Sign In"))
        self.register_email_label.setText(_translate("registration_window", "Email"))
        self.register_address_label.setText(_translate("registration_window", "Address"))
        self.register_password_label.setText(_translate("registration_window", "Password"))
        self.register_female_radioButton.setText(_translate("registration_window", "Female"))
        self.register_male_radioButton.setText(_translate("registration_window", "Male"))
        self.register_gender_label.setText(_translate("registration_window", "Gender"))
        self.register_register_pushButton.setText(_translate("registration_window", "Register"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registration_window = QtWidgets.QMainWindow()
    ui = Ui_registration_window()
    ui.setupUi(registration_window)
    registration_window.show()
    sys.exit(app.exec_())
