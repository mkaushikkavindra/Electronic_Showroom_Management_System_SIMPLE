def establish_connection () :
    global con
    global cursor
    import mysql.connector as mysql
    con = mysql.connect (host = "localhost", user = "root", password = "sjps2006", database = "brox_digitals")
    if con.is_connected() :
        print ("Connection successfully established!\n")
    else :
        print ("Connection is not established!\n")
    cursor = con.cursor()

establish_connection ()

from prettytable import PrettyTable
import datetime

def title () :
    print ("Welcome to BROX Digitals!")

#Login Module
def login () : 
    username, password = "admin", "admin123"
    username1 = input ("User Name : ")
    password1 = input ("Password : ")
    if (username1 == username) and (password1 == password) :
        print ("Logged in succesfully")
    else :
        print ("Error, Try Again!")

#Menu Module
def dashboard () :
    print ("1) Employee Registration")
    print ("2) Employee Reports")
    print ("3) Edit Employee Details")
    print ("4) Delete Employee Details")
    print ("5) Add New Products") #First Time Entry
    print ("6) View Products")
    print ("7) Edit Products")
    print ("8) Delete Products")
    print ("9) Sales")
    print ("10) View Sales Report")
    print ("11) Exit")

#Date Modules
def date_of_birth () :
    global dob
    dob1 = input('Enter date of birth (in DD-MM-YYYY format) : ')
    day, month, year = map(str, dob1.split('-'))
    dob = year + month + day
def date_of_joining () :
    global doj
    doj1 = input('Enter date of joining (in DD-MM-YYYY format) : ')
    day, month, year = map(str, doj1.split('-'))
    doj = year + month + day

#Employee Registration Module
def employee_registration () :
    empname = input ("Enter employee name : ")
    gender = input ("Gender : ")
    date_of_birth ()
    mobile_no = int (input ("Enter mobile number : "))
    email_id = input ("Enter email ID : ")
    address = input ("Enter address : ")
    date_of_joining ()
    profile = input ("Enter profile : ")
    shifttype = input ("Enter shift type (Morning/Evening) :")
    query = "insert into employees (employee_name, gender, date_of_birth, mobile_number, email_id, address, date_of_joining, profile, shift) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (empname, gender, dob, mobile_no, email_id, address, doj, profile, shifttype)
    cursor.execute(query, values)
    con.commit()
    print ("Successfully Added!")
    #Display empno here from the table (AutoGenerated)

#Employee Reports Module
def employee_reports () :
    cursor.execute ("select * from employees")
    emplo = cursor.fetchall()
    employees = PrettyTable()
    employees.field_names = ["Employee ID", "Employee Name", "Gender", "Date of Birth", "Mobile Number", "Email ID", "Address", "Date of Joining" , "Profile", "Shift Type"]
    for empp in emplo :
        employees.add_row([empp [0], empp [1], empp [2], empp [3], empp [4], empp [5], empp [6], empp [7], empp [8], empp [9]])
    print (employees)

