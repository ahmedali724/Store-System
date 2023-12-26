import sqlite3
from datetime import datetime

dp = sqlite3.connect("Store_dataBase.db")
cr = dp.cursor()

def close_and_save():
    dp.commit()
    dp.close()

class user:
    def __init__(self, user_name, user_password, user_email, user_gender):
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email
        self.user_gender = user_gender
    
    def login(self, email, password):
        cr.execute(f"SELECT user_password, user_type  FROM user WHERE user_password = '{password}' AND user_email = '{email}'")
        database_passwordAndType = cr.fetchone()
        if database_passwordAndType == None:
            return 0
        elif (database_passwordAndType[0] == password):
            return database_passwordAndType[1]

class category:
    def __init__(self, category_name):
        self.category_name = category_name
    
    def show_all_products(self, category_name):
        cr.execute(f"""
            SELECT product_name, product_price, product_discount, product_pices, product_photo, product_details, product_id
            FROM product
            WHERE category_name_fk = '{category_name}'
        """)
        items_listOfTuple = cr.fetchall()
        items_listOfList = [list(t) for t in items_listOfTuple]
        return items_listOfList

class product:
    def __init__(self, product_name, product_price, product_numberOfPices, product_discount, product_photo, product_details):
        self.product_name = product_name
        self.product_price = product_price
        self.product_numberOfPices = product_numberOfPices
        self.product_discount = product_discount
        self.product_photo = product_photo
        self.product_details = product_details
    
    def show_product_information(self, product_name):
        cr.execute(f"SELECT product_name, product_price, product_discount, product_pices, product_photo, product_details FROM product WHERE product_name = '{product_name}'")
        items_Tuple = cr.fetchone()
        items_List = list(items_Tuple)
        return items_List
        
class order:
    def __init__(self, user_id, product_id, order_number, order_date, order_state):
        self.user_id = user_id
        self.product_id = product_id
        self.order_number = order_number
        self.order_date = order_date
        self.order_state = order_state

    def make_an_order(self):
        cr.execute(f"UPDATE orders SET order_state = 2 where user_id_fk ='{self.user_id}' AND order_state = 0 ")
        dp.commit()
          
class admin(user):
    def __init__(self, user_name, user_password, user_email, user_gender):
        super().__init__(user_name, user_password, user_email, user_gender)
    
    def add_product(self, product_obj : product, category_obj : category):
        cr.execute(f"INSERT INTO product (product_name, product_price, product_discount, product_pices, product_details, product_photo, category_name_fk) VALUES('{product_obj.product_name}','{product_obj.product_price}','{product_obj.product_discount}','{product_obj.product_numberOfPices}','{product_obj.product_details}','{product_obj.product_photo}', '{category_obj.category_name}')")
        dp.commit()
    
    def remove_product(self, product_obj : product):
        cr.execute(f"DELETE FROM product WHERE product_name = '{product_obj.product_name}'")
        dp.commit()
    
    def show_all_products(self):
        cr.execute("""
                SELECT product_name, product_pices, product_details, product_price, product_discount, product_photo, category_name_fk FROM product
               """)
        items_listOfTuple = cr.fetchall()
        items_listOfList = [list(t) for t in items_listOfTuple]
        return items_listOfList

class delivery(user):
    def __init__(self, user_name, user_password, user_email, user_gender):
        super().__init__(user_name, user_password, user_email, user_gender)

    def deliver_order(self, order_obj: order):
        cr.execute(f"UPDATE orders SET order_state = 1 WHERE order_number = '{order_obj.order_number}'")
        dp.commit()

    def show_all_orders(self):
        cr.execute("""
                SELECT order_number, orders_date, user_name, user_address, order_state FROM orders, user WHERE user_id = user_id_fk
               """)
        orders_listOfTuple = cr.fetchall()
        orders_listOfList = [list(t) for t in orders_listOfTuple]
        return orders_listOfList

class customer(user):
    def __init__(self, user_name, user_password, user_email, user_gender, customer_address):
        super().__init__(user_name, user_password, user_email, user_gender)
        self.customer_address = customer_address

    def registration(self, user_obj : user, customer_address):
        if user_obj.user_name != "" and user_obj.user_gender != "" and user_obj.user_password != "" and user_obj.user_email != "" and customer_address != "":
            cr.execute(f"INSERT INTO user(user_name, user_type, user_address, user_gender, user_password, user_email) VALUES('{user_obj.user_name}','Regular','{customer_address}','{user_obj.user_gender}','{user_obj.user_password}','{user_obj.user_email}')")
            dp.commit()
            return 1
        else:
            return 0
        
    def purchase(self, order_obj: order):
        order_obj.make_an_order()

    def add_product_to_cart(self, order_obj: order):
        cr.execute("select MAX(order_number) from orders")
        maxOrderNumber = cr.fetchall()
        cr.execute(f"INSERT INTO orders (product_id_fk, user_id_fk,order_number, orders_date, order_state) VALUES('{order_obj.product_id}', '{order_obj.user_id}','{maxOrderNumber[0][0]+1}', '{datetime.now().date()}', '0')")
        dp.commit()

    def buy_product(self, order_obj: order):
        cr.execute("select MAX(order_number) from orders")
        maxOrderNumber = cr.fetchall()
        cr.execute(f"INSERT INTO orders (product_id_fk, user_id_fk,order_number, orders_date, order_state) VALUES('{order_obj.product_id}', '{order_obj.user_id}','{maxOrderNumber[0][0]+1}', '{datetime.now().date()}', '2')")
        dp.commit()

    def remove_from_cart(self, deletedProductId, user_id):
        cr.execute(f"DELETE FROM orders where product_id_fk = '{deletedProductId}' AND user_id_fk='{user_id}'")
        dp.commit()

    def show_all_orders(self, user_id):
        cr.execute(f"SELECT product_name, product_details, product_price, product_photo FROM product, orders WHERE user_id_fk = '{int(user_id)}' AND product_id_fk = product_id AND order_state = 1")
        orders_listOfTuple = cr.fetchall()
        orders_listOfList = [list(t) for t in orders_listOfTuple]
        return orders_listOfList
