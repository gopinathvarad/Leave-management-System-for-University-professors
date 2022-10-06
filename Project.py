import csv
import pandas as pd
import os as os


def general(n,ID):
    MAX=2
    times=5
    if(n<times):
        print("General Leave requested\n")
        with open("Employees.csv","r", newline="") as file:
            a = csv.writer(file)
            reader=csv.reader(file)
            rows=list(csv.reader(file))
            x=len(rows)
            for i in range(x):
                l=rows[i]
                if l[0]==ID:
                    wf=pd.read_csv("Employees.csv")
                    wf.loc[i-1,'STATUS']=f'Applied for general leave ({MAX} days)'
                    wf.to_csv("Employees.csv",index=False)
                    
    else:
        print("You cant apply for this leave\n")

def sick(n,ID):
    MAX=3
    times=10
    if(n<times):
        print("Sick Leave requested\n")
        with open("Employees.csv","r", newline="") as file:
            a = csv.writer(file)
            reader=csv.reader(file)
            rows=list(csv.reader(file))
            x=len(rows)
            for i in range(x):
                l=rows[i]
                if l[0]==ID:
                    wf=pd.read_csv("Employees.csv")
                    wf.loc[i-1,'STATUS']=f'Applied for sick leave ({MAX} days)'
                    wf.to_csv("Employees.csv",index=False)

def maternity(n,ID):
    MAX=84
    times=1
    if(n<times):
        print("Maternity Leave requested\n")
        with open("Employees.csv","r", newline="") as file:
            a = csv.writer(file)
            reader=csv.reader(file)
            rows=list(csv.reader(file))
            x=len(rows)
            for i in range(x):
                l=rows[i]
                if l[0]==ID:
                    wf=pd.read_csv("Employees.csv")
                    wf.loc[i-1,'STATUS']=f'Applied for Maternity leave ({MAX} days)'
                    wf.to_csv("Employees.csv",index=False)

def marriage(n,ID):
    MAX=3
    times=1
    if(n<times):
        print("Marriage Leave requested\n")
        with open("Employees.csv","r", newline="") as file:
            a = csv.writer(file)
            reader=csv.reader(file)
            rows=list(csv.reader(file))
            x=len(rows)
            for i in range(x):
                l=rows[i]
                if l[0]==ID:
                    wf=pd.read_csv("Employees.csv")
                    wf.loc[i-1,'STATUS']=f'Applied for Marriage leave ({MAX} days)'
                    wf.to_csv("Employees.csv",index=False)

def holiday(n,ID):
    MAX=18
    times=1
    if(n<times):
        print("Holiday requested\n")
        with open("Employees.csv","r", newline="") as file:
            a = csv.writer(file)
            reader=csv.reader(file)
            rows=list(csv.reader(file))
            x=len(rows)
            for i in range(x):
                l=rows[i]
                if l[0]==ID:
                    wf=pd.read_csv("Employees.csv")
                    wf.loc[i-1,'STATUS']=f'Applied for Holiday ({MAX} days)'
                    wf.to_csv("Employees.csv",index=False)

def earned(ID):
    MAX=10
    print("Earned Leave will be approved\n")
    with open("Employees.csv","r", newline="") as file:
        a = csv.writer(file)
        reader=csv.reader(file)
        rows=list(csv.reader(file))
        x=len(rows)
        for i in range(x):
            l=rows[i]
            if l[0]==ID:
                wf=pd.read_csv("Employees.csv")
                wf.loc[i-1,'STATUS']=f'Approved'
                wf.to_csv("Employees.csv",index=False)



def add_user():
    print()
    l=[]
    ID = int(input("Enter User ID :: "))
    with open("Employees.csv","r") as file:
        rows=list(csv.reader(file))
        x=len(rows)
        for i in range(x):
            l=rows[i]
            if l[0]==str(ID):
                print(f"ID already exists")
                return
    print()
    with open("Employees.csv", "a", newline="") as file:
        writer=csv.writer(file)
        password= input("Enter the password :: ")
        name = input("Enter your name :: ")
        salary = int(input("Enter the salary :: "))
        status='Not Applied'
        details = [ID,password,name,salary,status]
        writer.writerow(details)
    print()

def add_admin():
    print()
    l=[]
    ID = int(input("Enter Admin ID :: "))
    with open("Admins.csv","r") as file:
        rows=list(csv.reader(file))
        x=len(rows)
        for i in range(x):
            l=rows[i]
            if l[0]==str(ID):
                print(f"ID already exists")
                return
    print()
    with open("Admins.csv", "a", newline="") as file:
        writer = csv.writer(file)
        password= input("Enter password :: ")
        name = input("Enter your name :: ")
        details = [ID,password,name]
        writer.writerow(details)
    print()

def login_user(ID,password):
    l=[]
    success_id=""
    success_pw=""
    with open("Employees.csv","r") as file:
        rows=list(csv.reader(file))
        x=len(rows)
        for i in range(x):
            l=rows[i]
            if l[0]==str(ID) and l[1]==password:
                success_id=str(ID)
                success_pw=password
                print(f"Login Successful for user {l[2]}")
                apply_leave(ID)
            else:
                continue
    if success_id!=str(ID) or success_pw!=password:
        print("Re-enter user id and password")
        id=int(input("Enter User Login Id "))
        pw=input("Enter User Password ")
        login_user(str(id),pw)
        

