from PyQt5 import QtCore, QtGui, QtWidgets
import data_class as dc
import sqlite3

dp = sqlite3.connect("Store_dataBase.db")
cr = dp.cursor()

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.product_buy_pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.save_product_button_action())
        self.product_buy_pushButton_4.setEnabled(False)
        self.product_buy_pushButton_4.setGeometry(QtCore.QRect(120, 730, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.product_buy_pushButton_4.setFont(font)
        self.product_buy_pushButton_4.setStyleSheet("QPushButton:disabled {\n"
        "color:#cbcbcb;\n"
        "border:3px solid #cbcbcb;\n"
        "border-radius:25px;\n"
        "}\n"
        "QPushButton:enabled {\n"
        "background-color:rgb(5, 159, 169);\n"
        "color: white;\n"
        "border-radius:25px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "color:rgb(5, 159, 169);\n"
        "background-color:white;\n"
        "border:3px solid rgb(5, 159, 169);\n"
        "border-radius:25px;\n"
        "}")
        self.product_buy_pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.product_buy_pushButton_4.setObjectName("product_buy_pushButton_4")
        self.product_buy_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_product_button_action())
        self.product_buy_pushButton.setGeometry(QtCore.QRect(120, 670, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.product_buy_pushButton.setFont(font)
        self.product_buy_pushButton.setStyleSheet("QPushButton:disabled {\n"
"color:#cbcbcb;\n"
"border:3px solid #cbcbcb;\n"
"border-radius:25px;\n"
"}\n"
"QPushButton:enabled {\n"
"background-color:rgb(5, 159, 169);\n"
"color: white;\n"
"border-radius:25px;\n"
"}\n"
"QPushButton:hover {\n"
"color:rgb(5, 159, 169);\n"
"background-color:white;\n"
"border:3px solid rgb(5, 159, 169);\n"
"border-radius:25px;\n"
"}\n"
"")
        self.product_buy_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.product_buy_pushButton.setObjectName("product_buy_pushButton")
        self.category1_b3b3Logo_label = QtWidgets.QLabel(self.centralwidget)
        self.category1_b3b3Logo_label.setGeometry(QtCore.QRect(20, 10, 80, 80))
        self.category1_b3b3Logo_label.setStyleSheet("background-color: transparent;")
        self.category1_b3b3Logo_label.setText("")
        self.category1_b3b3Logo_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"))
        self.category1_b3b3Logo_label.setScaledContents(True)
        self.category1_b3b3Logo_label.setObjectName("category1_b3b3Logo_label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 140, 831, 491))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QHeaderView::section {\n"
"    background-color: #06a0aa ;\n"
"    color: white;\n"
"    border: none;\n"
"    border-right: 1px solid white;\n"
"}\n"
"QTableView {\n"
"     border: 2px solid #06a0aa;\n"
"}\n"
"QTableView::item:focus{\n"
"    border: 2px solid #06a0aa;\n"
"    color: #06a0aa;\n"
"    background-color: rgb(212, 212, 212);\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: rgb(188, 224, 235);\n"
"}\n"
" QScrollBar::handle:vertical {\n"
"    background: rgb(71, 153, 176);\n"
" }\n"
"QScrollBar:horizontal {\n"
"    background:rgb(188, 224, 235);\n"
"}\n"
" QScrollBar::handle:horizontal {\n"
"    background: #06a0aa;\n"
" }")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(6, 160, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(6, 160, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(6, 159, 169))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(6, 160, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(189)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(35)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.category1_background_label = QtWidgets.QLabel(self.centralwidget)
        self.category1_background_label.setGeometry(QtCore.QRect(-10, 0, 1121, 90))
        self.category1_background_label.setStyleSheet("background-color:rgb(6, 160, 170);")
        self.category1_background_label.setText("")
        self.category1_background_label.setObjectName("category1_background_label")
        self.product_buy_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_product_button_action(self.login_email_lineEdit.text()))
        self.product_buy_pushButton_3.setGeometry(QtCore.QRect(760, 730, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.product_buy_pushButton_3.setFont(font)
        self.product_buy_pushButton_3.setStyleSheet("QPushButton:hover {\n"
"color:red;\n"
"background-color:white;\n"
"border:3px solid red;\n"
"border-radius:25px;\n"
"}\n"
"QPushButton{\n"
"background-color:red;\n"
"color: white;\n"
"border-radius:25px;\n"
"}\n"
"\n"
"")
        self.product_buy_pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.product_buy_pushButton_3.setObjectName("product_buy_pushButton_3")
        self.login_email_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_email_lineEdit.setGeometry(QtCore.QRect(690, 670, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(13)
        self.login_email_lineEdit.setFont(font)
        self.login_email_lineEdit.setStyleSheet("background-color:white;\n"
"border: 5px solid rgb(6, 160, 170);\n"
"color: rgb(6, 160, 170);\n"
"border-radius:10px;\n"
"padding-left:10px;")
        self.login_email_lineEdit.setObjectName("login_email_lineEdit")
        self.category1_background_label.raise_()
        self.product_buy_pushButton_4.raise_()
        self.product_buy_pushButton.raise_()
        self.category1_b3b3Logo_label.raise_()
        self.tableWidget.raise_()
        self.product_buy_pushButton_3.raise_()
        self.login_email_lineEdit.raise_()
        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

        admin_objj = dc.admin("","","","")
        items_listOfList = admin_objj.show_all_products()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(items_listOfList):
            self.tableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number,QtWidgets.QTableWidgetItem(str(data)))

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "AdminWindow"))
        self.product_buy_pushButton_4.setText(_translate("AdminWindow", "Save"))
        self.product_buy_pushButton.setText(_translate("AdminWindow", "Add Product"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("AdminWindow", "Product 1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdminWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdminWindow", "Product Pices"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AdminWindow", "Product Details"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AdminWindow", "Product Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("AdminWindow", "Product Discount"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("AdminWindow", "Product Image"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("AdminWindow", "Category name"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("AdminWindow", "gfhgfh"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("AdminWindow", "sfddsfds"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("AdminWindow", "ghgfh"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("AdminWindow", "gfhgfh"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.product_buy_pushButton_3.setText(_translate("AdminWindow", "Delete Product"))
        self.login_email_lineEdit.setText(_translate("AdminWindow", "Product Name"))

    def add_product_button_action(self):
        self.product_buy_pushButton_4.setEnabled(True)
        self.product_buy_pushButton.setEnabled(False)
        cr.execute('SELECT COUNT(*) FROM product')
        number_of_rows = cr.fetchone()[0]
        self.tableWidget.insertRow(number_of_rows)

    def save_product_button_action(self):
        self.product_buy_pushButton_4.setEnabled(False)
        self.product_buy_pushButton.setEnabled(True)
        cr.execute('SELECT COUNT(*) FROM product')
        number_of_rows = cr.fetchone()[0]
        user_input = []
        for col_number in range(0, 7):
                item = self.tableWidget.item(number_of_rows, col_number)
                user_input.append(item.text())
        product_obj = dc.product("","","","","","")
        category_obj = dc.category("")
        admin_obj = dc.admin("","","","")
        product_obj.product_name = user_input[0]
        product_obj.product_numberOfPices = user_input[1]
        product_obj.product_details = user_input[2]
        product_obj.product_price = user_input[3]
        product_obj.product_discount = user_input[4]
        product_obj.product_photo = user_input[5]
        category_obj.category_name = user_input[6]
        admin_obj.add_product(product_obj, category_obj)

        msg = QtWidgets.QMessageBox() 
        msg.setIcon(QtWidgets.QMessageBox.Information) 
        msg.setText(f"Product {product_obj.product_name} Added Successfully") 
        msg.setWindowTitle("Info") 
        retval = msg.exec_() 
    
    def remove_product_button_action(self, product_name):
        admin_obj = dc.admin("","","","")
        product_obj = dc.product("","","","","","")
        product_obj.product_name = product_name
        admin_obj.remove_product(product_obj)
        items_listOfList = admin_obj.show_all_products()

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(items_listOfList):
            self.tableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number,QtWidgets.QTableWidgetItem(str(data)))
        
        msg = QtWidgets.QMessageBox() 
        msg.setIcon(QtWidgets.QMessageBox.Information) 
        msg.setText(f"Product {product_obj.product_name} Deleted Successfully") 
        msg.setWindowTitle("Info") 
        retval = msg.exec_() 
        
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminWindow()
    ui.setupUi(AdminWindow)
    AdminWindow.show()
    sys.exit(app.exec_())
