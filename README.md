# Store Management System (SMS)

## Table of Contents
1. [Introduction](#introduction)

   1.1 [Folder Structure](#folder-structure)
2. [System Overview](#system-overview)
3. [Target Users](#target-users)
4. [Document Revisions](#document-revisions)
5. [System Scope](#system-scope)
6. [Glossary](#glossary)
7. [User Roles and Objectives](#user-roles-and-objectives)
8. [User Requirements](#user-requirements)
9. [Constraints](#constraints)
10. [System Architecture](#system-architecture)
11. [Functional Requirements](#functional-requirements)
12. [Interface Requirements](#interface-requirements)
13. [Non-functional Requirements](#non-functional-requirements)
14. [System Models and Diagrams](#system-models-and-diagrams)

## Introduction<a name="introduction"></a>
Welcome to the Store Management System (SMS) project! This README file provides an overview of the system, its purpose, and guidelines for developers, administrators, and users.

### Folder Structure<a name="folder-structure"></a>
Before you begin, ensure that the "pyqt5" folder is added to the "C" directory. This folder should include all images used in the project.

## System Overview<a name="system-overview"></a>
The SMS aims to automate and streamline the shopping process, providing a user-friendly platform for customers, administrators, and delivery personnel. The system integrates customer interactions, product management, order fulfillment, and administrative control.

## Target Users<a name="target-users"></a>
- **Customer:** Can search for products, add/remove items to/from the cart, place orders, and view order history.
- **Administrator:** Manages products, controls the database, and ensures the smooth operation of the system.
- **Delivery Personnel:** Responsible for delivering orders and viewing order details.

## Document Revisions<a name="document-revisions"></a>
| Version | Author | Description | Date       |
|---------|--------|-------------|------------|
| 0.1     | B3B3   | Initial     | 30-11-2023 |
| 0.2     | B3B3   | Use-Case    | 11-12-2023 |
| 0.3     | B3B3   | Class-Diagram| 17-12-2023 |
| 0.4     | B3B3   | Sequence-Diagram | 21-12-2023 |

## System Scope<a name="system-scope"></a>
The SMS is designed to automate the shopping process, catering to customers, administrators, and delivery personnel. It includes functionalities such as customer management, product inventory control, and order fulfillment.

## Glossary<a name="glossary"></a>
- **FOEHU:** Faculty of Engineering, Helwan University.
- **B3B3:** Team Name.
- **SMS:** Store Management System.
- **SQLite3:** Database Used in System.

## User Roles and Objectives<a name="user-roles-and-objectives"></a>
### System Engineer (Developer)
- **Objectives:** Gain experience in software engineering and development.

### Customer
- **Objectives:** Save time and money on shopping, find easy ways to meet their needs.

### Delivery Personnel
- **Objectives:** Earn a salary from delivering orders.

### Administrator
- **Objectives:** Find a more comfortable way to control the store, identify issues.

## User Requirements<a name="user-requirements"></a>
### System Functions
1. Add products to categories.
2. Remove products.
3. Show all products.
4. Add to cart.
5. Remove from cart.
6. View all orders.
7. Login.
8. Registration.
9. Confirm buying orders.
10. Check if the order is delivered.
11. Deliver orders.

## Constraints<a name="constraints"></a>
- **User Authentication Constraint:** Ensure secure user authentication within the desktop application.
- **Data Security Constraint:** Safeguard user data and sensitive information stored on the local machine.

## System Architecture<a name="system-architecture"></a>
Refer to the provided System Architecture diagram (Figure 1).

## Functional Requirements<a name="functional-requirements"></a>
### Add Product to Categories
- Administrators can add new products with details to existing or new categories.

### Remove Product
- Administrators can remove products from the store.

### Show All Products
- Administrators can access and display all product details in the store.

### Add to Cart
- Registered users can create an order for products.

### Remove from Cart
- Registered users can remove a product from the cart.

### View All Orders
- Registered users can view all past orders.

### Login
- Users can log into the system with a valid email and password.

### Registration
- Users can register for a new account with necessary information.

### Confirm Buying Order
- Users can confirm and finalize orders in the cart.

### Check If the Order Is Delivered
- Users can check the status of their orders.

### Deliver Order
- Delivery personnel can confirm the delivery of an order.

## Interface Requirements<a name="interface-requirements"></a>
### User Interface
Refer to the provided interface screenshots in the documentation.

### Software Interface
- Database access using SQLite3 server.

## Non-functional Requirements<a name="non-functional-requirements"></a>
1. **Performance Requirements:** The desktop application should respond quickly to user interactions.
2. **Reliability Requirements:** The application should be consistently available, minimizing disruptions.
3. **Usability Requirements:** The user interface should adhere to industry usability standards.
4. **Security Requirements:** User information should be hidden from all except the administrator.

## System Models and Diagrams<a name="system-models-and-diagrams"></a>
Refer to the provided Use-Case, Class, ER, and Sequence diagrams in the documentation.
