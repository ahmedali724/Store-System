from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

dp = sqlite3.connect("Store_dataBase.db")
cr = dp.cursor()

class Ui_orderWindow(object):
    def setupUi(self, orderWindow,items:list):
        orderWindow.setObjectName("orderWindow")
        orderWindow.resize(1000, 800)
        orderWindow.setMinimumSize(QtCore.QSize(1000, 800))
        orderWindow.setMaximumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        orderWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        orderWindow.setWindowIcon(icon)
        orderWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        #scroll area
        self.scrollArea = QtWidgets.QScrollArea(orderWindow)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 90, 1011, 640))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1009, 709))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")

        for i in range(0,len(items)):
                #fram 
                self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
                self.frame_4.setMinimumSize(QtCore.QSize(200, 250))
                self.frame_4.setMaximumSize(QtCore.QSize(16777215, 300))
                self.frame_4.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_4.setObjectName("frame_4")
                self.category1_productbackground3_label_3 = QtWidgets.QLabel(self.frame_4)
                self.category1_productbackground3_label_3.setGeometry(QtCore.QRect(20, 50, 921, 200))
                self.category1_productbackground3_label_3.setStyleSheet("background-color: rgb(219, 219, 219);\n"
        "border-radius:10px;")
                self.category1_productbackground3_label_3.setText("")
                self.category1_productbackground3_label_3.setScaledContents(False)
                self.category1_productbackground3_label_3.setObjectName("category1_productbackground3_label_3")
                self.category1_productdetail3_label_3 = QtWidgets.QLabel(self.frame_4)
                self.category1_productdetail3_label_3.setGeometry(QtCore.QRect(210, 130, 211, 31))
                self.category1_productdetail3_label_3.setText(f"{items[i][1]}")
                font = QtGui.QFont()
                font.setFamily("Sans Serif Collection")
                font.setPointSize(8)
                self.category1_productdetail3_label_3.setFont(font)
                self.category1_productdetail3_label_3.setStyleSheet("background-color: TRANSPARENT;\n"
        "color: rgb(6, 160, 170);")
                self.category1_productdetail3_label_3.setObjectName("category1_productdetail3_label_3")
                #price
                self.category1_productprice3_label_3 = QtWidgets.QLabel(self.frame_4)
                #------------->>>>>>>>>>>>>
                self.category1_productprice3_label_3.setGeometry(QtCore.QRect(780, 80, 150, 41))
                self.category1_productprice3_label_3.setText(f"{items[i][2]}")
                font = QtGui.QFont()
                font.setFamily("Sans Serif Collection")
                font.setPointSize(25)
                self.category1_productprice3_label_3.setFont(font)
                self.category1_productprice3_label_3.setStyleSheet("background-color: TRANSPARENT;\n"
        "color: rgb(6, 160, 170);")
                self.category1_productprice3_label_3.setObjectName("category1_productprice3_label_3")
                #name
                self.category1_productname3_label_3 = QtWidgets.QLabel(self.frame_4)
                self.category1_productname3_label_3.setGeometry(QtCore.QRect(210, 80, 211, 51))
                self.category1_productname3_label_3.setText(f"{items[i][0]}")
                font = QtGui.QFont()
                font.setFamily("Sans Serif Collection")
                font.setPointSize(20)
                self.category1_productname3_label_3.setFont(font)
                self.category1_productname3_label_3.setStyleSheet("background-color: TRANSPARENT;\n"
        "color: rgb(6, 160, 170);")
                self.category1_productname3_label_3.setObjectName("category1_productname3_label_3")
                #image
                self.category1_productimg3_label_3 = QtWidgets.QLabel(self.frame_4)
                #=============>....>>>>>>>>>
                self.category1_productimg3_label_3.setGeometry(QtCore.QRect(40, 70, 160, 160))
                self.category1_productimg3_label_3.setStyleSheet("background-color:transparent;\n"
        "border: 5px solid rgb(6, 160, 170);\n"
        "border-radius:10px;\n"
        "")
                self.category1_productimg3_label_3.setText("")
                self.category1_productimg3_label_3.setPixmap(QtGui.QPixmap(items[i][3][1:-1]))
                self.category1_productimg3_label_3.setScaledContents(True)
                self.category1_productimg3_label_3.setObjectName("category1_productimg3_label_3")

                # self.category1_productbackground3_label_3.raise_()
                # self.category1_productdetail3_label_3.raise_()
                # self.category1_productprice3_label_3.raise_()
                # self.category1_productname3_label_3.raise_()
                # self.category1_productimg3_label_3.raise_()
                # self.product_buy_pushButton.raise_()

                self.verticalLayout.addWidget(self.frame_4)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

