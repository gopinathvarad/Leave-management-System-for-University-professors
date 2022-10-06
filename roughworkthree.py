import csv
import pandas as pd
import os as os
from tkinter import *
from tkinter import messagebox


def writerfunadmin(details):   
    #print(details)
    print()
    with open("Admins.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(details)

def writerfunuser(details):   
    #print(details)
    print()
    with open("Employees.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(details)

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

def general(ID):
    MAX=2
    times=5
    genframe = Toplevel(frame, padx=10, pady=10)
    genframe.title("General Leave")
    g= Entry(genframe, width=10, borderwidth=3)
    g.grid(row=0, column=1, padx=5, pady=10)
    g_label = Label(genframe, text="Enter number of times you have taken General leave previosly: ")
    g_label.grid(row=0, column=0, padx=5, pady=10)
    def read():
        n=int(g.get())
        if(n<times):
            print("General Leave requested\n")
            with open("Employees.csv","r", newline="") as file:
                a = csv.writer(file)
                reader=csv.reader(file)
                rows=list(csv.reader(file))
                x=len(rows)
                for i in range(x):
                    l=rows[i]
                    if l[0]==str(ID):
                        wf=pd.read_csv("Employees.csv")
                        wf.loc[i-1,'STATUS']=f'Applied for general leave ({MAX} days)'
                        wf.to_csv("Employees.csv",index=False)
                        messagebox.showinfo("Status",f'Applied for general leave ({MAX} days)')
                        
        else:
            messagebox.showwarning("Warning","You cant apply for general leave")
            print("You cant apply for this leave\n")
        
        genframe.destroy()

    applybtn = Button(genframe, text="Apply",
            padx=5, pady=5,bg='#FFFFFF',command=lambda:read())
    applybtn.grid(row=3, column=2, columnspan=1,rowspan=1,padx=5,pady=5)


def sick(ID):
    MAX=3
    times=10
    genframe = Toplevel(frame, padx=10, pady=10)
    genframe.title("Sick Leave")
    g= Entry(genframe, width=10, borderwidth=3)
    g.grid(row=0, column=1, padx=5, pady=10)
    g_label = Label(genframe, text="Enter number of times you have taken Sick leave previosly: ")
    g_label.grid(row=0, column=0, padx=5, pady=10)
    def read():
        n=int(g.get())
        if(n<times):
            print("Sick Leave requested\n")
            with open("Employees.csv","r", newline="") as file:
                a = csv.writer(file)
                reader=csv.reader(file)
                rows=list(csv.reader(file))
                x=len(rows)
                for i in range(x):
                    l=rows[i]
                    if l[0]==str(ID):
                        wf=pd.read_csv("Employees.csv")
                        wf.loc[i-1,'STATUS']=f'Applied for sick leave ({MAX} days)'
                        wf.to_csv("Employees.csv",index=False)
                        messagebox.showinfo("Status",f'Applied for sick leave ({MAX} days)')
                        
        else:
            messagebox.showwarning("Warning","You cant apply for sick leave")
            print("You cant apply for this leave\n")
        
        genframe.destroy()

    applybtn = Button(genframe, text="Apply",
            padx=5, pady=5,bg='#FFFFFF',command=lambda:read())
    applybtn.grid(row=3, column=2, columnspan=1,rowspan=1,padx=5,pady=5)
    

def maternity(ID):
    MAX=84
    times=1
    genframe = Toplevel(frame, padx=10, pady=10)
    genframe.title("Maternity Leave")
    g= Entry(genframe, width=10, borderwidth=3)
    g.grid(row=0, column=1, padx=5, pady=10)
    g_label = Label(genframe, text="Enter number of times you have taken Maternity leave previosly: ")
    g_label.grid(row=0, column=0, padx=5, pady=10)
    def read():
        n=int(g.get())
        if(n<times):
            print("Maternity Leave requested\n")
            with open("Employees.csv","r", newline="") as file:
                a = csv.writer(file)
                reader=csv.reader(file)
                rows=list(csv.reader(file))
                x=len(rows)
                for i in range(x):
                    l=rows[i]
                    if l[0]==str(ID):
                        wf=pd.read_csv("Employees.csv")
                        wf.loc[i-1,'STATUS']=f'Applied for maternity leave ({MAX} days)'
                        wf.to_csv("Employees.csv",index=False)
                        messagebox.showinfo("Status",f'Applied for maternity leave ({MAX} days)')
                        
        else:
            messagebox.showwarning("Warning","You cant apply for maternity leave")
            print("You cant apply for this leave\n")
        
        genframe.destroy()

    applybtn = Button(genframe, text="Apply",
            padx=5, pady=5,bg='#FFFFFF',command=lambda:read())
    applybtn.grid(row=3, column=2, columnspan=1,rowspan=1,padx=5,pady=5)  



def marriage(ID):
    MAX=3
    times=1
    genframe = Toplevel(frame, padx=10, pady=10)
    genframe.title("Marriage Leave")
    g= Entry(genframe, width=10, borderwidth=3)
    g.grid(row=0, column=1, padx=5, pady=10)
    g_label = Label(genframe, text="Enter number of times you have taken Marriage leave previosly: ")
    g_label.grid(row=0, column=0, padx=5, pady=10)
    def read():
        n=int(g.get())
        if(n<times):
            print("Marriage Leave requested\n")
            with open("Employees.csv","r", newline="") as file:
                a = csv.writer(file)
                reader=csv.reader(file)
                rows=list(csv.reader(file))
                x=len(rows)
                for i in range(x):
                    l=rows[i]
                    if l[0]==str(ID):
                        wf=pd.read_csv("Employees.csv")
                        wf.loc[i-1,'STATUS']=f'Applied for marriage leave ({MAX} days)'
                        wf.to_csv("Employees.csv",index=False)
                        messagebox.showinfo("Status",f'Applied for marriage leave ({MAX} days)')
                        
        else:
            messagebox.showwarning("Warning","You cant apply for marriage leave")
            print("You cant apply for this leave\n")
        
        genframe.destroy()

    applybtn = Button(genframe, text="Apply",
            padx=5, pady=5,bg='#FFFFFF',command=lambda:read())
    applybtn.grid(row=3, column=2, columnspan=1,rowspan=1,padx=5,pady=5)  
      

def holiday(ID):
    MAX=18
    times=1
    genframe = Toplevel(frame, padx=10, pady=10)
    genframe.title("Holiday")
    g= Entry(genframe, width=10, borderwidth=3)
    g.grid(row=0, column=1, padx=5, pady=10)
    g_label = Label(genframe, text="Enter number of times you have taken Holiday previosly: ")
    g_label.grid(row=0, column=0, padx=5, pady=10)
    def read():
        n=int(g.get())
        if(n<times):
            print("Holiday requested\n")
            with open("Employees.csv","r", newline="") as file:
                a = csv.writer(file)
                reader=csv.reader(file)
                rows=list(csv.reader(file))
                x=len(rows)
                for i in range(x):
                    l=rows[i]
                    if l[0]==str(ID):
                        wf=pd.read_csv("Employees.csv")
                        wf.loc[i-1,'STATUS']=f'Applied for Holiday ({MAX} days)'
                        wf.to_csv("Employees.csv",index=False)
                        messagebox.showinfo("Status",f'Applied for Holiday ({MAX} days)')
                        
        else:
            messagebox.showwarning("Warning","You cant apply for Holiday")
            print("You cant apply for this leave\n")
        
        genframe.destroy()

    applybtn = Button(genframe, text="Apply",
            padx=5, pady=5,bg='#FFFFFF',command=lambda:read())
    applybtn.grid(row=3, column=2, columnspan=1,rowspan=1,padx=5,pady=5)

def earned(ID):
    
    with open("Employees.csv","r", newline="") as file:
        a = csv.writer(file)
        reader=csv.reader(file)
        rows=list(csv.reader(file))
        x=len(rows)
        for i in range(x):
            l=rows[i]
            if l[0]==str(ID):
                wf=pd.read_csv("Employees.csv")
                wf.loc[i-1,'STATUS']='Approved'
                wf.to_csv("Employees.csv",index=False)
                messagebox.showinfo("Status",f'Earned Leave Approved')

# -------------------------------------------------GUI-----------------------------------#

root =Tk()

root.title("Leave management system")
frame = LabelFrame(root, padx=40, pady=20)
frame.pack(padx=75)


def add_admin():
    addadminframe = Toplevel(frame, padx=10, pady=10)
    addadminframe.title("Addadmin")

    print()
    l=[]
    
    #Admin ID
    adminid = Entry(addadminframe, width=10, borderwidth=3)
    adminid.grid(row=0, column=1, padx=5, pady=10)
    adminid_label = Label(addadminframe, text="Enter Admin ID:")
    adminid_label.grid(row=0, column=0, padx=5, pady=10)
    
    #Admin password
    adminpass = Entry(addadminframe, width=10, borderwidth=3)
    adminpass.grid(row=1, column=1, padx=5, pady=10)
    adminpass_label = Label(addadminframe, text="Enter Admin Password:")
    adminpass_label.grid(row=1, column=0, padx=5, pady=10)
    
    #Admin name
       
    adminname = Entry(addadminframe, width=10, borderwidth=3)
    adminname.grid(row=2, column=1, padx=5, pady=10)
    adminname_label = Label(addadminframe, text="Enter Admin name:")
    adminname_label.grid(row=2, column=0, padx=5, pady=10)

    def read():
        aid=int(adminid.get())  
        ap=adminpass.get()
        aname=adminname.get()
        with open("Admins.csv","r") as file:
            rows=list(csv.reader(file))
            x=len(rows)
            for i in range(x):
                l=rows[i]
                if l[0]==str(aid):
                    print(f"ID already exists")
                    messagebox.showwarning("Warning","Admin ID already exists")
                    return
                else:
                    details = [aid,ap,aname]
                    addadminframe.destroy()
            if l[0]!=str(aid):        
                writerfunadmin(details) 
    # Continue button in addadmin frame
    btn6 = Button(addadminframe, text="Continue",
              padx=5, pady=5,bg='#FFFFFF',command=read)
    btn6.grid(row=3,columnspan=5,column=0,padx=5,pady=5)
     
    
    
def add_user():
    adduserframe = Toplevel(frame, padx=10, pady=10)
    adduserframe.title("Adduser")


    print()
    l=[]
    #ID = int(input("Enter User ID :: "))
    userid = Entry(adduserframe, width=10, borderwidth=3)
    userid.grid(row=0, column=1, padx=5, pady=10)
    userid_label = Label(adduserframe, text="Enter User ID:")
    userid_label.grid(row=0, column=0, padx=5, pady=10)
    
    #user password
    userpass = Entry(adduserframe, width=10, borderwidth=3)
    userpass.grid(row=1, column=1, padx=5, pady=10)
    userpass_label = Label(adduserframe, text="Enter User Password:")
    userpass_label.grid(row=1, column=0, padx=5, pady=10)
    
    #user name
       
    username = Entry(adduserframe, width=10, borderwidth=3)
    username.grid(row=2, column=1, padx=5, pady=10)
    username_label = Label(adduserframe, text="Enter user name:")
    username_label.grid(row=2, column=0, padx=5, pady=10)

    usersal = Entry(adduserframe, width=10, borderwidth=3)
    usersal.grid(row=3, column=1, padx=5, pady=10)
    usersal_label = Label(adduserframe, text="Enter user salary:")
    usersal_label.grid(row=3, column=0, padx=5, pady=10)


    def uread():
        uid=int(userid.get())  
        up=userpass.get()
        uname=username.get()
        usal=usersal.get()
        ustatus="Not Applied"
        with open("Employees.csv","r") as file:
            rows=list(csv.reader(file))
            x=len(rows)
            for i in range(x):
                l=rows[i]
                if l[0]==str(uid):
                    print(f"ID already exists")
                    messagebox.showwarning("Warning","User ID already exists")
                    return
                else:
                    details = [uid,up,uname,usal,ustatus]
                    adduserframe.destroy()
            if l[0]!=str(uid):        
                writerfunuser(details) 

# Continue button in adduser frame
    btn8 = Button(adduserframe, text="Continue",padx=5, pady=5,bg='#FFFFFF',command=uread)
    btn8.grid(row=5,columnspan=5,column=0,padx=5,pady=5)

def loginuser():
    loginuserframe = Toplevel(frame, padx=10, pady=10)
    loginuserframe.title("Loginuser")
    
    #User login ID
    userloginid = Entry(loginuserframe, width=10, borderwidth=3)
    userloginid.grid(row=0, column=1, padx=5, pady=10)
    userloginid_label = Label(loginuserframe, text="Enter User Login ID:")
    userloginid_label.grid(row=0, column=0, padx=5, pady=10)
    
    #Admin login password
    userloginpass = Entry(loginuserframe, width=10, borderwidth=3)
    userloginpass.grid(row=1, column=1, padx=5, pady=10)
    adminloginpass_label = Label(loginuserframe, text="Enter User Login Password:")
    adminloginpass_label.grid(row=1, column=0, padx=5, pady=10)
    
    
    #continue button in admin login frame
    btn7 = Button(loginuserframe, text="Continue",
                padx=5, pady=5,bg='#FFFFFF',command=lambda:login_user(int(userloginid.get()) ,userloginpass.get()))
    btn7.grid(row=2,columnspan=5,column=0,padx=5,pady=5)

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
                    messagebox.showinfo("SUCCESS",f"Login Successful for User {l[2]}")
                    applyframe = Toplevel(frame, padx=180, pady=10)
                    applyframe.minsize(500,200)
                    applyframe.title("Apply")
                    startapplybtn = Button(applyframe, text="Start Applying",
                padx=5, pady=5,bg='#FFFFFF',command=lambda:apply_leave(ID,l[2]))
                    startapplybtn.grid(row=2,columnspan=5,column=0,padx=5,pady=5)
                    #apply_leave(ID)
                else:
                    continue
        if success_id!=str(ID) or success_pw!=password:
            print("Re-enter User id and password")
            messagebox.showwarning("Warning","Re-enter User id and password")
            #id=int(input("Enter User Login Id "))
            #pw=input("Enter User Password ")
            #login_user(str(id),pw)
        
        def apply_leave(ID,name):
            print(ID)

            userlabel = Label(applyframe, text=f"----Logged in into----\n \nUser ID :{ID}\nName: {name}")
            userlabel.grid(row=0, column=0, padx=5, pady=10)


            genbtn = Button(applyframe, text="General leave",
            padx=10, pady=5,bg='#FFFFFF',command=lambda:general(ID) )
            genbtn.grid(row=2, column=0, columnspan=1,rowspan=1,padx=10,pady=5)
            
            
            sickbtn = Button(applyframe, text="Sick leave",
              padx=5, pady=5,bg='#FFFFFF',command=lambda:sick(ID) )
            sickbtn.grid(row=3, column=0, columnspan=1,rowspan=1,padx=5,pady=5)

            maternitybtn = Button(applyframe, text="Maternity leave",
              padx=5, pady=5,bg='#FFFFFF',command=lambda:maternity(ID) )
            maternitybtn.grid(row=4, column=0, columnspan=1,rowspan=1,padx=5,pady=5)

            marriagebtn = Button(applyframe, text="Marriage leave",
              padx=5, pady=5,bg='#FFFFFF',command=lambda:marriage(ID) )
            marriagebtn.grid(row=5, column=0, columnspan=1,rowspan=1,padx=5,pady=5)

            holidaybtn = Button(applyframe, text="Holiday",
              padx=5, pady=5,bg='#FFFFFF',command=lambda:holiday(ID) )
            holidaybtn.grid(row=6, column=0, columnspan=1,rowspan=1,padx=5,pady=5)

            earnedbtn= Button(applyframe, text="Earned Leave",
              padx=5, pady=5,bg='#FFFFFF',command=lambda:earned(ID) )
            earnedbtn.grid(row=7, column=0, columnspan=1,rowspan=1,padx=5,pady=5)

            logout= Button(applyframe, text="Logout",
              padx=5, pady=5,bg='#FFFFFF',command=applyframe.destroy )
            logout.grid(row=8, column=0, columnspan=1,rowspan=1,padx=5,pady=5)



def close():
    messagebox.showinfo("Greetings","Thanks For Using Our Software")
    root.destroy()
    frame.destroy()

#Adduser
btn1 = Button(frame, text="Add user",
              padx=5, pady=5,bg='#FFFFFF',command=add_user )
btn1.grid(row=2, column=0, columnspan=1,rowspan=1,padx=5,pady=5)

#Loginuser
btn2 = Button(frame, text="Login user",
              padx=5, pady=5,bg='#FFFFFF',command=lambda:loginuser() )
btn2.grid(row=4, column=0, columnspan=1,rowspan=1,padx=5,pady=5)

#Addadmin
btn3 = Button(frame, text="Add Admin",
              padx=5, pady=5,bg='#FFFFFF' ,command= add_admin)
btn3.grid(row=6, column=0, columnspan=1,rowspan=1,padx=5,pady=5)

#Loginadmin
btn4 = Button(frame, text="Login Admin",
              padx=5, pady=5,bg='#FFFFFF',command=lambda: loginadmin())
btn4.grid(row=8, column=0, columnspan=1,rowspan=1,padx=5,pady=5)

#Close
btn5 = Button(frame, text="Close",
              padx=5, pady=5,bg='#FFFFFF', command=lambda:close())
btn5.grid(row=10, column=0, columnspan=1,rowspan=1,padx=5,pady=5)


    
def loginadmin():
    loginadminframe = Toplevel(frame, padx=10, pady=10)
    loginadminframe.title("Loginadmin")
    
    #Admin login ID
    adminloginid = Entry(loginadminframe, width=10, borderwidth=3)
    adminloginid.grid(row=0, column=1, padx=5, pady=10)
    adminloginid_label = Label(loginadminframe, text="Enter Admin Login ID:")
    adminloginid_label.grid(row=0, column=0, padx=5, pady=10)
    
    #Admin login password
    adminloginpass = Entry(loginadminframe, width=10, borderwidth=3)
    adminloginpass.grid(row=1, column=1, padx=5, pady=10)
    adminloginpass_label = Label(loginadminframe, text="Enter Admin Login Password:")
    adminloginpass_label.grid(row=1, column=0, padx=5, pady=10)
    
    
    #continue button in admin login frame
    btn7 = Button(loginadminframe, text="Continue",
                padx=5, pady=5,bg='#FFFFFF',command=lambda:login_admin(int(adminloginid.get()) ,adminloginpass.get()))
    btn7.grid(row=2,columnspan=5,column=0,padx=5,pady=5)
    

    def admin_approve(ID):
        def yesFunc():
            wf=pd.read_csv("Employees.csv")
            wf.loc[i-2,'STATUS']='Approved'
            wf.to_csv("Employees.csv",index=False)
            adminapproveframe.destroy()
        def noFunc():
            wf=pd.read_csv("Employees.csv")
            wf.loc[i-2,'STATUS']='Denied'
            wf.to_csv("Employees.csv",index=False)
            print("Application Denied")
            adminapproveframe.destroy()
        
        #GUI
        adminapproveframe = Toplevel(frame, padx=10, pady=10)
        adminapproveframe.title("Admin approve")
       
            
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
                    adminloginsuccess_label = Label(adminapproveframe, text=f"Approve leave for ID: {ID}? ")
                    adminloginsuccess_label.grid(row=0, column=0, padx=5, pady=10)    

                    yesbtn = Button(adminapproveframe, text="YES",
                    padx=5, pady=5,bg='#FFFFFF',command=lambda:yesFunc())
                    yesbtn.grid(row=2,columnspan=5,column=0,padx=5,pady=5)

                    nobtn = Button(adminapproveframe, text="NO",
                    padx=10, pady=5,bg='#FFFFFF',command=lambda:noFunc())
                    nobtn.grid(row=2,columnspan=5,column=3,padx=10,pady=5)
                    
                    print("Denied")
                       
                    print("Approval done")
                    return    
            
    
    def display_leave_id():
        names=[]
        IDs=[]
        displayidframe = Toplevel(frame, padx=10, pady=10)
        displayidframe.title("Elligible ids") 
        with open("Employees.csv","r", newline="") as file:
            a = csv.writer(file)
            reader=csv.reader(file)
            rows=list(csv.reader(file))
            x=len(rows)
            for i in range(x):
                l=rows[i]
                if l[4]!='Not Applied' and i!=0:
                    if l[4]!='Denied':
                        if l[4]!='Approved':
                            IDs.append(l[0])
                            print(l[0])
                            names.append(l[2])

            for i in range (len(IDs)):
                appliedid_label = Label(displayidframe, text=str(IDs[i])+" : "+names[i])
                appliedid_label.grid(row=i+2 ,column=0,padx=5,pady=10)
        x=len(IDs)
        approvebtn = Button(displayidframe, text="Start Approving",
                padx=5, pady=5,bg='#FFFFFF',command=lambda:start())
        approvebtn.grid(row=5,columnspan=5,column=0,padx=5,pady=5)

        logout= Button(displayidframe, text="Logout",
        padx=5, pady=5,bg='#FFFFFF',command=displayidframe.destroy )
        logout.grid(row=6, column=0, columnspan=5,rowspan=1,padx=5,pady=5)
        def start():
            for i in IDs:
                if str(i) in IDs:
                    admin_approve(i)
                
    
    
    
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
                    messagebox.showinfo("SUCCESS",f"Login Successful for Admin {l[2]}")
 
                    print(f"Login Successful for user {l[2]}")
                    print("All IDs elligible for approval : ")
                    display_leave_id()    
                else:
                    continue
        if success_id!=str(ID) or success_pw!=password:
            print("Re-enter Admin id and password")
            messagebox.showwarning("Warning","Re-enter Admin id and password")
            #id=int(input("Enter Admin Login Id "))
            #pw=input("Enter Admin Password ")
            #login_admin(str(id),pw)
        
    

root.mainloop()




# def general(n,ID):
#     MAX=2
#     times=5
#     if(n<times):
#         print("General Leave requested\n")
#         with open("Employees.csv","r", newline="") as file:
#             a = csv.writer(file)
#             reader=csv.reader(file)
#             rows=list(csv.reader(file))
#             x=len(rows)
#             for i in range(x):
#                 l=rows[i]
#                 if l[0]==ID:
#                     wf=pd.read_csv("Employees.csv")
#                     wf.loc[i-1,'STATUS']=f'Applied for general leave ({MAX} days)'
#                     wf.to_csv("Employees.csv",index=False)
                    
#     else:
#         print("You cant apply for this leave\n")

# def sick(n,ID):
#     MAX=3
#     times=10
#     if(n<times):
#         print("Sick Leave requested\n")
#         with open("Employees.csv","r", newline="") as file:
#             a = csv.writer(file)
#             reader=csv.reader(file)
#             rows=list(csv.reader(file))
#             x=len(rows)
#             for i in range(x):
#                 l=rows[i]
#                 if l[0]==ID:
#                     wf=pd.read_csv("Employees.csv")
#                     wf.loc[i-1,'STATUS']=f'Applied for Sick leave ({MAX} days)'
#                     wf.to_csv("Employees.csv",index=False)

# def maternity(n,ID):
#     MAX=84
#     times=1
#     if(n<times):
#         print("Maternity Leave requested\n")
#         with open("Employees.csv","r", newline="") as file:
#             a = csv.writer(file)
#             reader=csv.reader(file)
#             rows=list(csv.reader(file))
#             x=len(rows)
#             for i in range(x):
#                 l=rows[i]
#                 if l[0]==ID:
#                     wf=pd.read_csv("Employees.csv")
#                     wf.loc[i-1,'STATUS']=f'Applied for Maternity leave ({MAX} days)'
#                     wf.to_csv("Employees.csv",index=False)

# def marriage(n,ID):
#     MAX=3
#     times=1
#     if(n<times):
#         print("Marriage Leave requested\n")
#         with open("Employees.csv","r", newline="") as file:
#             a = csv.writer(file)
#             reader=csv.reader(file)
#             rows=list(csv.reader(file))
#             x=len(rows)
#             for i in range(x):
#                 l=rows[i]
#                 if l[0]==ID:
#                     wf=pd.read_csv("Employees.csv")
#                     wf.loc[i-1,'STATUS']=f'Applied for Marriage leave ({MAX} days)'
#                     wf.to_csv("Employees.csv",index=False)

# def holiday(n,ID):
#     MAX=18
#     times=1
#     if(n<times):
#         print("Holiday requested\n")
#         with open("Employees.csv","r", newline="") as file:
#             a = csv.writer(file)
#             reader=csv.reader(file)
#             rows=list(csv.reader(file))
#             x=len(rows)
#             for i in range(x):
#                 l=rows[i]
#                 if l[0]==ID:
#                     wf=pd.read_csv("Employees.csv")
#                     wf.loc[i-1,'STATUS']=f'Applied for Holiday ({MAX} days)'
#                     wf.to_csv("Employees.csv",index=False)

# def earned(ID):
#     MAX=10
#     print("Earned Leave will be approved\n")
#     with open("Employees.csv","r", newline="") as file:
#         a = csv.writer(file)
#         reader=csv.reader(file)
#         rows=list(csv.reader(file))
#         x=len(rows)
#         for i in range(x):
#             l=rows[i]
#             if l[0]==ID:
#                 wf=pd.read_csv("Employees.csv")
#                 wf.loc[i-1,'STATUS']=f'Approved'
#                 wf.to_csv("Employees.csv",index=False)



# def add_user():
#     print()
#     l=[]
#     ID = int(input("Enter User ID :: "))
#     with open("Employees.csv","r") as file:
#         rows=list(csv.reader(file))
#         x=len(rows)
#         for i in range(x):
#             l=rows[i]
#             if l[0]==str(ID):
#                 print(f"ID already exists")
#                 return
#     print()
#     with open("Employees.csv", "a", newline="") as file:
#         writer=csv.writer(file)
#         password= input("Enter the password :: ")
#         name = input("Enter your name :: ")
#         salary = int(input("Enter the salary :: "))
#         status='Not Applied'
#         details = [ID,password,name,salary,status]
#         writer.writerow(details)
#     print()


    

        

        

# # def login_admin(ID,password):
# #     l=[]
# #     success_id=""
# #     success_pw=""
# #     with open("Admins.csv","r") as file:
# #         rows=list(csv.reader(file))
# #         x=len(rows)
# #         for i in range(x):
# #             l=rows[i]
# #             if l[0]==str(ID) and l[1]==password:
# #                 success_id=l[0]
# #                 success_pw=l[1]
# #                 print(f"Login Successful for user {l[2]}")
# #                 print("All IDs elligible for approval : ")
# #                 display_leave_id()    
# #             else:
# #                 continue
# #     if success_id!=str(ID) or success_pw!=password:
# #         print("Re-enter Admin id and password")
# #         id=int(input("Enter Admin Login Id "))
# #         pw=input("Enter Admin Password ")
# #         login_admin(str(id),pw)


    

                                   
# def apply_leave(ID):
#     ch = 0
#     while ch != -1:
#         print("Press 1 for General leave")
#         print("Press 2 for Sick leave")
#         print("Press 3 for Maternity leave")
#         print("Press 4 for Marriage leave")
#         print("Press 5 for Holiday")
#         print("Press 6 for Earned leave")
#         print("Press 7 to Logout")
#         ch = int(input("Enter Your Choice :: "))

#         if ch == 1:
#             g=int(input("Enter number of times you have taken General leave previosly: "))
#             general(g,ID)
        
#         elif ch == 2:
#             g=int(input("Enter number of times you have taken Sick leave previosly: "))
#             sick(g,ID)
        
#         elif ch == 3:
#             g=int(input("Enter number of times you have taken Maternityleave previosly: "))
#             maternity(g,ID)

#         elif ch == 4:
#             g=int(input("Enter number of times you have taken Marriage leave previosly: "))
#             marriage(g,ID)
        
#         elif ch == 5:
#             g=int(input("Enter number of times you have taken Holiday previosly: "))
#             holiday(g,ID)
        
#         elif ch == 6:
#             earned(ID)

#         elif ch == 7:
#             print("Loging Out...")
#             ch = -1
#         else:
#             print("Invalid Choice !!!")
#             print()




# def main():
#     print("WELCOME TO LEAVE MANAGEMENT SYSTEM")
#     ch = 0
#     while ch != -1:
#         print("Press 1 to Add User")
#         print("Press 2 to Login into User")
#         print("Press 3 to Add Admin")
#         print("Press 4 to Login into Admin")
#         print("Press 5 to Exit")
#         ch = int(input("Enter Your Choice :: "))

#         if ch == 1:
#             add_user()
        
#         elif ch == 2:
#             id=int(input("Enter User Login Id "))
#             pw=input("Enter User Password ")
#             #login_user(str(id),pw)
        
#         elif ch == 3:
#             add_admin()

#         elif ch == 4:
#             id=int(input("Enter Admin Login Id "))
#             pw=input("Enter Admin Password ")
#            # login_admin(str(id),pw)
        
#         elif ch == 5:
#             print("Thanks For Using our software...")
#             ch = -1
        
#         else:
#             print("Invalid Choice !!!")
#             print()

# if __name__=="__main__":
#     main()

#add_user()
# add_user()
# add_admin()
#login_user('1','aaa')
#login_user('2','bbb')
#login_admin('1','aaa')
#display_leave_id()
#admin_approve(3)




