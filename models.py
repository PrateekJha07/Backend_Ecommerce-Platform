import sqlite3 #importing sqlite3 to work with database
#assigning values to customerID, vendorID, StoreID, itemdID, orderID
Cust_idval=1000
Vendor_idval=1100
Store_idval=1200
item_idval=1331
order_idval=1445

#function to add customers
def add_customer(req_json):
    #try block to handle exceptions
    try:
        #Defining variable as global variable
        global Cust_idval
        #establishing connection to ecommerce database
        conn = sqlite3.connect("Ecommerce.db")
        #creating a cursor for the database
        cur=conn.cursor()
        #SQl query to insert values to customer table in database
        sql_query = "INSERT INTO customer (c_id,c_FirstName,c_LastName,c_Number,c_UserName, c_Password, c_Email, c_Street,c_City, c_State, c_Country,level) values(%d,%s,%s,%d,%s,%s,%s,%s,%s,%s,%s,%d)"%(Cust_idval,req_json["FirstName"],req_json["LastName"],123123123,req_json["username"],req_json["password"],"'pjhaEmail'","'45-Street'","'BBI'","'Ohio'","'US'",req_json["level"])
        #executing the SQl query
        cur.execute(sql_query)
        #commiting changes to the database
        conn.commit()
        #Closing the database connections
        conn.close()
        #incrementing customer ID values by 1 to add new customers to the database
        Cust_idval+=1
    #handling integritingError to enter unique values    
    except(sqlite3.IntegrityError):
        return "Enter a unique customer ID to proceed.\n"
    else: #if there are no error then excute this block  
        if(req_json["level"]==0): #condition to check whether the user is a customer or not
            #if user is a customer -> return these values
            return {"Status":200,"id":Cust_idval-1,"details":"Sign up for customer was successful"}
        else: #if user is an admin -> return these values
            return {"Status":200,"id":Cust_idval-1,"details":"Sign up for admin was successful"}

#function to add vendors
def add_vendor(req_json):
    #try block to handle exceptions
    try:
        #Defining variable as global variable
        global Vendor_idval
        #establishing connection to ecommerce database
        conn = sqlite3.connect("Ecommerce.db")
        #creating a cursor for the database
        cur=conn.cursor()
        #SQl query to insert values to vendor table in database
        sql_query = "INSERT INTO vendor (v_id,v_Name,v_PhoneNumer, v_Email,v_Street,v_City, v_State, v_Country, c_id) values(%d,%s,%d,%s,%s,%s,%s,%s,%d)"%(Vendor_idval,req_json["name"],1231222,req_json["Email"],"'45-Street'","'BBI'","'Ohio'","'US'",1002)
        #executing the SQl query
        cur.execute(sql_query)
        #commiting changes to the database
        conn.commit()
        #Closing the database connections
        conn.close()
         #incrementing vendor ID values by 1 to add new vendors to the database
        Vendor_idval+=1
    #handling integritingError to enter unique values 
    except(sqlite3.IntegrityError): 
        return "Enter a unique vendor_ID to proceed."
    else: #if there are no error then excute this block, return that the vendor was added successully
        return {"Status":200,"id":Vendor_idval-1,"Details":"Vendor added"}

#Function for the users to login
def login(req_json):
    #try block to handle exceptions
    try:
        #establishing connection to ecommerce database
        conn = sqlite3.connect("Ecommerce.db")
         #creating a cursor for the database
        cur=conn.cursor()
        #SQl query to check whether the user exists in the database
        sql_query = ("SELECT * FROM customer WHERE c_UserName=%s AND c_Password=%s")%(req_json["username"],req_json["password"])
        #executing the SQl query and assigning it to a variable
        result = cur.execute(sql_query)
        #fetching one row from the  query
        rows = result.fetchone()
    #block to handle exception is user does not exist in the DB
    except (TypeError):
        return "Please enter valid username and password.\n"
    else: #if there are no error then excute this block
        if (rows): #if there are values in rows then return user added successfully
            return (req_json["username"]+"is successfully logged in.\n")
        else: #if no values in rows -> return to enter valid username and password 
            return "Please enter a valid username and password"

