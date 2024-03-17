User_Id =0
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database ="python")
cur = con.cursor()

class admin:
    def login(s):
        acc_no = input("Enter Account Number : ")
        password = input("Enter Password : ")
        sql = "select * from bank where ACC_NO = %s and Password = %s"
        cur.execute(sql,(acc_no,password))
        row = cur.fetchone()
        if row==None:
            print("Wrong Email or Password")
            return 0
        else:
            return row[0]
    def signup(s,type):
        name = input("Enter Name : ")
        digit = 0
        while digit!=6:
            acc_no = int(input("Enter Account Number : "))
            temp = acc_no                
            digit=0
            while temp !=0:
                temp = temp//10
                digit+=1
        sql = "select * from bank where ACC_NO = %s"
        cur.execute(sql,(acc_no,))
        row = cur.fetchone()
        if row==None:
            password = input("Enter Password : ")
            if type=='saving':
                temp = 20000
            else: 
                temp = 10000
            amount = 0
            while amount<temp:
                amount = int(input("Enter Amount : "))
                if amount<temp:
                    print("Give amount grater than ",temp)
            sql = "insert into bank (Name,ACC_NO,Password,Type,Amount) values (%s,%s,%s,%s,%s)"
            cur.execute(sql,(name,acc_no,password,type,amount))
            con.commit()
        else:
            print("This Contact is Already Exist")
        

class account:
    def __init__(self):
        sql = "select * from bank where ID = %s"
        cur.execute(sql,(User_Id,))
        self.row = cur.fetchone()
        self.amount = self.row[5]
    def diposite(s):
        add = int(input("Enter Ammount to Diposite : "))
        s.amount += add
        sql = "update bank set Amount = %s where ID = %s"
        cur.execute(sql,(s.amount,User_Id,))
        con.commit()
    def Widhdraw(s):
        minus = int(input("Enter Ammount to Widhdraw : "))
        if s.amount>=minus:
            s.amount -= minus
        else:
            print("You Can't widhdraw amount grater than your balance")
        sql = "update bank set Amount = %s where ID = %s"
        cur.execute(sql,(s.amount,User_Id,))
        con.commit()
    # Show Details
    def show(s):
        from tabulate import tabulate
        sql = "select ID,Name,ACC_NO,Type,Amount from bank where ID = %s"
        cur.execute(sql,(User_Id,))
        row= cur.fetchall()
        head = ["id", "name","Account no","Type","Amount"]
        print(tabulate(row,headers=head,tablefmt='fancy_grid'))

# main
obj1 = admin()
cnt = 1
while cnt!=0:
    print("1. login")
    print("2. Sign Up")
    n = int(input("Enter Your Choice : "))
    if n==1:
        print("login")
        User_Id = obj1.login()
        if User_Id>0:
            cnt=0
        else:
            print("Enter Valid Email or Password")
    elif n==2:
        print("sign up ")
        ch=0
        while ch!=1 and ch!=2:
            print("1. Saving")
            print("2. current")
            ch = int(input("Enter choice : "))
            if ch==1:
                print("saving Account")
                obj1.signup('Saving')
            elif ch==2:
                print("current Account")
                obj1.signup('Current')
            else:
                print("Not Valid")
    else :
        print("Enter Valid Number ")

if cnt==0:
    obj2 = account()
    ch=1
    while ch!=0:
        print("1. Deposite ")
        print("2. Withdraw")
        print("3. Show Accout Detail")
        print("0. Exit")
        ch = int(input("Enter Your Choice : ")) 
        if ch==1:
            print("Deposite")
            obj2.diposite()
        elif ch==2:
            print("Withdraw")
            obj2.Widhdraw()
        elif ch==3:
            print("Details")
            obj2.show()
        elif ch==0:
            print()
        else:
            print("Not Valid Choice")