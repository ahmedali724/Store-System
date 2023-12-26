from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_product_window(object):
    product_id = None
    user_id = None
    def setupUi(self, product_window,product_img,product_name,product_price,product_details):
        product_window.setObjectName("product_window")
        product_window.resize(1000, 800)
        product_window.setMinimumSize(QtCore.QSize(1000, 800))
        product_window.setMaximumSize(QtCore.QSize(1000, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        product_window.setWindowIcon(icon)
        product_window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.product_productprice_label = QtWidgets.QLabel(product_window)
        self.product_productprice_label.setText(product_price)
        self.product_productprice_label.setGeometry(QtCore.QRect(700, 170, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(25)
        self.product_productprice_label.setFont(font)
        self.product_productprice_label.setStyleSheet("background-color: TRANSPARENT;\n"
"color: rgb(6, 160, 170);")
        self.product_productprice_label.setObjectName("product_productprice_label")
        self.product_productbackground1_label = QtWidgets.QLabel(product_window)
        self.product_productbackground1_label.setGeometry(QtCore.QRect(40, 110, 921, 571))
        self.product_productbackground1_label.setStyleSheet("background-color: rgb(219, 219, 219);\n"
"border-radius:15px;")
        self.product_productbackground1_label.setText("")
        self.product_productbackground1_label.setScaledContents(False)
        self.product_productbackground1_label.setObjectName("product_productbackground1_label")
        self.product_productname_label = QtWidgets.QLabel(product_window)
        self.product_productname_label.setText(product_name)
        self.product_productname_label.setGeometry(QtCore.QRect(340, 170, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(20)
        self.product_productname_label.setFont(font)
        self.product_productname_label.setStyleSheet("background-color: TRANSPARENT;\n"
"color: rgb(6, 160, 170);")
        self.product_productname_label.setObjectName("product_productname_label")
        self.product_productimg_label = QtWidgets.QLabel(product_window)
        self.product_productimg_label.setGeometry(QtCore.QRect(70, 140, 250, 250))
        self.product_productimg_label.setStyleSheet("background-color:transparent;\n"
"border: 5px solid rgb(6, 160, 170);\n"
"border-radius:10px;\n"
"")
        self.product_productimg_label.setText("")
        self.product_productimg_label.setPixmap(QtGui.QPixmap(product_img))
        self.product_productimg_label.setScaledContents(True)
        self.product_productimg_label.setObjectName("product_productimg_label")
        self.product_addtocart_pushButton = QtWidgets.QPushButton(product_window)
        self.product_addtocart_pushButton.setGeometry(QtCore.QRect(690, 700, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.product_addtocart_pushButton.setFont(font)
        self.product_addtocart_pushButton.setStyleSheet("background-color:transparent;\n"
"color: #06a0aa;\n"
"border-radius:20px;\n"
"border: 3px solid #06a0aa;\n"
"")
        self.product_addtocart_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.product_addtocart_pushButton.setObjectName("product_addtocart_pushButton")
        self.product_productmaindetail1_label = QtWidgets.QLabel(product_window)
        self.product_productmaindetail1_label.setText(product_details)
        self.product_productmaindetail1_label.setGeometry(QtCore.QRect(340, 220, 591, 361))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(13)
        self.product_productmaindetail1_label.setFont(font)
        self.product_productmaindetail1_label.setStyleSheet("background-color: TRANSPARENT;\n"
"color: rgb(6, 160, 170);")
        self.product_productmaindetail1_label.setWordWrap(True)
        self.product_productmaindetail1_label.setObjectName("product_productmaindetail1_label")
        self.product_buy_pushButton = QtWidgets.QPushButton(product_window)
        self.product_buy_pushButton.setGeometry(QtCore.QRect(830, 700, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.product_buy_pushButton.setFont(font)
        self.product_buy_pushButton.setStyleSheet("\n"
"background-color:rgb(5, 159, 169);\n"
"color: white;\n"
"border-radius:20px;\n"
"")
        self.product_buy_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.product_buy_pushButton.setObjectName("product_buy_pushButton")
        self.frame = QtWidgets.QFrame(product_window)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1111, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
#         self.product_account_pushButton = QtWidgets.QPushButton(self.frame)
#         self.product_account_pushButton.setGeometry(QtCore.QRect(660, 30, 93, 28))
#         font = QtGui.QFont()
#         font.setFamily("Sans Serif Collection")
#         font.setPointSize(10)
#         self.product_account_pushButton.setFont(font)
#         self.product_account_pushButton.setStyleSheet("border: 5px solid white;\n"
# "background-color: rgb(255, 255, 255);\n"
# "color: rgb(5, 159, 169);\n"
# "border-radius:10px;\n"
# "")
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/icons8-male-user-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.product_account_pushButton.setIcon(icon1)
#         self.product_account_pushButton.setIconSize(QtCore.QSize(20, 20))
#         self.product_account_pushButton.setObjectName("product_account_pushButton")
        self.product_b3b3Logo_label = QtWidgets.QLabel(self.frame)
        self.product_b3b3Logo_label.setGeometry(QtCore.QRect(30, 10, 80, 80))
        self.product_b3b3Logo_label.setStyleSheet("background-color: transparent;")
        self.product_b3b3Logo_label.setText("")
        self.product_b3b3Logo_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"))
        self.product_b3b3Logo_label.setScaledContents(True)
        self.product_b3b3Logo_label.setObjectName("product_b3b3Logo_label")
        self.product_background_label = QtWidgets.QLabel(self.frame)
        self.product_background_label.setGeometry(QtCore.QRect(0, 0, 1121, 90))
        self.product_background_label.setStyleSheet("background-color:rgb(6, 160, 170);")
        self.product_background_label.setText("")
        self.product_background_label.setObjectName("product_background_label")
#         self.product_home_pushButton = QtWidgets.QPushButton(self.frame)
#         self.product_home_pushButton.setGeometry(QtCore.QRect(540, 30, 93, 28))
#         font = QtGui.QFont()
#         font.setFamily("Sans Serif Collection")
#         font.setPointSize(10)
#         self.product_home_pushButton.setFont(font)
#         self.product_home_pushButton.setStyleSheet("border: 5px solid white;\n"
# "background-color: rgb(255, 255, 255);\n"
# "color: rgb(5, 159, 169);\n"
# "border-radius:10px;\n"
# "")
#         icon2 = QtGui.QIcon()
#         icon2.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/icons8-home-1000.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.product_home_pushButton.setIcon(icon2)
#         self.product_home_pushButton.setIconSize(QtCore.QSize(20, 20))
#         self.product_home_pushButton.setObjectName("product_home_pushButton")
        self.product_orders_pushButton = QtWidgets.QPushButton(self.frame)
        self.product_orders_pushButton.setGeometry(QtCore.QRect(780, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.product_orders_pushButton.setFont(font)
        self.product_orders_pushButton.setStyleSheet("border: 5px solid white;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(5, 159, 169);\n"
"border-radius:10px;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/orders.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.product_orders_pushButton.setIcon(icon3)
        self.product_orders_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.product_orders_pushButton.setObjectName("product_orders_pushButton")
        self.product_cart_pushButton = QtWidgets.QPushButton(self.frame)
        self.product_cart_pushButton.setGeometry(QtCore.QRect(900, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.product_cart_pushButton.setFont(font)
        self.product_cart_pushButton.setStyleSheet("border: 5px solid white;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(5, 159, 169);\n"
"border-radius:10px;\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/icons8-cart-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.product_cart_pushButton.setIcon(icon4)
        self.product_cart_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.product_cart_pushButton.setObjectName("product_cart_pushButton")
        self.product_background_label.raise_()
        #self.product_account_pushButton.raise_()
        self.product_b3b3Logo_label.raise_()
        #self.product_home_pushButton.raise_()
        self.product_orders_pushButton.raise_()
        self.product_cart_pushButton.raise_()
        self.product_productbackground1_label.raise_()
        self.product_productprice_label.raise_()
        self.product_productname_label.raise_()
        self.product_productimg_label.raise_()
        self.product_addtocart_pushButton.raise_()
        self.product_productmaindetail1_label.raise_()
        self.product_buy_pushButton.raise_()
        self.frame.raise_()

        self.retranslateUi(product_window)
        QtCore.QMetaObject.connectSlotsByName(product_window)

    def retranslateUi(self, product_window):
        _translate = QtCore.QCoreApplication.translate
        product_window.setWindowTitle(_translate("product_window", "B3B3 - Product"))
        # self.product_productprice_label.setText(_translate("product_window", "50$"))
        # self.product_productname_label.setText(_translate("product_window", "Product name"))
        self.product_addtocart_pushButton.setText(_translate("product_window", "Add To Cart"))
        #self.product_productmaindetail1_label.setText(_translate("product_window", "main details (category, color,etc) dnkvn,ddkvnk lknrlgnnklnrlkngkhswfklghoih oihwoihioshlksnvverhghheo irhgovhnlknvkjlboheghon greoihgihonblkdnbngio irwghlkfnlfvb pgrjkrnklnvkbronvoijrieog\'[ahh;jnbjadbjdbkj vhlfvkj"))
        self.product_buy_pushButton.setText(_translate("product_window", "Buy Now"))
        #self.product_account_pushButton.setText(_translate("product_window", "Account"))
        #self.product_home_pushButton.setText(_translate("product_window", "Home"))
        self.product_orders_pushButton.setText(_translate("product_window", "back"))
        self.product_cart_pushButton.setText(_translate("product_window", "Cart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    product_window = QtWidgets.QWidget()
    ui = Ui_product_window()
    ui.setupUi(product_window,"C:\\pyqt5\\MATELRIAL\\IMG\\Electronics\\Samsung-Galaxy-S23-5G.jpg","vlbd","vlnsd","wlvndv")
    product_window.show()
    sys.exit(app.exec_())