#function to add vendorStoreName
def add_vendorStorename(req_json):
    #defining variables as global variables.
    global Store_idval
    global Vendor_idval
    #try block to handle exceptions
    try:
        #establishing connection to ecommerce database
        conn = sqlite3.connect("Ecommerce.db")
        #creating a cursor for the database
        curr=conn.cursor()
        #SQL query to search for customer in the database
        sql_query="SELECT * FROM customer WHERE c_id=%s"%(req_json["cust_id"])
        #executing the SQl query and assigning it to a variable
        result=curr.execute(sql_query)
        #fetching value of the customer id from the query
        rows = curr.fetchone()[0]
    except(TypeError): #block to handle noneType exception
        return "Only added customers can be made vendors, please sign up as customer first.\n"
    else: #if there are not errors execute this block
        try: #try block to handle exceptions
            #Sql query to insert values to the vendor table in the database
            sql_query="INSERT INTO vendor (v_id,v_Name,v_PhoneNumer, v_Email,v_Street,v_City, v_State, v_Country, c_id) values(%d,%s,%d,%s,%s,%s,%s,%s,%s)"%(Vendor_idval,"'TryVname'",1231222,"'TryVemail'","'45-Street'","'BBI'","'Ohio'","'US'",req_json["cust_id"])
            #executing the SQl query
            curr.execute(sql_query)
            #commiting changes to the database
            conn.commit()
            #Sql query to insert values to the store table in the database
            sql_query="INSERT INTO store (store_id,store_name,store_Category,store_ContactNumber,store_street,store_City,store_State,store_Country,store_capacityUnits,v_id) values (%d,%s,%s,%d,%s,%s,%s,%s,%d,%d)"%(Store_idval,req_json["store_name"],"'Sports'",00000000,"'45-Street'","'HYD'","'Goa'","'India'",400,1000)
            #executing the SQl query
            curr.execute(sql_query)
            #commiting changes to the database
            conn.commit()
            #closing the database connection
            conn.close()
            #incerementing values of vendor and store ID in the database
            Vendor_idval+=1
            Store_idval+=1
        #block to catch and return the exception message 
        except Exception as e:
            return str(e)+"\n"
        else: #if there are no errors then this block executes.
            return{"Status":200,"Store_Name":req_json["store_name"],"Cust_id":req_json["cust_id"],"Vendor_id":Vendor_idval-1,"Details":"The vendor was successfully added"} 

#function to add_item
def add_item(req_json):
    #defining variable as global variable
    global item_idval
    #try block to catch exceptions
    try:
        #establishing connection to ecommerce database
        conn = sqlite3.connect("Ecommerce.db")
        #creating a cursor for the database
        curr = conn.cursor()
        #SQl query to insert items to the item table
        sql_query="INSERT INTO items(item_id, item_Name, item_Category,item_UnitPrice,item_QuantityAvailable, item_Weight, item_Color, item_brand, item_description,v_id,store_id) values (%d,%s,%s,%d,%d,%d,%s,%s,%s,%d,%d)"%(item_idval,req_json["item_name"],"'Try Sports'",req_json["unit_price"],req_json["available_unit"],23,"'red'","'Adidas'","'No description'",req_json["v_id"],req_json["store_id"])
        #executing the SQl query
        curr.execute(sql_query) 
        #commiting changes to the database
        conn.commit()
        #closing the database connection
        conn.close()
        #incerementing values of items ID in the database
        item_idval+=1
    #block to catch and return message  
    except(sqlite3.IntegrityError):
        return "Please enter a unique item ID.\n"
    else: #if there are not errors -> this block executes
        return {"Status":200,"Item_name":req_json["item_name"],"Unit Price":req_json["unit_price"],"store_id":req_json["store_id"],"Details":"Item added successfully"}

#function to search item by name
def search_item_by_name(req_json):
    #try block to catch exception 
    try:
        #establishing connection to ecommerce database
        conn = sqlite3.connect("Ecommerce.db")
        #creating a cursor for the database
        cur = conn.cursor()
        #SQL query to get values from items table
        sql_query =("SELECT * FROM items WHERE v_id=%d and item_name=%s"%(req_json["v_id"],req_json["item_name"])) 
        #executing the SQl query
        cur.execute(sql_query)
    #block to catch error is vendor does not exists
    except(TypeError):
        return "Vendor does not exists, please enter a valid vendor id and item name or add a new vendor.\n"
    #if there are not errors then this blocks excutes
    else:  
        #executing the SQl query to get values
        result=cur.execute(sql_query)
        if(result):  #if values are present in result then return
            return {"Complete item info":list(result)} 
        else: #if no values -> return
            return "No values are present for this vendor, please check and try again.\n"

#function to place orders
def place_orders(req_json):
    #try block to catch exception 
    try:
        #defining variable as global variable
        global order_idval
        #establishing connection to ecommerce database
        conn = sqlite3.connect("Ecommerce.db")
         #creating a cursor for the database
        cur = conn.cursor()
        #Calculating the total amount of the order based on the quantity and unit price
        order_total = req_json["quantity"]*req_json["unit_price"]
        #SQL query to add values to the orders table in DB
        sql_query="INSERT INTO orders (Order_id,Order_Date,order_details,order_Total, paymentMethod, Billing_address, shipping_address, item_id, c_id) values (%d,%s,%s,%d,%s,%s,%s,%d,%d)"%(order_idval,"'1-09-2021'","'no details'",order_total,"'Credit card'","'BBI'","'HYD'",req_json["item_id"],req_json["c_id"])
        #executing the SQl query
        cur.execute(sql_query)
        #commiting changes to the database
        conn.commit() 
        #closing the database connection
        conn.close()
        #incerementing values of order ID in the database
        order_idval+=1
    #block to catch exception and return the message
    except Exception as e:
        return str(e)+"\n"
    else: #block to be executed if there are not errors
        return {"Status":200,"Quantity placed":req_json["quantity"],"Item_id":req_json["item_id"],"c_id":req_json["c_id"]}

