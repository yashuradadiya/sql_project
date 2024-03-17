m = []
class result():
    def __init__(self):
        import mysql.connector
        self.con = mysql.connector.connect(host="localhost",user="root",password="",database="Python")
        self.cur = self.con.cursor()
    # Data Add
    def add_data(s):
        s.name = input("Enter Name : ")
        for i in range(5):
            m.append(int(input("Enter marks of sub "+str(i+1)+" : ")))
        s.total = 0
        cnt = 0
        s.min = m[0]
        s.max = m[0]
        for i in m:
            s.total += i
            if s.min>i:
                s.min = i
            if s.max<i:
                s.max = i
            if i<33:
                cnt += 1
        if cnt==0:
            s.per = s.total/5
            s.result = "PASS"
        elif cnt<=2:
            s.per = 0
            s.result = "ATKT"
        else :
            s.per = 0
            s.result = "FAIL"
        if s.per>=90:
            s.grade = "dist."
        elif s.per>=70:
            s.grade = "firlst Class"
        elif s.per>=50:
            s.grade = "Second Class"
        elif s.per>=33:
            s.grade = "Third Class"
        else :
            s.grade = "-"
    # Insert
    def insert(s):
        s.add_data()
        sql = "insert into Result (name,sub1,sub2,sub3,sub4,sub5,total,per,min,max,result,grade) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        s.cur.execute(sql,(s.name,m[0],m[1],m[2],m[3],m[4],s.total,s.per,s.min,s.max,s.result,s.grade))
        s.con.commit()
    # Update 
    def update(s):
        id = int(input("Enter Update Id = "))
        s.add_data()
        sql = "update Result set name=%s , sub1=%s , sub2=%s , sub3=%s ,sub4=%s , sub5=%s , total=%s ,per=%s , min=%s , max=%s , result=%s , grade=%s where id = %s"
        s.cur.execute(sql,(s.name,m[0],m[1],m[2],m[3],m[4],s.total,s.per,s.min,s.max,s.result,s.grade,id,))
        s.con.commit()
    def delete(s):
        id = int(input("Enter Delete Id : "))
        sql = "DELETE FROM Result WHERE id = %s"
        s.cur.execute(sql,(id,))
    def select(s):
        from tabulate import tabulate
        sql = "select * from Result"
        s.cur.execute(sql)
        row = s.cur.fetchall()
        head = ["id", "name" ,"sub1","sub2","sub3","sub4","sub5","total","per","min","max","result","grade"]
        print(tabulate(row,headers=head,tablefmt='fancy_grid'))
    def select_one(s):
        from tabulate import tabulate
        id = int(input("Enter Select id : "))
        sql = "select * from Result where ID = %s"
        s.cur.execute(sql,(id,))
        row = s.cur.fetchone()
        head = ["id", "name" ,"sub1","sub2","sub3","sub4","sub5","total","per","min","max","result","grade"]
        print(tabulate(row,headers=head,tablefmt='fancy_grid'))
        
obj = result()
ch = 1
while ch!=0:
    print("1. INSERT DATA")
    print("2. DELETE DATA")
    print("3. UPDATE DATA")
    print("4. SELECT ALL DATA")
    print("5. SELECT ONE ROW")
    print("0. Exit")
    ch = int(input("Enter Your Choice : "))
    if ch==1:
        obj.insert()
    elif ch==2:
        obj.delete()
    elif ch==3:
        obj.update()
    elif ch==4:
        obj.select()
    elif ch==5:
        obj.select_one()
    elif ch==0:
        print("Exit")
    else:
        print("Enter Vlid Choice")
