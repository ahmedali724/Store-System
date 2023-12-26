from PyQt5 import QtCore, QtGui, QtWidgets
import data_class as dc

class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(1000, 800)
        login_window.setMinimumSize(QtCore.QSize(1000, 800))
        login_window.setMaximumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        login_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_window.setWindowIcon(icon)
        login_window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.login_email_label = QtWidgets.QLabel(self.centralwidget)
        self.login_email_label.setGeometry(QtCore.QRect(280, 440, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.login_email_label.setFont(font)
        self.login_email_label.setStyleSheet("background-color: TRANSPARENT;\n"
        "color: rgb(6, 160, 170);")
        self.login_email_label.setObjectName("login_email_label")
        self.login_account_label = QtWidgets.QLabel(self.centralwidget)
        self.login_account_label.setGeometry(QtCore.QRect(440, 210, 200, 200))
        self.login_account_label.setText("")
        self.login_account_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/account.jpg"))
        self.login_account_label.setScaledContents(True)
        self.login_account_label.setObjectName("login_account_label")
        self.login_pass_label = QtWidgets.QLabel(self.centralwidget)
        self.login_pass_label.setGeometry(QtCore.QRect(220, 510, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.login_pass_label.setFont(font)
        self.login_pass_label.setStyleSheet("background-color: TRANSPARENT;\n"
        "color:rgb(6, 160, 170);")
        self.login_pass_label.setObjectName("login_pass_label")
        self.login_email_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_email_lineEdit.setGeometry(QtCore.QRect(380, 440, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(13)
        self.login_email_lineEdit.setFont(font)
        self.login_email_lineEdit.setStyleSheet("background-color:white;\n"
        "border: 5px solid rgb(6, 160, 170);\n"
        "color: rgb(6, 160, 170);\n"
        "border-radius:10px;\n"
        "padding-left:10px;")
        self.login_email_lineEdit.setText("")
        self.login_email_lineEdit.setObjectName("login_email_lineEdit")
        self.login_not_a_member_label = QtWidgets.QLabel(self.centralwidget)
        self.login_not_a_member_label.setGeometry(QtCore.QRect(430, 640, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.login_not_a_member_label.setFont(font)
        self.login_not_a_member_label.setStyleSheet("background-color: TRANSPARENT;\n"
        "color:rgb(6, 160, 170);")
        self.login_not_a_member_label.setObjectName("login_not_a_member_label")
        self.login_signup_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.login_signup_pushButton.setGeometry(QtCore.QRect(580, 640, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.login_signup_pushButton.setFont(font)
        self.login_signup_pushButton.setStyleSheet("background-color: TRANSPARENT;\n"
        "color:rgb(6, 160, 170);")
        self.login_signup_pushButton.setObjectName("login_signup_pushButton")
        self.login_password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_password_lineEdit.setGeometry(QtCore.QRect(380, 507, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(13)
        self.login_password_lineEdit.setFont(font)
        self.login_password_lineEdit.setStyleSheet("background-color:white;\n"
        "border: 5px solid rgb(6, 160, 170);\n"
        "color: rgb(6, 160, 170);\n"
        "border-radius:10px;\n"
        "padding-left:10px;")
        self.login_password_lineEdit.setText("")
        self.login_password_lineEdit.setFrame(False)
        self.login_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password_lineEdit.setObjectName("login_password_lineEdit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1111, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.login_b3b3Logo_label = QtWidgets.QLabel(self.frame)
        self.login_b3b3Logo_label.setGeometry(QtCore.QRect(30, 10, 80, 80))
        self.login_b3b3Logo_label.setStyleSheet("background-color: transparent;")
        self.login_b3b3Logo_label.setText("")
        self.login_b3b3Logo_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"))
        self.login_b3b3Logo_label.setScaledContents(True)
        self.login_b3b3Logo_label.setObjectName("login_b3b3Logo_label")
        self.login_background_label = QtWidgets.QLabel(self.frame)
        self.login_background_label.setGeometry(QtCore.QRect(0, 0, 1121, 90))
        self.login_background_label.setStyleSheet("background-color:rgb(6, 160, 170);")
        self.login_background_label.setText("")
        self.login_background_label.setObjectName("login_background_label")
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/icons8-home-1000.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_background_label.raise_()
        self.login_b3b3Logo_label.raise_()
        self.login_login_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: button_action(self.login_email_lineEdit.text(), self.login_password_lineEdit.text()))
        self.login_login_pushButton.setGeometry(QtCore.QRect(480, 570, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_login_pushButton.setFont(font)
        self.login_login_pushButton.setStyleSheet("\n"
        "background-color:rgb(5, 159, 169);\n"
        "color: white;\n"
        "border-radius:25px;\n"
        "")
        self.login_login_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.login_login_pushButton.setObjectName("login_login_pushButton")
        login_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

        def button_action(email, password):
                user_obj = dc.user("","","","")
                global user_type_shared
                user_type_shared = user_obj.login(email, password)
                if user_type_shared == 0:
                        msg = QtWidgets.QMessageBox() 
                        msg.setIcon(QtWidgets.QMessageBox.Critical) 
                        msg.setText("Wrong password or email") 
                        msg.setWindowTitle("Error") 
                        retval = msg.exec_() 
            
    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "B3B3 - Login"))
        self.login_email_label.setText(_translate("login_window", "Email"))
        self.login_pass_label.setText(_translate("login_window", "Password"))
        self.login_not_a_member_label.setText(_translate("login_window", "Not a member"))
        self.login_signup_pushButton.setText(_translate("login_window", "Sign Up"))
        self.login_login_pushButton.setText(_translate("login_window", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    ui = Ui_login_window()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec_())
