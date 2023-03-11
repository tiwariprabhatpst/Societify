import mysql.connector
import datetime
from dateutil.relativedelta import relativedelta
comp = mysql.connector.connect(user='root', password='Prabhat@0811',
                              host='localhost',
                              database='Societify')

def add_house():
    house_no = input("Enter your House Number: ")
    type = input("Enter the type of your house: ")
    mycursor = comp.cursor()
    
    print("Now enter the details of the owner: ")
    name = input("Enter Owner's Name: ")
    contact = input("Enter Owner's Contact Number: ")
    vehicles = int(input("Number of vehicles for parking: "))
    members = int(input("Enter the number of family members: "))

    sql = "INSERT INTO house_owner (House_no,Name,Contact,No_of_Vehicles,No_of_family_members) VALUES (%s, %s, %s, %s, %s)"
    val2 = (house_no,name,contact,vehicles,members)
    mycursor.execute(sql,val2)

    sql = "INSERT INTO house (House_no,Type) VALUES (%s, %s)"
    val = (house_no,type)
    mycursor.execute(sql,val)

    comp.commit()

def show_all_activities():
    mycursor = comp.cursor()
    mycursor.execute("SELECT Activity_id,Activity_name, Pricing FROM activity")
    myresult = mycursor.fetchall()

    for x in myresult:
        for b in x:
            print(b,end='\t\t')
        print()

def show_activity(act):
    mycursor = comp.cursor()
    mycursor.execute("SELECT Activity_id,Activity_name, Pricing FROM activity")
    myresult = mycursor.fetchall()
    for x in myresult:
        if act in x:
            return x[2]
            for b in x:
                print(b,end='\t\t')
            print()

def get_activity_id(act):
    mycursor = comp.cursor()
    mycursor.execute("SELECT Activity_id,Activity_name, Pricing FROM activity")
    myresult = mycursor.fetchall()
    for x in myresult:
        if act in x:
            return x[0]

def get_activity_price(act):
    mycursor = comp.cursor()
    mycursor.execute("SELECT Activity_id,Activity_name, Pricing FROM activity")
    myresult = mycursor.fetchall()
    for x in myresult:
        if act in x:
            return x[2]

def visitor_in():
    vehicle_no = input("Enter Vehicle Number If any: ")
    in_time = str(datetime.datetime.now().strftime("%H:%M:%S")) + " "+ str(datetime.date.today())
    name = input("Name of the visitor: ")
    house_no = input("Enter the House Number: ")

    mycursor = comp.cursor()

    sql = "INSERT INTO visitor (Vehicle_no,in_time,Name,House_no) VALUES (%s, %s, %s, %s)"
    val = (vehicle_no,in_time,name,house_no)
    mycursor.execute(sql,val)
    comp.commit()

def visitor_out():
    out_time = str(datetime.datetime.now().strftime("%H:%M:%S")) + " "+ str(datetime.date.today())
    name = input("Name of the visitor: ")
    house_no = input("Enter the House Number: ")
    mycursor = comp.cursor()
    sql = "INSERT INTO visitor (out_time) VALUES ({}) WHERE Name = {}".format(out_time,name)
    
    mycursor.execute(sql)
    comp.commit()

def membership():
    var = 0
    lst = ["GYM","Swimming","Club House","Sports"]
    print("Now enter the details of the Member: ")
    name = input("Enter Member's Name: ")
    contact = input("Enter Member's Contact Number: ")
    while(True):
        mem_name = input("Enter the name of the activity: ")
        if mem_name in lst:
            break
    
    h_no = input("Enter your house number: ")
    mem_id = get_activity_id(mem_name)
    mem_price = int(get_activity_price(mem_name))

    while(True):
        print("Press 1 if you want monthly subscription :")
        print("Press 2 if you want qaurterly subscription :")
        print("Press 3 if you want annually subscription :")
        var = int(input())
        if(var == 1):
            var = 1
            break
        elif(var == 2):
            var = 3
            break
        elif(var == 3):
            var = 12
            break

        print("Enter valid input")

    mycursor = comp.cursor()

    start_date = datetime.date.today()
    end_date = datetime.date.today() + relativedelta(months=+ var)
    sql = "INSERT INTO membership(Mem_name,Contact,Start_date,End_date,House_no,Activity_id) VALUES (%s, %s, %s, %s, %s, %s)"
    val2 = (name,contact,start_date,end_date,h_no,mem_id)
    mycursor.execute(sql,val2)
    comp.commit()

    print("Amount To be paid is: ")
    print(mem_price * var)

def Committee_members():
    name = input("Enter the name: ")
    desig = input("Enter the designation of the person: ")
    h_no = input("Enter the House Number: ")
    mycursor = comp.cursor()

    sql = "INSERT INTO committe (Designation,Name,House_no) VALUES (%s, %s, %s)"
    val = (desig,name,h_no)
    mycursor.execute(sql,val)
    comp.commit()