#Edit Employee Details
def edit_employees () :
    print ('''What to Update?
---> employee_name [1]  
---> date_of_birth [2] 
---> mobile_number [3]
---> email_id [4] 
---> address [5] 
---> date_of_joining [6] 
---> profile [7] 
---> shift [8] ''')
    enter_empid = int (input ("Enter Employee ID : "))
    choice = int (input ("Enter your choice : "))
    if choice == 1 :
        newempname = input ("Enter new employee name : ")
        query1 = "update employees set employee_name = (%s) where employee_id = (%s)"
        values1 = (newempname, enter_empid)
        cursor.execute (query1, values1)
        con.commit ()
        print ("Employee Name Updated")
    elif choice == 2 :
        dob2 = input('Enter new Date of Birth (in DD-MM-YYYY format) : ')
        day, month, year = map(str, dob2.split('-'))
        newdob = year + month + day
        query2 = "update employees set date_of_birth = (%s) where employee_id = (%s)"
        values2 = (newdob, enter_empid)
        cursor.execute (query2, values2)
        con.commit ()
        print ("Date of Birth Updated")
    elif choice == 3 :
        newmobileno = int(input ("Enter new mobile number : "))
        query3 = "update employees set mobile_number = (%s) where employee_id = (%s)"
        values3 = (newmobileno, enter_empid)
        cursor.execute (query3, values3)
        con.commit ()
        print ("Mobile Number Updated!")
    elif choice == 4 :
        newemailid = input ("Enter new email id : ")
        query4 = "update employees set email_id = (%s) where employee_id = (%s)"
        values4 = (newemailid, enter_empid)
        cursor.execute (query4, values4)
        con.commit ()
        print ("E-Mail ID Updated!")
    elif choice == 5 :
        newaddress = input ("Enter new address : ")
        query5 = "update employees set address = (%s) where employee_id = (%s)"
        values5 = (newaddress, enter_empid)
        cursor.execute (query5, values5)
        con.commit ()
        print ("Address Updated!")
    elif choice == 6 :
        doj2 = input('Enter new Date of Joining (in DD-MM-YYYY format) : ')
        day, month, year = map(str, doj2.split('-'))
        newdoj = year + month + day
        query6 = "update employees set date_of_joining = (%s) where employee_id = (%s)"
        values6 = (newdoj, enter_empid)
        cursor.execute (query6, values6)
        con.commit ()
        print ("Date of Joining Updated")
    elif choice == 7 :
        newprofile = input ("Enter new profile : ")
        query7 = "update employees set profile = (%s) where employee_id = (%s)"
        values7 = (newprofile, enter_empid)
        cursor.execute (query7, values7)
        con.commit ()
        print ("Profile Updated!")
    elif choice == 8 :
        newshift = input ("Enter new shift (Morning/Evening) : ")
        query8 = "update employees set shift = (%s) where employee_id = (%s)"
        values8 = (newshift, enter_empid)
        cursor.execute (query8, values8)
        con.commit ()
        print ("Shift Updated!")
    else :
        print ("ERROR, Try Again!")

#delete employees
def delete_employees () :
    empiddelete = int (input ("Enter the employee id to delete : "))
    query9 = "delete from employees where employee_id = (%s)"
    values9 = (empiddelete,)
    cursor.execute (query9, values9)
    con.commit ()
    print ("Employee details deleted successfully!")

#Add New Products
def addproducts () :
    cursor.execute ("select product_name from products")
    productlist = cursor.fetchall ()
    prodid = input ("Enter Product ID : ")
    prodname = input ("Enter product name : ")
    prodtype = input ("Enter product type : ")
    prodbrand = input ("Enter product brand : ")
    cost = int (input ("Enter cost (in Rs.) : "))
    modelno = input ("Enter model no : ")
    warranty = int (input ("Enter warranty (in months) : "))
    quantity = int (input ("Enter the quantity : "))
    query10 = "insert into products (product_id, product_name, product_type, product_brand, cost_in_rs, model_no, warranty_in_months, quantity_available) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    values10 = (prodid, prodname, prodtype, prodbrand, cost, modelno, warranty, quantity)
    cursor.execute(query10, values10)
    con.commit()
    print ("Product Successfully Added!")
    #Display empno here from the table (AutoGenerated)

#View Products
def viewproducts () :
    cursor.execute ("select * from products")
    productdetails = cursor.fetchall()
    producttable = PrettyTable()
    producttable.field_names = ["Product ID", "Product Name", "Product Type", "Product Brand", "Cost (In Rs.)", "Model No.", "Warranty (In Months)", "Quantity Available"]
    for prod in productdetails :
        producttable.add_row([prod [0], prod [1], prod [2], prod [3], prod [4], prod [5], prod [6], prod [7]])
    print (producttable)

