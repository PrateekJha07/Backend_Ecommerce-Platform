This project is a complete backend implemenation for an ecommerce website.

A person can perform the following tasks in the website:
1. signup customers,vendors and admin 
2. login them using their credentials 
3. A vendor can add items in the database
4. Customer or vendor can search item by the name 
5. A customer can place an order
6. A customer can view all the orders placed
6. An admin can see all the orders placed.
7. A user can get the vendor details along with store and item offerings.

deployment instruction:
To run the project use the following command
1. python3 app.py
After starting the flask application
1. Use curl the commands present in API documentation (zipped along with other files) to run the various API being in the website

Project folder structure:
All the API/JSON are placed under the JSON_api folder
JSON_api:
1.additem.json
2.ddVendor.json
3.getOrders.json
4.login.json
5.placeOrder.json
6.searchitem.json
7.signUp.json

files:
app.py -> contains the code to run the flask app
models.py -> contains the code to run sql query 
Ecommerce.db -> database used in add/edit values
cookies.txt -> contains details of the active sessions 
Api_Documentayion -> Contains detailed instructions to run the APIs using curl
ER diagram -> shows the entity relationships

Design explanation of the database:
1.Every user is a Customer
2.Every Customer is a vendor, one and only one Customer can be a vendor
3.One and only one vendor can be a Customer
4.One vendor should have at least one store, one vendor can have many Stores
5.One store should have at least one vendor. 
6.One store can have zero or many items.
7.Every store should have at least one item.
8.One item can be present one or many stores.
9.Every Order should have at least one item.
10.One order can have many items
11.One item can be placed in one or many orders.
12.One and only one Customer can have zero to many orders. 
