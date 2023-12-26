from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import data_class as dc
global name
name = 0
dp = sqlite3.connect("Store_dataBase.db")
cr = dp.cursor()

class Ui_cart_window(object):
    r = None
    user_id = None   
    total_sum = 0
    
    @classmethod
    def GetR(cls):
         cr.execute(f"SELECT product_name FROM product,orders where product_id =product_id_fk AND user_id_fk='{cls.user_id}' AND order_state='0'")
         cls.r = cr.fetchall()

    def onButtonClick(self,index):
         if 0 <= index < len(self.frams):
            customer_obj = dc.customer("","","","","")
            widget = self.frams[index]
            widget.setParent(None)
            widget.deleteLater()
            cr.execute(f"SELECT SUM(product_price) FROM product,orders where product_id =product_id_fk AND user_id_fk='{Ui_cart_window.user_id}' AND order_state='0'")
            totalPrice = cr.fetchall()
            st = Ui_cart_window.r[index]
            cr.execute(f"SELECT product_price FROM product where product_name = '{st[0]}'")
            deletedProductPrice = cr.fetchall()
            cr.execute(f"SELECT product_id_fk FROM orders ,product where user_id_fk='{Ui_cart_window.user_id}' AND product_name='{str(Ui_cart_window.r[index][0])}' And product_id=product_id_fk")
            deletedProductId = cr.fetchall()
            customer_obj.remove_from_cart(deletedProductId[0][0], Ui_cart_window.user_id)
            self.total_price_label.setText(f"total price:{totalPrice[0][0]-deletedProductPrice[0][0]}")
            dp.commit()

    def setupUi(self, category1_window,items:list):
        category1_window.setObjectName("category1_window")
        category1_window.resize(1000, 800)
        category1_window.setMinimumSize(QtCore.QSize(1000, 800))
        category1_window.setMaximumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        category1_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        category1_window.setWindowIcon(icon)
        category1_window.setStyleSheet("background-color: rgb(255, 255, 255);")
        #scroll area
        self.scrollArea = QtWidgets.QScrollArea(category1_window)
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
        self.frams = []
        # self.total_price = 0
        for i in range(0,len(items)):
                #fram 
                Ui_cart_window.total_sum = Ui_cart_window.total_sum + items[i][2]
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
              # Use lambda to capture the index

                self.cart_remove_pushButton = QtWidgets.QPushButton(self.frame_4)
                self.cart_remove_pushButton.setText('X')
                self.cart_remove_pushButton.setGeometry(QtCore.QRect(780, 160, 100, 50))
                font = QtGui.QFont()
                font.setPointSize(25)
                self.cart_remove_pushButton.setFont(font)
                self.cart_remove_pushButton.setStyleSheet("border-radius:15PX;\n"
                "background-color: rgb(255, 8, 8);\n"
                "color: white;")
                self.cart_remove_pushButton.clicked.connect(lambda _, index=i: self.onButtonClick(index))
                self.cart_remove_pushButton.setObjectName("cart_remove_pushButton")
                
                self.frams.append(self.frame_4)
        
        for fram1 in self.frams:
                self.verticalLayout.addWidget(fram1)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

#==========================================================================>>>>
        self.cart_purchase_pushButton = QtWidgets.QPushButton(category1_window)
        self.cart_purchase_pushButton.setMinimumSize(QtCore.QSize(120, 40))
        self.cart_purchase_pushButton.setMaximumSize(QtCore.QSize(120, 40))
        self.cart_purchase_pushButton.setText("Purchase")
        self.cart_purchase_pushButton.setGeometry(QtCore.QRect(860, 745, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(14)
        self.cart_purchase_pushButton.setFont(font)
        self.cart_purchase_pushButton.setStyleSheet("color: white;\n"
        "border-radius:20px;\n"
        "background-color: rgb(6, 160, 170);\n"
        "")
        self.cart_purchase_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.cart_purchase_pushButton.setObjectName("cart_purchase_pushButton")

        #total price label
        self.total_price_label= QtWidgets.QLabel(category1_window)
        self.total_price_label.setGeometry(QtCore.QRect(20, 745, 253, 41))
        self.total_price_label.setText(f"total price:{Ui_cart_window.total_sum}")
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(20)
        self.total_price_label.setFont(font)
        self.total_price_label.setStyleSheet("background-color: TRANSPARENT;\n"
        "color: rgb(6, 160, 170);")
        self.total_price_label.setObjectName("total_price_label")
        
        self.frame = QtWidgets.QFrame(category1_window)
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

        self.retranslateUi(category1_window)
        QtCore.QMetaObject.connectSlotsByName(category1_window)

    def retranslateUi(self, category1_window):
        _translate = QtCore.QCoreApplication.translate
        category1_window.setWindowTitle(_translate("category1_window", "B3B3 - Cart"))
        # self.category1_account_pushButton.setText(_translate("category1_window", "Account"))
        self.category1_home_pushButton.setText(_translate("category1_window", "Home"))
        # self.category1_orders_pushButton.setText(_translate("category1_window", "Orders"))
        # self.category1_cart_pushButton.setText(_translate("category1_window", "Cart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    category1_window = QtWidgets.QWidget()
    ui = Ui_cart_window()
    ui.setupUi(category1_window,[["S7S", "TOPPPPPP",'1000'],["HELAL", "3bet",'0.5'],["product1", "detail1",'50'],["product1", "detail1",'50'],["product1", "detail1",'50'],["product1", "detail1",'50'],["product1", "detail1",'50']])
    category1_window.show()
    sys.exit(app.exec_())