#Edit Products
def editproducts () :
    print ('''What to Update?
---> Product Name [1]  
---> Product Type [2] 
---> Product Brand [3]
---> Cost (In Rs.) [4] 
---> Model No. [5] 
---> Warranty [6] 
---> Quantity [7]''')
    enter_prodid = input ("Enter Product ID : ")
    choice1 = int (input ("Enter your choice : "))
    if choice1 == 1 :
        newprodname = input ("Enter new product name : ")
        query11 = "update products set product_name = (%s) where product_id = (%s)"
        values11 = (newprodname, enter_prodid)
        cursor.execute (query11, values11)
        con.commit ()
        print ("Product Name Updated")
    elif choice1 == 2 :
        newprodtype = input ("Enter new product type : ")
        query12 = "update products set product_type = (%s) where product_id = (%s)"
        values12 = (newprodtype, enter_prodid)
        cursor.execute (query12, values12)
        con.commit ()
        print ("Product Type Updated")
    elif choice1 == 3 :
        newprodbrand = input ("Enter new product brand : ")
        query13 = "update products set product_brand = (%s) where product_id = (%s)"
        values13 = (newprodbrand, enter_prodid)
        cursor.execute (query13, values13)
        con.commit ()
        print ("Product Brand Updated")
    elif choice1 == 4 :
        newprodcost = int (input ("Enter new product cost : "))
        query14 = "update products set cost_in_rs = (%s) where product_id = (%s)"
        values14 = (newprodcost, enter_prodid)
        cursor.execute (query14, values14)
        con.commit ()
        print ("Product Cost Updated")
    elif choice1 == 5 :
        newmodno = input ("Enter new model no : ")
        query15 = "update products set model_no = (%s) where product_id = (%s)"
        values15 = (newmodno, enter_prodid)
        cursor.execute (query15, values15)
        con.commit ()
        print ("Model No. Updated")
    elif choice1 == 6 :
        newwarranty = int (input ("Enter new warranty period (in months) : "))
        query16 = "update products set warranty_in_months = (%s) where product_id = (%s)"
        values16 = (newwarranty, enter_prodid)
        cursor.execute (query16, values16)
        con.commit ()
        print ("Warranty Period Updated")
    elif choice1 == 7 :
        print ('''MANAGE QUANTITY
1) Add Quantity
2) Deduct Quantity
3) Replace Quantity''')
        cursor.execute ("select quantity_available from products where product_id = (%s)", (enter_prodid,))
        org = cursor.fetchone ()
        originalquantity = org [0]
        subchoice = int (input ("Enter your choice : "))
        if subchoice == 1 :
            addno = int (input ("How many items to add? --> "))
            editedquantity1 = originalquantity + addno
            cursor.execute ("update products set quantity_available = (%s) where product_id = (%s)", (editedquantity1, enter_prodid))
            con.commit ()
            print ("Quantity Updated")
        if subchoice == 2 :
            deductno = int (input ("How many items to deduct? --> "))
            editedquantity2 = originalquantity - deductno
            cursor.execute ("update products set quantity_available = (%s) where product_id = (%s)", (editedquantity2, enter_prodid))
            con.commit ()
            print ("Quantity Updated")
        if subchoice == 3 :
            replaceno = int (input ("Enter New Quantity --> "))
            cursor.execute ("update products set quantity_available = (%s) where product_id = (%s)", (replaceno, enter_prodid))
            con.commit ()
            print ("Quantity Updated")
    else :
        print ("ERROR, Try Again!")

#Delete Product
def delete_product () :
    prodiddelete = input ("Enter the product id to delete : ")
    query17 = "delete from products where product_id = (%s)"
    values17 = (prodiddelete,)
    cursor.execute (query17, values17)
    con.commit()
    print ("Product details deleted successfully!")

#Sales
def invoice_date () :
    global invdate
    invd1 = datetime.date.today()
    year = invd1.strftime("%y")
    month = invd1.strftime ("%m")
    date = invd1.strftime ("%d")
    invdate = year + month + date

