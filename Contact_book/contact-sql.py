User_Id = 0
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="contact")
cur = con.cursor()
class contact_book:
    # insert 
    def insert(s):
        name = input("Enter Name : ")
        email = input("Enter Email : ")
        contact = input("Enter Contact : ")
        city = input("Enter City : ")
        sql = "select * from contacts where Name=%s and Email=%s and Contact=%s and City=%s and User_id=%s"
        cur.execute(sql,(name,email,contact,city,User_Id,))
        row = cur.fetchone()
        if row==None:
            sql = "insert into contacts (Name,Email,Contact,City,User_id) values (%s,%s,%s,%s,%s)"
            cur.execute(sql,(name,email,contact,city,User_Id))
            con.commit()
        else:
            print("This Contact is Already Exist")
    # select all
    def select(s):
        from tabulate import tabulate
        sql = "select Id,Name,Email,Contact,City from contacts where User_id = %s"
        cur.execute(sql,(User_Id,))
        row= cur.fetchall()
        head = ["id", "name","email","Contact","City"]
        print(tabulate(row,headers=head,tablefmt='fancy_grid'))
    # select one 
    def select_one(s):
        id = int(input("Enter id = "))
        sql = "select Id,Name,Email,Contact,City from contacts where User_id = %s and ID = %s"
        cur.execute(sql,(User_Id,id,))
        row= cur.fetchone()
        print(row)
    # Update
    def update(s):
        id = int(input("Enter Update Id : "))
        name = input("Enter Name : ")
        email = input("Enter Email : ")
        contact = int(input("Enter contact : "))
        city = input("Enter city : ")
        sql = "update contacts set Name=%s,Email=%s,Contact=%s,City=%s where User_id = %s and Id = %s"
        cur.execute(sql,(name,email,contact,city,User_Id,id,))
        con.commit()
    #  delete 
    def delete(s):
        id = int(input("Enter delete id = "))
        sql = "delete from contacts where User_id = %s and ID = %s"
        cur.execute(sql,(User_Id,id,))
        con.commit()

class admin:
    def login(s):
        email = input("Enter Email : ")
        password = input("Enter Password : ")
        sql = "select * from admin where Email = %s and Password = %s"
        cur.execute(sql,(email,password))
        row  = cur.fetchone()
        if row==None:
            return 0
        else:
            return row[0]
    def signup(s):
        name = input("Enter Name : ")
        email = input("Enter Emial : ")
        contact = int(input("Enter Contact number : "))
        password = input("Enter Password : ")
        sql = "insert into admin (Name,Email,Contact,Password) values (%s,%s,%s,%s)"
        cur.execute(sql,(name,email,contact,password))
        con.commit()

obj1 = admin()
h = 0
while h!=1:
    print("1. login ")
    print("2. sign up")
    n = int(input("Enter your choice : "))
    if n==1:
        User_Id = obj1.login()
        if User_Id>0:
            h=1
        else:
            print("Enter Valid Email or Password")
    elif n==2:
        obj1.signup()
    else:
        print("Enter Valid choice")

if h==1:
    obj2 = contact_book()
    ch = 1
    while ch!=0:
        print("1. INSERT DATA")
        print("2. DELETE DATA")
        print("3. UPDATE DATA")
        print("4. SELECT ALL DATA")
        print("5. SELECT ONE ROW")
        ch = int(input("Enter Your Choice : "))
        if ch==1:
            obj2.insert()
        elif ch==2:
            obj2.delete()
        elif ch==3:
            obj2.update()
        elif ch==4:
            obj2.select()
        elif ch==5:
            obj2.select_one()
        else :
            print("Enter Valid Choice")
