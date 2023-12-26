import sqlite3

dp = sqlite3.connect("Store_dataBase.db")
cr = dp.cursor()

def close_and_save():
    dp.commit()
    dp.close()

# Create table
cr.execute("""
           create table if not exists user(user_id integer primary key AUTOINCREMENT,
                                           user_name varchar(30),
                                           user_type varchar(30),
                                           user_address varchar(50),
                                           user_gender varchar(5),
                                           user_password varchar(30),
                                           user_email varchar(50) UNIQUE
           )""")
cr.execute("""
           create table if not exists product(product_id integer primary key AUTOINCREMENT,
                                              product_name varchar(50),
                                              product_price decimal,
                                              product_discount integer,
                                              product_pices integer,
                                              product_details text,
                                              product_photo text,
                                              category_name_fk varchar(30),
                                              FOREIGN KEY(category_name_fk) REFERENCES category(category_name)
            )""")
cr.execute("""
           create table if not exists orders(product_id_fk integer,
                                             user_id_fk integer,
                                             order_number integer UNIQUE,
                                             orders_date date,
                                             order_state integer,
                                             FOREIGN KEY(user_id_fk) REFERENCES user(user_id),
                                             FOREIGN KEY(product_id_fk) REFERENCES product(product_id)
           )""")
  
cr.execute("""
           create table if not exists category(category_name varchar(30) primary key)
           """)


# Insert Data
cr.execute("""
           INSERT INTO user (user_name, user_type, user_address, user_gender, user_password, user_email) VALUES
           ('John Doe', 'Regular', '123 Main St', 'M', 'pass123', 'john@example.com'),
           ('Jane Doe', 'Admin', '456 Oak St', 'F', 'adminpass', 'jane@example.com'),
           ('Alice Smith', 'Regular', '789 Pine St', 'F', 'userpass', 'alice@example.com'),
           ('Bob Johnson', 'Regular', '101 Elm St', 'M', 'user123', 'bob@example.com'),
           ('Eva Brown', 'Admin', '202 Cedar St', 'F', 'admin123', 'eva@example.com'),
           ('Charlie Green', 'Regular', '303 Maple St', 'M', 'greenpass', 'charlie@example.com'),
           ('Olivia White', 'Admin', '404 Birch St', 'F', 'adminpass', 'olivia@example.com'),
           ('David Black', 'Regular', '505 Walnut St', 'M', 'pass123', 'david@example.com'),
           ('Sophia Grey', 'Regular', '606 Pine St', 'F', 'userpass', 'sophia@example.com'),
           ('Henry Blue', 'Admin', '707 Oak St', 'M', 'adminpass', 'henry@example.com');
           """)

cr.execute("""
                INSERT INTO category (category_name) VALUES
                ('Electronics'),
                ('Clothing'),
                ('Home and Garden'),
                ('Books'),
                ('Toys');
            """)

cr.execute("""
            INSERT INTO product (product_name, product_price, product_discount, product_pices, product_details, product_photo, category_name_fk) VALUES
            ('Smartphone', 599.99, 10, 100, 'High-end smartphone with advanced features', 'path/to/smartphone.jpg', 'Electronics'),
            ('T-shirt', 19.99, 5, 200, 'Cotton T-shirt for everyday wear', 'path/to/tshirt.jpg', 'Clothing'),
            ('Garden Hose', 29.99, 0, 50, 'Durable and flexible garden hose', 'path/to/gardenhose.jpg', 'Home and Garden'),
            ('Java Programming Book', 39.99, 15, 30, 'Comprehensive guide to Java programming', 'path/to/javabook.jpg', 'Books'),
            ('Action Figure', 12.99, 0, 50, 'Collectible action figure for kids', 'path/to/actionfigure.jpg', 'Toys'),
            ('LED TV', 799.99, 20, 50, 'Large-screen LED TV for immersive viewing', 'path/to/ledtv.jpg', 'Electronics'),
            ('Jeans', 34.99, 8, 150, 'Classic denim jeans for casual wear', 'path/to/jeans.jpg', 'Clothing'),
            ('Lawn Mower', 149.99, 0, 20, 'Electric lawn mower for easy lawn maintenance', 'path/to/lawnmower.jpg', 'Home and Garden'),
            ('Mystery Novel', 14.99, 10, 40, 'Engaging mystery novel by a popular author', 'path/to/mysterynovel.jpg', 'Books'),
            ('Board Game', 24.99, 5, 100, 'Family-friendly board game for game nights', 'path/to/boardgame.jpg', 'Toys');
           """)

cr.execute("""
            INSERT INTO orders (product_id_fk, user_id_fk, order_number, orders_date, order_state) VALUES
            (1, 1, 1001, '2023-01-15', 1),
            (2, 3, 1002, '2023-02-20', 2),
            (3, 5, 1003, '2023-03-25', 1),
            (4, 2, 1004, '2023-04-10', 2),
            (5, 4, 1005, '2023-05-05', 1),
            (1, 6, 1006, '2023-06-12', 2),
            (2, 8, 1007, '2023-07-18', 1),
            (3, 10, 1008, '2023-08-23', 2),
            (4, 7, 1009, '2023-09-30', 1),
            (5, 9, 1010, '2023-10-15', 2);
           """)

close_and_save()
