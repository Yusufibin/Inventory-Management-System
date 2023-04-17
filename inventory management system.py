def addrec():
    import mysql.connector
    db=mysql.connector.connect(host="localhost", user="root", passwd="kushi1012", database="inventorymanage")
    c=db.cursor()
    name=input("Enter item name: ")
    p=input("Enter mrp of item: ")
    id1=input("Enter item id: ")
    lrd=input("Enter item last restocking date: yyyy-mm-dd:")
    q=input("Enter quantity of  item as per last restocking date: ")
    str1="("+id1+","+"'"+name+"'"+","+p+","+q+","+"'"+lrd+"'"+");"
    c.execute("insert into item values"+str1)
    db.commit()
    print ("Record added")
    
def updaterec():
    print(" ")
    print("ID**********NAME**********PRICE**********QUANTITY**********LASTDATE_OF_RESTOCKING**********")
    import mysql.connector
    db=mysql.connector.connect(host="localhost", user="root", passwd="jungcock", database="inventorymanage")
    c=db.cursor()
    c.execute("Select * from item;")
    rows=c.fetchall()
    for i in rows:
        for m in i:
            print(m,end='**********')
        print ()
    print (" ")  
toedit=input("Enter item ID of record to edit: ")
    print ("a-to edit name")
    print ("b-to edit price")
    print ("c-to edit item id")
    print ("d-to edit last restocking date")
    print ("e-to edit stock quantity")
    z=input("Enter a-e: ")
    if z=='a':
        n=input("enter new name:")
        str1=("update item set Name='"+n+"' where ID="+toedit+";")
        c.execute(str1)
        print ("Record updated")
        db.commit()
    elif z=='b':
        n=input("enter new price:")
        str1=("update item set Product_price="+n+"where ID="+toedit+";")
        c.execute(str1)
        print ("Record updated")
        db.commit()
    elif z=='c':
        n=input("enter new ID:")
        str1=("update item set ID="+n+"where ID="+toedit+";")
        c.execute(str1)
        print ("Record updated")
        db.commit()
    elif z=='d':
        n=input("enter new last restocking date (yyyy-mm-dd):")
        str1=("update item set Last_restocking_date='"+n+"' where ID="+toedit+";")
        c.execute(str1)
        print ("Record updated")
        db.commit()
    elif z=='e':
        n=input("enter new quantity:")
        str1=("update item set Quantity="+n+"where ID="+toedit+";")
        c.execute(str1)
        print ("Record updated")
        db.commit()
        
def delrec():
    print(" ")
    print("ID**********NAME**********PRICE**********QUANTITY**********LASTDATE_OF_RESTOCKING**********")
    import mysql.connector
    db=mysql.connector.connect(host="localhost", user="root", passwd="kushi1012", database="inventorymanage")
    c=db.cursor()
    c.execute("Select * from item;")
    rows=c.fetchall()
    for i in rows:
        for m in i:
            print(m,end='**********')
        print ()
    print(" ")
    todel=input("Enter item ID of record to delete: ")
    str1=("delete from item where ID="+todel+";")
    c.execute(str1)
    print ("Record deleted")
    db.commit()
    
def showallrecs():
    print(" ")
    print("ID**********NAME**********PRICE**********QUANTITY**********LASTDATE_OF_RESTOCKING**********")
    import mysql.connector
    db=mysql.connector.connect(host="localhost", user="root", passwd="kushi1012", database="inventorymanage")
    c=db.cursor()
    c.execute("Select * from item;")
    rows=c.fetchall()
    for i in rows:
        for m in i:
            print(m,end='**********')
        print ()
    print(" ")

choice=1

while choice!=0:
    print ("************************************")
    print ("1-Add an item")
    print ("2-Remove an item")
    print ("3-Edit specefics of an item")
    print ("4-Show all items")
    print ("5-Help: See all commands again")
    print ("0-Quit")
    print ("************************************")
    choice=int(input("Enter your choice: "))


    if choice==1:
        addrec()
    elif choice==2:
        delrec()
    elif choice==3:
        updaterec()
    elif choice==4:
        showallrecs()
    elif choice==5:
        while choice!=0:
            print ("1-Add an item")
            print ("2-Remove an item")
            print ("3-Edit specefics of an item")
            print ("4-Show all items")
            print ("5-Help: See all commands again")
            print ("0-Quit")
            choice=int(input("Enter your choice: "))
    elif choice==0:
        choice=0
