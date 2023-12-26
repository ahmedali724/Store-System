from PyQt5 import QtCore, QtGui, QtWidgets
import data_class as dc
import sqlite3

dp = sqlite3.connect("Store_dataBase.db")
cr = dp.cursor()

class Ui_DelivaryWindow(object):
    def setupUi(self, DelivaryWindow):
        DelivaryWindow.setObjectName("DelivaryWindow")
        DelivaryWindow.resize(1000, 800)
        DelivaryWindow.setMinimumSize(QtCore.QSize(1000, 800))
        DelivaryWindow.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(DelivaryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 130, 831, 491))
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
        self.tableWidget.setColumnCount(4)
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
        self.tableWidget.setHorizontalHeaderItem(2, item)
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
        self.tableWidget.setHorizontalHeaderItem(3, item)
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
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 4, item)
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
        self.login_email_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_email_lineEdit.setGeometry(QtCore.QRect(390, 660, 261, 41))
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
        self.category1_b3b3Logo_label = QtWidgets.QLabel(self.centralwidget)
        self.category1_b3b3Logo_label.setGeometry(QtCore.QRect(20, 0, 80, 80))
        self.category1_b3b3Logo_label.setStyleSheet("background-color: transparent;")
        self.category1_b3b3Logo_label.setText("")
        self.category1_b3b3Logo_label.setPixmap(QtGui.QPixmap("C:/pyqt5/MATELRIAL/IMG/Logo.jpg"))
        self.category1_b3b3Logo_label.setScaledContents(True)
        self.category1_b3b3Logo_label.setObjectName("category1_b3b3Logo_label")
        self.product_buy_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.make_order_checked_button_action(self.login_email_lineEdit.text()))
        self.product_buy_pushButton_3.setGeometry(QtCore.QRect(450, 720, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.product_buy_pushButton_3.setFont(font)
        self.product_buy_pushButton_3.setStyleSheet("QPushButton:hover {\n"
        "color:green;\n"
        "background-color:white;\n"
        "border:3px solid green;\n"
        "border-radius:25px;\n"
        "}\n"
        "QPushButton{\n"
        "background-color:green;\n"
        "color: white;\n"
        "border-radius:25px;\n"
        "}\n"
        "\n"
        "")
        self.product_buy_pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.product_buy_pushButton_3.setObjectName("product_buy_pushButton_3")
        self.category1_background_label = QtWidgets.QLabel(self.centralwidget)
        self.category1_background_label.setGeometry(QtCore.QRect(-10, -10, 1121, 90))
        self.category1_background_label.setStyleSheet("background-color:rgb(6, 160, 170);")
        self.category1_background_label.setText("")
        self.category1_background_label.setObjectName("category1_background_label")
        self.category1_background_label.raise_()
        self.tableWidget.raise_()
        self.login_email_lineEdit.raise_()
        self.category1_b3b3Logo_label.raise_()
        self.product_buy_pushButton_3.raise_()
        DelivaryWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(DelivaryWindow)
        QtCore.QMetaObject.connectSlotsByName(DelivaryWindow)
        delivery_obj = dc.delivery("","","","")
        orders_listOfList = delivery_obj.show_all_orders()
        orders_listOfListWithoutChecked = []
        for record in orders_listOfList:
            if record[-1] == 2:
                orders_listOfListWithoutChecked.append(record)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(orders_listOfListWithoutChecked):
            self.tableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number,QtWidgets.QTableWidgetItem(str(data)))

    def retranslateUi(self, DelivaryWindow):
        _translate = QtCore.QCoreApplication.translate
        DelivaryWindow.setWindowTitle(_translate("DelivaryWindow", "B3B3 - Delivery"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("DelivaryWindow", "Order"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DelivaryWindow", "Order Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DelivaryWindow", "Order Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DelivaryWindow", "Customer Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("DelivaryWindow", "Customer Address"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.login_email_lineEdit.setText(_translate("DelivaryWindow", "Order Number"))
        self.product_buy_pushButton_3.setText(_translate("DelivaryWindow", "Delivered"))

    def make_order_checked_button_action(self, order_number):
        delivery_obj = dc.delivery("","","","")
        order_obj = dc.order("","",order_number,"","")
        delivery_obj.deliver_order(order_obj)
        orders_listOfList = delivery_obj.show_all_orders()
        orders_listOfListWithoutChecked = []
        for record in orders_listOfList:
            if record[-1] == 2:
                orders_listOfListWithoutChecked.append(record)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(orders_listOfListWithoutChecked):
            self.tableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number,QtWidgets.QTableWidgetItem(str(data)))
        
        msg = QtWidgets.QMessageBox() 
        msg.setIcon(QtWidgets.QMessageBox.Information) 
        msg.setText(f"Order {order_number} Delivered Successfully") 
        msg.setWindowTitle("Info") 
        retval = msg.exec_() 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DelivaryWindow = QtWidgets.QMainWindow()
    ui = Ui_DelivaryWindow()
    ui.setupUi(DelivaryWindow)
    DelivaryWindow.show()
    sys.exit(app.exec_())