#View the Invoice
def viewinvoice () :
    cursor.execute ("select * from sales_report")
    salesreport = cursor.fetchall()
    totalinvoices = 0
    for ch in salesreport :
        totalinvoices += 1
    index = totalinvoices - 1
    invoii = salesreport [index]
    invoice = PrettyTable()
    invoice.field_names = ["Invoice ID", "Invoice Date", "Product ID", "Product Name", "Product Type", "Product Brand", "Quantity", "Total Cost", "Model No.", "Warranty (In Months)", "Customer Name", "Customer Mobile No", "Customer Email ID", "Customer Address"]
    invoice.add_row([invoii [0], invoii [1], invoii [2], invoii [3], invoii [4], invoii [5], invoii [6], invoii [7], invoii [8], invoii [9], invoii [10], invoii [11], invoii [12], invoii [13]])
    print (invoice)

#Billing Process
def sales () :
    invoice_date ()
    prodidd = input ("Enter Product ID : ")
    cursor.execute ("select quantity_available from products where product_id = (%s)", (prodidd,))
    tqa = cursor.fetchone ()
    totalquantityavailable = tqa[0]
    cursor.execute ("select product_name, product_type, product_brand, model_no, warranty_in_months, cost_in_rs from products where product_id = (%s)", (prodidd,))
    proddetailss = cursor.fetchone ()
    prodnamee, prodtypee, prodbrandd, modelnoo, warantyyy, cost = proddetailss [0], proddetailss [1], proddetailss [2], proddetailss [3], proddetailss [4], proddetailss [5]
    quantitypurchased = int (input ("Enter the quantity : "))
    cursor.execute ("update products set quantity_available = quantity_available - (%s) where product_id = (%s)", (quantitypurchased, prodidd))
    remquan = totalquantityavailable - quantitypurchased
    con.commit ()
    if remquan <= 0 :
        print ("Exceeding the remaining stock", totalquantityavailable, "items remaining")
    elif totalquantityavailable == 0 :
        print ("Out of Stock!")
    else :
        totalcost = quantitypurchased * cost
        customername = input ("Enter customer name : ")
        customermobileno = int (input ("Enter customer mobile number : "))
        customeremailid = input ("Enter customer E-Mail ID : ")
        customeraddress = input ("Enter customer address : ")
        query19 = "insert into sales_report (invoice_date, product_id, product_name, product_type, product_brand, quantity_purchased, total_cost_in_rs, model_no, warranty_in_months, customer_name, customer_mobileno, customer_emailid, customer_address) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values19 = (invdate, prodidd, prodnamee, prodtypee, prodbrandd, quantitypurchased, totalcost, modelnoo, warantyyy, customername, customermobileno, customeremailid, customeraddress)
        cursor.execute(query19, values19)
        con.commit()
        print ("Invoice created successfully!")
        print ()
        print ("                                        BROX DIGITALS")
        print ("Invoice :\n")
        viewinvoice ()

#Sales Report
def viewsales () :
    cursor.execute ("select * from sales_report")
    srp = cursor.fetchall()
    salesreport = PrettyTable()
    salesreport.field_names = ["Invoice ID", "Invoice Date", "Product ID", "Product Name", "Product Type", "Product Brand", "Quantity", "Total Cost", "Model No.", "Warranty (In Months)", "Customer Name", "Customer Mobile No", "Customer Email ID", "Customer Address"]
    for a in srp :
        salesreport.add_row([a [0], a [1], a [2], a [3], a [4], a [5], a [6], a [7], a [8], a [9], a [10], a [11], a [12], a [13]])
    print ("SALES REPORT : ")
    print (salesreport)

#application
def application () :
    option = int (input ("Enter the option : "))
    if option == 1 :
        employee_registration ()
    elif option == 2 :
        employee_reports ()
    elif option == 3 :
        edit_employees ()
    elif option == 4 :
        delete_employees ()
    elif option == 5 :
        addproducts ()
    elif option == 6 :
        viewproducts ()
    elif option == 7 :
        editproducts ()
    elif option == 8 :
        delete_product ()
    elif option == 9 :
        sales ()
    elif option == 10 :
        viewsales ()
    elif option == 11 :
        print ("Bye, have a nice day!")
    else :
        print ("ERROR, Try again!")

#Interface
title ()
login ()
dashboard ()
application ()
