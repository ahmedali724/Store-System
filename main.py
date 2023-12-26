global k
k = 7
import categories, cart, login, register, home, product, admin, delivery, order
import data_class as dc
from PyQt5.QtWidgets import QStackedWidget
from PyQt5 import QtWidgets,QtCore, QtGui
from functools import partial
import sqlite3
from datetime import datetime

dp = sqlite3.connect("Store_dataBase.db")
cr = dp.cursor()

class Ui_category1_window(object):
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
        self.scrollArea.setGeometry(QtCore.QRect(-10, 90, 1011, 711))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1009, 709))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frams = []
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
                self.category1_productdetail3_label_3.setGeometry(QtCore.QRect(210, 130, 500, 31))
                self.category1_productdetail3_label_3.setText(f"Discount: {items[i][2]}%, Pices: {items[i][3]}")
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
                self.category1_productprice3_label_3.setText(f"{items[i][1]}$")
                font = QtGui.QFont()
                font.setFamily("Sans Serif Collection")
                font.setPointSize(25)
                self.category1_productprice3_label_3.setFont(font)
                self.category1_productprice3_label_3.setStyleSheet("background-color: TRANSPARENT;\n"
                "color: rgb(6, 160, 170);")
                self.category1_productprice3_label_3.setObjectName("category1_productprice3_label_3")
                self.category1_productprice3_label_3.setAlignment(QtCore.Qt.AlignCenter)
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
                self.category1_productimg3_label_3.setPixmap(QtGui.QPixmap(items[i][4][1:-1]))
                self.category1_productimg3_label_3.setScaledContents(True)
                self.category1_productimg3_label_3.setObjectName("category1_productimg3_label_3")
                #------------>>>>>>>>>>>>
                self.product_buy_pushButton = QtWidgets.QPushButton(self.frame_4)
                self.product_buy_pushButton.setGeometry(QtCore.QRect(780, 170, 131, 51))
                self.product_buy_pushButton.setText("Show Details")
                font = QtGui.QFont()
                font.setFamily("Sans Serif Collection")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.product_buy_pushButton.setFont(font)
                self.product_buy_pushButton.setStyleSheet("\n"
                "background-color:rgb(5, 159, 169);\n"
                "color: white;\n"
                "border-radius:25px;\n"
                "")
                self.product_buy_pushButton.setIconSize(QtCore.QSize(30, 30))                 #product_img  #product_name #product_price #product_details 
                self.product_buy_pushButton.clicked.connect(lambda _, product_info=[items[i][4][1:-1],items[i][0],items[i][1],items[i][5],items[i][-1]]: show_product_info(product_info[0],product_info[1],product_info[2],product_info[3],product_info[4]))
                self.product_buy_pushButton.setObjectName("product_buy_pushButton")
                self.frams.append(self.frame_4)

        for fram1 in self.frams:
                self.verticalLayout.addWidget(fram1)

                
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