def staff_entry():
    name = input("Enter the name: ")
    depart = input("Enter the department of the staff: ")
    handled_by = input("Enter the Designation of the person who manages the staff member: ")
    contact = input("Enter the contact number of the staff member: ")
    mycursor = comp.cursor()

    sql = "INSERT INTO staff (Staff_name,Department,Handled_by,Contact) VALUES (%s, %s, %s, %s)"
    val = (name,depart,handled_by,contact)
    mycursor.execute(sql,val)
    comp.commit()

def committee_member_details(desig):
    mycursor = comp.cursor()
    mycursor.execute("SELECT * FROM committe")
    myresult = mycursor.fetchall()
    
    for x in myresult:
        if desig in x:
            for b in x:
                print(b,end='\t\t')
            print()

def staff_details(name):
    mycursor = comp.cursor()
    mycursor.execute("SELECT * FROM staff")
    myresult = mycursor.fetchall()
    
    for x in myresult:
        if name in x:
            for b in x:
                print(b,end='\t\t')
            print()

def maintenance():
    date = datetime.date.today()
    status = input("Enter the status of the payment: ")
    house_no = input("Enter the house number: ")

    mycursor = comp.cursor()

    sql = "INSERT INTO maintenance (date,status,House_no) VALUES (%s, %s, %s)"
    val = (date, status, house_no)
    mycursor.execute(sql,val)
    comp.commit()

def maintenance_status(h_no):
    mycursor = comp.cursor()
    mycursor.execute("SELECT * FROM staff")
    myresult = mycursor.fetchall()
    
    for x in myresult:
        if h_no in x:
            for b in x:
                print(b,end='\t\t')
            print()

def admin():
    username = input("Enter user name: ")
    passw = input("Enter the Password: ")

    mycursor = comp.cursor()

    sql = "INSERT INTO admin (ID, pass) VALUES (%s, %s)"
    val = (username,passw)
    mycursor.execute(sql,val)
    comp.commit()

def login():
    user=input("Enter user name: ")
    p=input("Enter your password: ")
    
    mycursor = comp.cursor()  
    mycursor.execute("SELECT * FROM admin")
    myresult = mycursor.fetchall()
    
    for x in myresult:
        if user and p in x:
            return True
            
    return False

def delete():
    user=input("Enter user name")
    p=input("Enter your password")
    mycursor = comp.cursor()
    com="DELETE FROM user2 WHERE Name='{}'".format(user)
    mycursor.execute(com)
    comp.commit()    

def admin_main():
    print('\t\t\t\t\t\t\t','     Welcome to Societify','\t\t\t\t\t\t\t\t\t\t')
    print('\t\t\t\t\t\t\t'," Press 1 To Enter house details",)
    print('\t\t\t\t\t\t\t'," Press 2 To Enter staff details",)
    print('\t\t\t\t\t\t\t'," Press 3 to Enter Membership details",)
    print('\t\t\t\t\t\t\t'," Press 4 to View house details",)
    print('\t\t\t\t\t\t\t'," Press 5 to View Staff details",)
    print('\t\t\t\t\t\t\t'," Press 6 to View Membership details",)
    print('\t\t\t\t\t\t\t'," Press 7 to Enter Maintainance details",)
    print('\t\t\t\t\t\t\t'," Press 8 to View Maintainance details",)
    print('\t\t\t\t\t\t\t'," Press 9 to Enter Committee details",)
    print('\t\t\t\t\t\t\t'," Press 10 to View Committee details",)


    inp=int(input("Enter your choice: "))

    if inp==1:
        add_house()
        admin_main()

    elif inp==2:
        staff_entry()
        admin_main()
        
    elif inp==3:
        membership()
        admin_main()

    elif inp==4:
        
        admin_main()

    elif inp==5:
        s = input("Enter staff member name: ")
        staff_details(s)
        admin_main()
    
    elif inp==6:
        show_all_activities()
        admin_main()

    elif inp==7:
        maintenance()
        admin_main()
    
    elif inp==8:
        v = input("Enter House Number: ")
        maintenance_status(v)
        admin_main()

    elif inp==9:
        Committee_members()
        admin_main()

    elif inp==10:
        d = input("Enter the Designation: ")
        committee_member_details(d)
        admin_main()

    else:
        print("Wrong input! Please try again")
        main()

def main():
    print('\t\t\t\t\t\t\t','     Welcome to Societify','\t\t\t\t\t\t\t\t\t\t')
    print()
    print()
    print()
    print('\t\t\t\t\t\t\t\t',"  Main Menu:")
    print()
    print('\t\t\t\t\t\t\t'," Press 1 To Enter visitor details",)
    print('\t\t\t\t\t\t\t'," Press 2 to Enter Admin Mode",)
    inp=int(input("Enter your choice:"))

    if inp == 1:
        inp2= 0
        print('\t\t\t\t\t\t\t'," Press 1 For Visitor In",)
        print('\t\t\t\t\t\t\t'," Press 2 For Visitor Out",)
        if inp2 == 1:
            visitor_in()
        elif inp2 == 2:
            visitor_out()
        else:
            print("Invalid Input! Please try again")
        main()

    elif inp == 2:
        if login() == True:
            admin_main()
        
    else:
        print("Wrong input! Please try again")
        main()

main()
