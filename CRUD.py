import pymysql

mydb = pymysql.connect(host='localhost',user='root',password='',db='ecom')
conn = mydb.cursor()

#create records
def Createrecord():
    tablename = input("Enter table name: ")
    tname = tablename[0:3]
    
    conn.execute(f'CREATE TABLE {tablename} ({tname}_id int PRIMARY KEY,{tname}_name varchar(50),{tname}_phone_number varchar(10),{tname}_city Varchar(20))')
    
    print(f'Table: {tablename}, created sucessfully!')
    
#Show tables in databse
def Showrecord():
    conn.execute(f'SHOW TABLES')
    p = conn.fetchall()
    print(p)
    
    
#Drop table
def Droprecord():
    tablename = input("Enter table name: ")
    
    conn.execute(f'DROP TABLE {tablename}')
    
    print(f'Table: {tablename}, deleted sucessfully!')


#Insert values in table
def Insertrecord():
    tablename = input("Enter table name: ")
    tname = tablename[0:3]
    
    id = input(f'\nEnter {tname}_id :')
    name = input(f'Enter {tname}_name :')
    phone_no = input(f'Enter {tname}_phone_number :')
    city = input(f'Enter {tname}_city :')

    conn.execute(f"INSERT INTO {tablename} VALUES ('"+id+"', '"+name+"', '"+phone_no+"', '"+city+"')")
    
    print(f'Data inserted sucessfully!')
    
# Show table data
def Showdata():
    tablename = input("Enter table name: ")
    conn.execute(f'SELECT * FROM {tablename}')
    p = conn.fetchall()
    print(p)
    

#update table data
def Updatedata():
    tablename = input("Enter table name: ")
    tname = tablename[0:3]
    
    # menu for updating data in table
    print(f'''
             Select data to be updated:               
             1.{tname}_name
             2.{tname}_phone_number
             3.{tname}_city
             4.more than one feild
             ''')
    ch = 10
    ch = int(input('Enter your choice :'))
    if ch == 1:
        id = int(input(f'\nEnter {tname}_id :'))
        name = input(f'\nEnter {tname}_name :')
        conn = mydb.cursor()
        conn.execute(f"UPDATE {tablename} SET {tname}_name = '{name}' WHERE {tablename}.{tname}_id = {id}")
        
    elif ch == 2:
        id = int(input(f'Enter {tname}_id :'))
        phone_no = input(f'Enter {tname}_phone_number :')
        conn = mydb.cursor()
        conn.execute(f"UPDATE {tablename} SET {tname}_phone_number = '{phone_no}' WHERE {tname}_id = {id}")
    
    elif ch == 3:
        id = int(input(f'Enter {tname}_id :'))
        city = input(f'Enter {tname}_city :')
        conn = mydb.cursor()
        conn.execute(f"UPDATE {tablename} SET {tname}_city = '{city}' WHERE {tname}_id = {id}")
          
    elif ch == 4:
        id = int(input(f'\nEnter {tname}_id :'))
        name = input(f'\nEnter {tname}_name :')
        phone_no = input(f'Enter {tname}_phone_number :')
        city = input(f'Enter {tname}_city :')
        conn = mydb.cursor()
        conn.execute(f"UPDATE {tablename} SET {tname}_name = '{name}', {tname}_phone_number = '{phone_no}', {tname}_city = '{city}' WHERE {tablename}.{tname}_id = '"+str(id)+"'")
     
    print('updated')
    conn = mydb.cursor()
    conn.execute(f"select * from {tablename}")
    p = conn.fetchall()
    print(p)
    
#delete data in a table
def Deletedata():
    tablename = input("\nEnter table name: ")
    tname = tablename[0:3]
    id = input(f'\nEnter {tname}_id :')
    
    conn.execute(f"DELETE FROM {tablename} WHERE {tablename}.{tname}_id = '"+id+"'")
    
    
# menu for operations in applixcation
print("Welcome to CRUD application.")
chce = 10 #for defining "chce" variable as integer
while chce > 0:
    print('''
             1.Create Table
             2.Show Tables
             3.Drop Table
             4.Insert Data
             5.Show Data
             6.Update Data
             7.Delete Data
             0.Exit
             ''')
    chce = int(input("Enter your choice: "))
    if chce == 0:
        print("\n======|  Thank You for using CRUD application  |======\n")
    
    else:
        func = [Createrecord,Showrecord,Droprecord,Insertrecord,Showdata,Updatedata,Deletedata]
        op = func[chce -1]()
        print(op)