#function to get orders by customers
def get_orderByCustomer(req_json):
    #establishing connection to ecommerce database
    conn = sqlite3.connect("Ecommerce.db")
    #creating a cursor for the database
    cur = conn.cursor()
    #DQl query to get orders from table orders in the database
    sql_query = ("SELECT * FROM orders WHERE c_id=%d"%(req_json["Cust_id"]))
    #executing the SQl query
    result = cur.execute(sql_query)
    if(list(result)): #if there are values in result, then return the order details
        sql_query = cur.execute("SELECT * FROM orders WHERE c_id=%d"%(req_json["Cust_id"]))
        return {"Info":list(sql_query)} 
    else: #if there are no values -> return the message
        return "There are no orders for this customer, Please enter a valid Customer ID or place a new order.\n"

#function to get all the orders
def get_all_orders():
    #establishing connection to ecommerce database
    conn = sqlite3.connect("Ecommerce.db")
    #getting rows for connection 
    conn.row_factory = sqlite3.Row
    #creating a cursor for the database
    cur = conn.cursor()
    #executing the SQl query
    cur.execute("select * from orders")
    #fetching all the values extracted from the query
    rows = cur.fetchall()
    #assigning an empty list
    rows_out = []
    #looping all the values fetched from the rows
    for row in rows:
        #appending the values to the empty list based on the index
        rows_out.append(["Order_id-"+str(row[0]),"Order_Date-"+str(row[1]),"Order_details-"+str(row[2]),"Order_Total-"+str(row[3]),"Payment Method-"+str(row[4]),"Billing Address-"+str(row[5]),"Shipping address-"+str(row[6]),"Item_id-"+str(row[7]),"Customer_id-"+str(row[8])])  
    return str(rows_out) #returning the list after adding the values

#function to get all the vendors added to the database
def get_all_vendors():
    #establishing connection to ecommerce database
    conn = sqlite3.connect("Ecommerce.db")
    #getting rows for connection 
    conn.row_factory = sqlite3.Row
    #creating a cursor for the database
    cur = conn.cursor()
    #executing the SQl query
    cur.execute("select * from vendor")
    #fetching all the values extracted from the query
    rows = cur.fetchall()
    #assigning an empty list
    rowsVendor_out = []
    #looping all the values fetched from the rows
    for row in rows:
        #appending the values to the empty list based on the index
        rowsVendor_out.append(["Vendor_id-"+str(row[0]),"vendor_name-"+str(row[1]),"vendor_phone-"+str(row[2]),"Vendor_email-"+str(row[3]),"vendor_street"+str(row[4]),"Vendor_City"+str(row[5]),"Vendor_State-"+str(row[6]),"Vendor_country-"+str(row[7]),"Customer_id-"+str(row[8])])
    return {"Vendors List":str(rowsVendor_out)} #returning the list after adding the values

#functiont to get orders and items for vendors
def get_VendorOrdersItems(v_id):
    #establishing connection to ecommerce database
    conn = sqlite3.connect("Ecommerce.db")
    #creating a cursor for the database
    cur = conn.cursor()
    #executing the SQl query to get items from items table 
    sql_query_items = cur.execute("select*from items where v_id=%d"%(v_id))
    #fetching all the values extracted from the query
    rows_items = cur.fetchall()
    #assigning an empty list to add items
    rows_items_out=[]
    #looping all the values fetched from the rows
    for row in rows_items:
        #appending the values to the empty list based on the index
        rows_items_out.append(["item_id: "+str(row[0]),"item_name: "+str(row[1]),"item_category: "+str(row[2]),"item_UnitPrice: "+str(row[3]),"item_Quantity:"+str(row[4]),"Item_Weight: "+str(row[5]),"Item_color: "+str(row[6]),"Item_brand: "+str(row[7]),"Item_Description: "+str(row[8]),"Vendor_id: "+str(row[9]),"Store_id: "+str(row[10])])
    
    #executing the SQl query to get orders from orders table 
    sql_query_stores = cur.execute("select*from store where v_id= '"+str(v_id)+"'")
    #fetching all the values extracted from the query
    rows_store = cur.fetchall()
     #assigning an empty list to add store details
    rows_store_out=[]
    #looping all the values fetched from the rows
    for row in rows_store:
        #appending the values to the empty list based on the index
        rows_store_out.append(["Store_id: "+str(row[0]),"Store_name: "+str(row[1]),"Store_category: "+str(row[2]),"Store_contact: "+str(row[3]),"Store_street: "+str(row[4]),"Store_city: "+str(row[5]),"Store_state: "+str(row[6]),"Store_country: "+str(row[7]),"Store_capacity:"+str(row[8]),"Vendor_id: "+str(row[9])])
    return {"Items":rows_items_out,"Stores":rows_store_out} #returning the values for items and store