#==========================================================================>>>>
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.frame = QtWidgets.QFrame(orderWindow)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1111, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # self.category1_account_pushButton = QtWidgets.QPushButton(self.frame)
        # self.category1_account_pushButton.setGeometry(QtCore.QRect(660, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        # self.category1_account_pushButton.setFont(font)
        # self.category1_account_pushButton.setStyleSheet("border: 5px solid white;\n"
        # "background-color: rgb(255, 255, 255);\n"
        # "color: rgb(5, 159, 169);\n"
        # "border-radius:10px;\n"
        # "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/icons8-male-user-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.category1_account_pushButton.setIcon(icon1)
        # self.category1_account_pushButton.setIconSize(QtCore.QSize(20, 20))
        # self.category1_account_pushButton.setObjectName("category1_account_pushButton")
        self.category1_b3b3Logo_label = QtWidgets.QLabel(self.frame)
        self.category1_b3b3Logo_label.setGeometry(QtCore.QRect(30, 10, 80, 80))
        self.category1_b3b3Logo_label.setStyleSheet("background-color: transparent;")
        self.category1_b3b3Logo_label.setText("")
        self.category1_b3b3Logo_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"))
        self.category1_b3b3Logo_label.setScaledContents(True)
        self.category1_b3b3Logo_label.setObjectName("category1_b3b3Logo_label")
        self.category1_background_label = QtWidgets.QLabel(self.frame)
        self.category1_background_label.setGeometry(QtCore.QRect(0, 0, 1121, 90))
        self.category1_background_label.setStyleSheet("background-color:rgb(6, 160, 170);")
        self.category1_background_label.setText("")
        self.category1_background_label.setObjectName("category1_background_label")
        self.category1_home_pushButton = QtWidgets.QPushButton(self.frame)
        self.category1_home_pushButton.setGeometry(QtCore.QRect(900, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.category1_home_pushButton.setFont(font)
        self.category1_home_pushButton.setStyleSheet("border: 5px solid white;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(5, 159, 169);\n"
"border-radius:10px;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/icons8-home-1000.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.category1_home_pushButton.setIcon(icon2)
        self.category1_home_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.category1_home_pushButton.setObjectName("category1_home_pushButton")
        # self.category1_orders_pushButton = QtWidgets.QPushButton(self.frame)
        # self.category1_orders_pushButton.setGeometry(QtCore.QRect(780, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        # self.category1_orders_pushButton.setFont(font)
        # self.category1_orders_pushButton.setStyleSheet("border: 5px solid white;\n"
        # "background-color: rgb(255, 255, 255);\n"
        # "color: rgb(5, 159, 169);\n"
        # "border-radius:10px;\n"
        # "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/orders.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.category1_orders_pushButton.setIcon(icon3)
        # self.category1_orders_pushButton.setIconSize(QtCore.QSize(30, 30))
        # self.category1_orders_pushButton.setObjectName("category1_orders_pushButton")
        # self.category1_cart_pushButton = QtWidgets.QPushButton(self.frame)
        # self.category1_cart_pushButton.setGeometry(QtCore.QRect(900, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        # self.category1_cart_pushButton.setFont(font)
        # self.category1_cart_pushButton.setStyleSheet("border: 5px solid white;\n"
        # "background-color: rgb(255, 255, 255);\n"
        # "color: rgb(5, 159, 169);\n"
        # "border-radius:10px;\n"
        # "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/icons8-cart-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.category1_cart_pushButton.setIcon(icon4)
        # self.category1_cart_pushButton.setIconSize(QtCore.QSize(30, 30))
        # self.category1_cart_pushButton.setObjectName("category1_cart_pushButton")
        self.category1_background_label.raise_()
        # self.category1_account_pushButton.raise_()
        self.category1_b3b3Logo_label.raise_()
        self.category1_home_pushButton.raise_()
        # self.category1_orders_pushButton.raise_()
        # self.category1_cart_pushButton.raise_()

        self.retranslateUi(orderWindow)
        QtCore.QMetaObject.connectSlotsByName(orderWindow)

    def retranslateUi(self, orderWindow):
        _translate = QtCore.QCoreApplication.translate
        orderWindow.setWindowTitle(_translate("orderWindow", "B3B3 - Cart"))
       # self.category1_productdetail3_label_3.setText(_translate("orderWindow", "product details (category, color,etc)"))
        #self.category1_productprice3_label_3.setText(_translate("orderWindow", "50$"))
        #self.category1_productname3_label_3.setText(_translate("orderWindow", "Product name"))
        
        # self.category1_account_pushButton.setText(_translate("orderWindow", "Account"))
        self.category1_home_pushButton.setText(_translate("orderWindow", "Home"))
        # self.category1_orders_pushButton.setText(_translate("orderWindow", "Orders"))
        # self.category1_cart_pushButton.setText(_translate("orderWindow", "Cart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    orderWindow = QtWidgets.QWidget()
    ui = Ui_orderWindow()
    ui.setupUi(orderWindow)
    orderWindow.show()
    sys.exit(app.exec_())