def login_admin(ID,password):
    l=[]
    success_id=""
    success_pw=""
    with open("Admins.csv","r") as file:
        rows=list(csv.reader(file))
        x=len(rows)
        for i in range(x):
            l=rows[i]
            if l[0]==str(ID) and l[1]==password:
                success_id=l[0]
                success_pw=l[1]
                print(f"Login Successful for user {l[2]}")
                print("All IDs elligible for approval : ")
                display_leave_id()    
            else:
                continue
    if success_id!=str(ID) or success_pw!=password:
        print("Re-enter Admin id and password")
        id=int(input("Enter Admin Login Id "))
        pw=input("Enter Admin Password ")
        login_admin(str(id),pw)

def display_leave_id():
    names=[]
    IDs=[]
    with open("Employees.csv","r", newline="") as file:
        a = csv.writer(file)
        reader=csv.reader(file)
        rows=list(csv.reader(file))
        x=len(rows)
        for i in range(x):
            l=rows[i]
            if l[4]!='Not Applied' and i!=0:
                if l[4]!='Denied':
                    IDs.append(l[0])
                    print(l[0])
                    names.append(l[2])

    x=len(IDs)
    for i in IDs:
        if str(i) in IDs:
            admin_approve(i)
        
    
def admin_approve(ID):
    with open("Employees.csv","r", newline="") as file:
        a = csv.writer(file)
        reader=csv.reader(file)
        rows=list(csv.reader(file))
        x=len(rows)
        i=1
        while i<x:
            l=rows[i]
            i=i+1
            #print(l[0],ID)
            if l[0]==str(ID) and l[4]!='Approved':
                ch=input(f"Approve Leave for ID {ID} ?....Y or N\n")
                if ch=='Y':
                    wf=pd.read_csv("Employees.csv")
                    wf.loc[i-2,'STATUS']='Approved'
                    wf.to_csv("Employees.csv",index=False)
                    print("Approval done")
                    
                else:
                    wf=pd.read_csv("Employees.csv")
                    wf.loc[i-2,'STATUS']='Denied'
                    wf.to_csv("Employees.csv",index=False)
                    print("Application Denied")
                return
                                   
def apply_leave(ID):
    ch = 0
    while ch != -1:
        print("Press 1 for General leave")
        print("Press 2 for Sick leave")
        print("Press 3 for Maternity leave")
        print("Press 4 for Marriage leave")
        print("Press 5 for Holiday")
        print("Press 6 for Earned leave")
        print("Press 7 to Logout")
        ch = int(input("Enter Your Choice :: "))

        if ch == 1:
            g=int(input("Enter number of times you have taken General leave previosly: "))
            general(g,ID)
        
        elif ch == 2:
            g=int(input("Enter number of times you have taken Sick leave previosly: "))
            sick(g,ID)
        
        elif ch == 3:
            g=int(input("Enter number of times you have taken Maternity leave previosly: "))
            maternity(g,ID)

        elif ch == 4:
            g=int(input("Enter number of times you have taken Marriage leave previosly: "))
            marriage(g,ID)
        
        elif ch == 5:
            g=int(input("Enter number of times you have taken Holiday previosly: "))
            holiday(g,ID)
        
        elif ch == 6:
            earned(ID)

        elif ch == 7:
            print("Loging Out...")
            ch = -1
        else:
            print("Invalid Choice !!!")
            print()



if not os.path.isfile("./Employees.csv"):
    with open("Employees.csv", "w", newline="") as file:
        headings=['ID','PASSWORD','NAME','SALARY','STATUS']
        writer=csv.DictWriter(file,fieldnames=headings)
        writer.writeheader()

if not os.path.isfile("./Admins.csv"):
    with open("Admins.csv", "w", newline="") as file:
        heading=['ID','PASSWORD','NAME']
        writer=csv.DictWriter(file,fieldnames=heading)
        writer.writeheader()

def main():
    print("WELCOME TO LEAVE MANAGEMENT SYSTEM")
    ch = 0
    while ch != -1:
        print("Press 1 to Add User")
        print("Press 2 to Login into User")
        print("Press 3 to Add Admin")
        print("Press 4 to Login into Admin")
        print("Press 5 to Exit")
        ch = int(input("Enter Your Choice :: "))

        if ch == 1:
            add_user()
        
        elif ch == 2:
            id=int(input("Enter User Login Id "))
            pw=input("Enter User Password ")
            login_user(str(id),pw)
        
        elif ch == 3:
            add_admin()

        elif ch == 4:
            id=int(input("Enter Admin Login Id "))
            pw=input("Enter Admin Password ")
            login_admin(str(id),pw)
        
        elif ch == 5:
            print("Thanks For Using our software...")
            ch = -1
        
        else:
            print("Invalid Choice !!!")
            print()

if __name__=="__main__":
    main()


# add_user()
# add_user()
# add_admin()
#login_user('1','aaa')
#login_user('2','bbb')
#login_admin('1','aaa')
#display_leave_id()
#admin_approve(3)