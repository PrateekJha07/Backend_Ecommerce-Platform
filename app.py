#import all the required libararies
from flask import Flask, jsonify,request,session 
#import models to access fucntions from models.py file
import models

#creating a flask instance
app = Flask(__name__)

#allocating secret key for sessions 
app.config["SECRET_KEY"] = "secretkey"

@app.route("/") #defining route for the home page
def home():  
    return "Welcome to Ecommerce website" #return value for home the page 

@app.route("/AddCustomer",methods=["POST","GET"]) #defining the route to add customers
def add_customer(): 
    #condition to check if the request method is correct or not
    if (request.method=="POST"): 
        data = request.get_json() #creating a json object to get values from signUp.json
        level=data["level"] #Getting the value of level from the json object 
        #condition to check whether the customer is admin/customer, level 2 -> admin, level 0 -> customer 
        if(level==2 or level==0): 
            cust_response=models.add_customer(data) #calling add customer function from models to signup users as admin/customer
            return jsonify(cust_response) #returning signup.json value after the user in successfully added
        elif(level==1): #condition to check in the user is suppose to be added as a vendor, level 1 -> vendor
            vendor_response=models.add_vendor(data) #calling add vendor function from models to signup users as vendor
            return jsonify(vendor_response) #returning signup.json value after the user in successfully added 
        else: #else condition to return value for invalid level
            return "Please enter a valid level to add customer/vendor/admin."
    else: #else condition to return value for invalid request 
        return "Please enter a valid request to add customer/vendor/admin.\n"

@app.route("/Login",methods=["GET","POST"]) #defining the route to login as user
def Login():
    #if condition to check if the request method is correct or not
    if(request.method=="POST"): 
        data = request.get_json() #creating a json object to get values from login.json
        username= data["username"] #getting the username from json object
        session["USERNAME"]=username #assigning username to flask session  
        return models.login(request.get_json()) #calling and returning values from login function in models
    else: #else condition to return value for invalid request 
        return "Enter a valid request to login.\n"

@app.route("/AddVendor",methods=["POST","GET"]) #defining route to add vendor
def add_vendorStorename():
    #if condition to check if the request method is correct or not
    if(request.method=="POST"):
        return models.add_vendorStorename(request.get_json()) #calling add_vendorStorename to add vendor and store, returning values after adding.
    else: #else condition to return value for invalid request 
        return "Please enter a valid request to add vendor.\n"

@app.route("/Additem",methods=["POST","GET"]) #defining route to add item
def add_item():
    #if condition to check if the request method is correct or not
    if(request.method=="POST"):
        #if condition to check whether the session active or not 
        if(session.get("USERNAME") is not None): 
            #if the session is active -> call add item from models to add items in the database. return values after adding the items
            return models.add_item(request.get_json())
        else: #if the session in not active -> returning statment to login
            return "PLease login to add items.\n"
    else: #else condition to return value for invalid request 
        return "Please enter a valid request to add items.\n"

@app.route("/SearchItemByName",methods=["GET"]) #defining the route to search item by name
def search_item_by_name():
    #if condition to check if the request method is correct or not
    if(request.method=="GET"): 
        #if condition to check whether the session active or not 
        if(session.get("USERNAME") is not None):
             #if the session is active -> call search_item_by_name from models to search for items as vendor, returning the searched values
            return models.search_item_by_name(request.get_json())
        else: #if the session in not active -> returning statment to login
            return "Please login to view items.\n"
    else: #else condition to return value for invalid request
        return "Please enter a valid request to search item by name"

@app.route("/Placeorders",methods=["POST","GET"]) #defining the route to place orders.
def place_order():
    #if condition to check if the request method is correct or not
    if(request.method=="POST"):
        #if condition to check whether the session active or not 
        if(session.get("USERNAME") is not None):
            #if the session is active -> call place_orders from models to place the order, return values after placing the order
            return models.place_orders(request.get_json())
        else: #if the session in not active -> returning statment to login
            return "Please login to place orders.\n"
    else: #else condition to return value for invalid request
        return "Please enter a valid request to place orders\n"

@app.route("/GetOrdersByCustomer",methods=["GET","POST"]) #defining the route to get orders by customers
def get_ordersByCustomer():
    #if condition to check if the request method is correct or not
    if(request.method=="GET"):
        #if condition to check whether the session active or not 
        if(session.get("USERNAME") is not None):    
            #if the session is active -> call get_OrdersByCustomer to get the orders, return the values after fetching the orders
            return models.get_orderByCustomer(request.get_json())
        else: #if the session in not active -> returning statment to login
            return "Please login to view the orders.\n"
    else: #else condition to return value for invalid request
        return "Enter a valid request to get the orders,\n"

@app.route("/GetAllOrders/<level>",methods=["GET","POST"]) #defining the route to get all orders
def get_all_orders(level):
    #if condition to check if the request method is correct or not
    if(request.method=="GET"):     
        #if condition to check whether the user is an admin or not  
        if(level=="2"):
            #if condition to check whether the session active or not
            if(session.get("USERNAME") is not None):
                #if the session is active -> call get_all_order from models and return all values of the order 
                return jsonify(models.get_all_orders())
            else: #if the session in not active -> returning statment to login
                return "Please login as admin to view to the orders.\n"
        else: #if user in not an admin -> return please login as admin
            return "Sorry, only admins can view all the orders.\nPlease login as admin to view orders.\n"
    else: #else condition to return value for invalid request
        return "Please enter a valid request to view the orders.\n"

@app.route("/GetVendors",methods=["GET","POST"]) #defining the route to get vendors
def get_vendors():
    #if condition to check if the request method is correct or not
    if(request.method=="GET"):
        #if condition to check whether the session active or not
        if(session.get("USERNAME") is not None):
             #if the session is active -> call get_all_vendors from models and return the values
            return jsonify(models.get_all_vendors())
        else: #if the session is not active -> returning statment to login
            return "Please login to get details of the vendors.\n"
    else: #else condition to return value for invalid request
        return "Please entet a valid request to view the vendors.\n"

@app.route("/GetOrdersItemsVendors/<v_id>",methods=["POST","GET"]) #defining the route to get orders and items from vendor ID
def get_VendorOrdersItems(v_id):
    #if condition to check if the request method is correct or not
    if(request.method == "GET"):
         #if condition to check whether the session active or not
        if(session.get("USERNAME") is not None):
            #if the session is active -> call get_VendorOrdersByItem from models to get the orders and items, returning value after getting the values
            return jsonify(models.get_VendorOrdersItems(int(v_id)))
        else: #if the session is not active -> returning statment to login
            return "Please login to view the stores and items.\n"
    else: #else condition to return value for invalid request
        return "Please enter a valid request to view stores and items.\n"

@app.route("/Logout",methods=["GET","POST"]) #defining the route to logout
def Logout():
    #if condition to check if the request method is correct or not
    if(request.method=="GET"):
        #if condition to check whether the session active or not
        if (session.get("USERNAME") is not None):
            #Remove session in the user is active
            session.pop("USERNAME",None)
            #return statement after logging out the user successfully
            return "The user is successfully logged out.\n"
        else: #if the session is not active -> return the user is already logged out
            return "The user is already logged out.\n"
    else: #else condition to return value for invalid request
        return "Please enter a valid request to logout.\n"


#running the flask app
if __name__ == "__main__":
    app.run(debug=True)