#==========================================================================>>>>
        self.frame = QtWidgets.QFrame(category1_window)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1111, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.category1_b3b3Logo_label = QtWidgets.QLabel(self.frame)
        self.category1_b3b3Logo_label.setGeometry(QtCore.QRect(30, 10, 80, 80))
        self.category1_b3b3Logo_label.setStyleSheet("background-color: transparent;")
        self.category1_b3b3Logo_label.setText("")
        self.category1_b3b3Logo_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"))
        self.category1_b3b3Logo_label.setScaledContents(True)
        self.category1_b3b3Logo_label.setObjectName("category1_b3b3Logo_label")
        self.category1_b3b3Logo_label.mousePressEvent = open_home_window1
        self.category1_background_label = QtWidgets.QLabel(self.frame)
        self.category1_background_label.setGeometry(QtCore.QRect(0, 0, 1121, 90))
        self.category1_background_label.setStyleSheet("background-color:rgb(6, 160, 170);")
        self.category1_background_label.setText("")
        self.category1_background_label.setObjectName("category1_background_label")
        self.category1_orders_pushButton = QtWidgets.QPushButton(self.frame)
        #back Action button
        self.category1_orders_pushButton.clicked.connect(open_categories_window1)
        self.category1_orders_pushButton.setGeometry(QtCore.QRect(780, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.category1_orders_pushButton.setFont(font)
        self.category1_orders_pushButton.setStyleSheet("border: 5px solid white;\n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(5, 159, 169);\n"
        "border-radius:10px;\n"
        "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/orders.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.category1_orders_pushButton.setIcon(icon3)
        self.category1_orders_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.category1_orders_pushButton.setObjectName("category1_orders_pushButton")
        self.category1_cart_pushButton = QtWidgets.QPushButton(self.frame)
        self.category1_cart_pushButton.setGeometry(QtCore.QRect(900, 30, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.category1_cart_pushButton.setFont(font)
        self.category1_cart_pushButton.setStyleSheet("border: 5px solid white;\n"
        "background-color: rgb(255, 255, 255);\n"
        "color: rgb(5, 159, 169);\n"
        "border-radius:10px;\n"
        "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/icons8-cart-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.category1_cart_pushButton.setIcon(icon4)
        self.category1_cart_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.category1_cart_pushButton.setObjectName("category1_cart_pushButton")
        self.category1_background_label.raise_()
        self.category1_b3b3Logo_label.raise_()
        self.category1_orders_pushButton.raise_()
        self.category1_cart_pushButton.raise_()

        self.retranslateUi(category1_window)
        QtCore.QMetaObject.connectSlotsByName(category1_window)
        
    def retranslateUi(self, category1_window):
        _translate = QtCore.QCoreApplication.translate
        category1_window.setWindowTitle(_translate("category1_window", "B3B3 - Category"))
        self.category1_orders_pushButton.setText(_translate("category1_window", "back"))
        self.category1_cart_pushButton.setText(_translate("category1_window", "Cart"))

def Increment():
   globals()['k'] = k + 1
   return k

def open_categories_window(eve):
    stacked_widget.setCurrentIndex(1)

def open_categories_window1():
    stacked_widget.setCurrentIndex(1)

def open_home_window():
    stacked_widget.setCurrentIndex(2)

def open_home_window1(eve):
    stacked_widget.setCurrentIndex(2)

def open_cart_window():
    stacked_widget.setCurrentIndex(6)

def open_login_window():
    stacked_widget.setCurrentIndex(0)

def open_registration_window():
    stacked_widget.setCurrentIndex(3)

def open_order_window(eve):
    stacked_widget.setCurrentIndex(7)

def purchase(user_id):
    customer_obj = dc.customer("","","","","")
    order_obj = dc.order(user_id,"","","","")
    customer_obj.purchase(order_obj)
    msg = QtWidgets.QMessageBox() 
    msg.setIcon(QtWidgets.QMessageBox.Information) 
    msg.setText("Orders Purchased Successfully") 
    msg.setWindowTitle("Info") 
    retval = msg.exec_() 

def choose_between_admin_delivery_customer():
    #cart screen object
    cartWindow = QtWidgets.QWidget()
    ui = cart.Ui_cart_window()
    orderWindow = QtWidgets.QMainWindow()
    ui1 = order.Ui_orderWindow()
    if login.user_type_shared == 'Regular':
        cr.execute(f"SELECT user_id FROM user WHERE user_email = '{ui2.login_email_lineEdit.text()}'")
        user_id = cr.fetchall()
        if user_id != []:
            customer_obj = dc.customer("","","","","")
            product.Ui_product_window.user_id = int(user_id[0][0])
            cr.execute(f"SELECT product_name,product_details,product_price,product_photo,product_id FROM  product,orders WHERE product_id = product_id_fk AND user_id_fk='{int(user_id[0][0])}' AND order_state = 0")
            l = cr.fetchall()
            orders_listOfList = customer_obj.show_all_orders(user_id[0][0])
            ui.setupUi(cartWindow,l)
            ui.cart_purchase_pushButton.clicked.connect(lambda:purchase(cart.Ui_cart_window.user_id))
            ui.category1_home_pushButton.clicked.connect(open_home_window)
            stacked_widget.addWidget(cartWindow)
            ui1.setupUi(orderWindow, orders_listOfList)
            ui1.category1_home_pushButton.clicked.connect(open_home_window)
            stacked_widget.addWidget(orderWindow)
            cart.Ui_cart_window.user_id = int(user_id[0][0]) 
            cart.Ui_cart_window.GetR()                     
    if login.user_type_shared == 'Admin':
        stacked_widget.setCurrentIndex(4)
    elif login.user_type_shared == 'Regular':
        stacked_widget.setCurrentIndex(2)
    elif login.user_type_shared == 'Delivery':
        stacked_widget.setCurrentIndex(5)

def open_admin_window():
    stacked_widget.setCurrentIndex(4)

def open_delivary_window():
    stacked_widget.setCurrentIndex(5)

def open_Electronics_window(eve):
    category1_window = QtWidgets.QWidget()
    ui = Ui_category1_window()
    category_obj = dc.category("")
    items_listOfList = category_obj.show_all_products("Electronics")#category name
    ui.setupUi(category1_window, items_listOfList)
    ui.category1_orders_pushButton.clicked.connect(open_categories_window)
    stacked_widget.addWidget(category1_window)
    stacked_widget.setCurrentIndex(Increment())
    

def open_Clothing_window(eve):
    category1_window = QtWidgets.QWidget()
    ui = Ui_category1_window()
    category_obj = dc.category("")
    items_listOfList = category_obj.show_all_products("Clothing")#category name
    ui.setupUi(category1_window, items_listOfList)
    ui.category1_orders_pushButton.clicked.connect(open_categories_window)
    stacked_widget.addWidget(category1_window)
    stacked_widget.setCurrentIndex(Increment())
    
def open_Books_window(eve):
    category1_window = QtWidgets.QWidget()
    ui = Ui_category1_window()
    category_obj = dc.category("")
    items_listOfList = category_obj.show_all_products("Books")#category name
    ui.setupUi(category1_window, items_listOfList)
    ui.category1_orders_pushButton.clicked.connect(open_categories_window)
    stacked_widget.addWidget(category1_window)
    stacked_widget.setCurrentIndex(Increment())
    
def open_Toys_window(eve):
    category1_window = QtWidgets.QWidget()
    ui = Ui_category1_window()
    category_obj = dc.category("")
    items_listOfList = category_obj.show_all_products("Toys")#category name
    ui.setupUi(category1_window, items_listOfList)
    ui.category1_orders_pushButton.clicked.connect(open_categories_window)
    stacked_widget.addWidget(category1_window)
    stacked_widget.setCurrentIndex(Increment())
    
def open_Home_and_Garden_window(eve):
    category1_window = QtWidgets.QWidget()
    ui = Ui_category1_window()
    category_obj = dc.category("")
    items_listOfList = category_obj.show_all_products("Home and Garden")#category name
    ui.setupUi(category1_window, items_listOfList)
    ui.category1_orders_pushButton.clicked.connect(open_categories_window)
    stacked_widget.addWidget(category1_window)
    stacked_widget.setCurrentIndex(Increment())
    
def add_product_to_cart(product_id,user_id):
        customer_obj = dc.customer("","","","","")
        order_obj = dc.order(user_id, product_id, "", "", "")
        customer_obj.add_product_to_cart(order_obj)
        msg = QtWidgets.QMessageBox() 
        msg.setIcon(QtWidgets.QMessageBox.Information) 
        msg.setText("Product Added To Cart Successfully") 
        msg.setWindowTitle("Info") 
        retval = msg.exec_() 
        
def buy_product(product_id,user_id):
        customer_obj = dc.customer("","","","","")
        order_obj = dc.order(user_id, product_id, "", "", "")
        customer_obj.buy_product(order_obj)
        msg = QtWidgets.QMessageBox() 
        msg.setIcon(QtWidgets.QMessageBox.Information) 
        msg.setText("Product Purchased Successfully") 
        msg.setWindowTitle("Info") 
        retval = msg.exec_() 

def show_product_info(product_img,product_name,product_price,product_details,product_id):
    product_window = QtWidgets.QWidget()
    ui = product.Ui_product_window()
    ui.setupUi(product_window,product_img,product_name,str(product_price),product_details)
    ui.product_orders_pushButton.clicked.connect(open_categories_window1)
    ui.product_b3b3Logo_label.mousePressEvent = open_home_window1
    ui.product_cart_pushButton.clicked.connect(lambda:open_cart_window())
    stacked_widget.addWidget(product_window)
    stacked_widget.setCurrentIndex(Increment()) 
    ui.product_addtocart_pushButton.clicked.connect(lambda:add_product_to_cart(product_id,cart.Ui_cart_window.user_id))
    ui.product_buy_pushButton.clicked.connect(lambda:buy_product(product_id,cart.Ui_cart_window.user_id))

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    
    stacked_widget = QStackedWidget()

    #categories screen object
    category_window = QtWidgets.QMainWindow()
    ui = categories.Ui_category_window()
    ui.setupUi(category_window)
    ui.category_category1_label.mousePressEvent = open_Electronics_window
    ui.category_category2_label.mousePressEvent = open_Clothing_window
    ui.category_category3_label.mousePressEvent = open_Books_window
    ui.category_category4_label.mousePressEvent = open_Electronics_window#edit to Gaming
    ui.category_category5_label.mousePressEvent = open_Toys_window
    ui.category_category6_label.mousePressEvent = open_Electronics_window#edit to sales
    ui.category_category7_label.mousePressEvent = open_Home_and_Garden_window
    ui.category_category8_label.mousePressEvent = open_Electronics_window#edit to sports
    ui.category_cart_pushButton.clicked.connect(open_cart_window)
    ui.category_b3b3Logo_label.mousePressEvent = open_home_window1
    
    #home screen object
    home_window = QtWidgets.QDialog()
    ui = home.Ui_home_window()
    ui.setupUi(home_window)
    ui.home_categories_label.mousePressEvent = open_categories_window
    ui.home_order_label.mousePressEvent = open_order_window
    ui.category1_cart_pushButton.clicked.connect(open_cart_window)
    
    #login screen object
    login_window = QtWidgets.QMainWindow()
    ui2 = login.Ui_login_window()
    ui2.setupUi(login_window)
    ui2.login_login_pushButton.clicked.connect(choose_between_admin_delivery_customer)
    ui2.login_signup_pushButton.clicked.connect(open_registration_window)

    #regisregistration screen object
    registration_window = QtWidgets.QMainWindow()
    ui = register.Ui_registration_window()
    ui.setupUi(registration_window)
    ui.register_signin_pushButton.clicked.connect(open_login_window)
  
    #admin screen object
    AdminWindow = QtWidgets.QMainWindow()
    ui = admin.Ui_AdminWindow()
    ui.setupUi(AdminWindow)

    #delivery screen object
    DelivaryWindow = QtWidgets.QMainWindow()
    ui = delivery.Ui_DelivaryWindow()
    ui.setupUi(DelivaryWindow)

    stacked_widget.addWidget(login_window)          #0
    stacked_widget.addWidget(category_window)       #1
    stacked_widget.addWidget(home_window)           #2
    stacked_widget.addWidget(registration_window)   #3
    stacked_widget.addWidget(AdminWindow)           #4
    stacked_widget.addWidget(DelivaryWindow)        #5
         
    stacked_widget.setFixedHeight(800)
    stacked_widget.setFixedWidth(1000)
    stacked_widget.show()

    sys.exit(app.exec_())