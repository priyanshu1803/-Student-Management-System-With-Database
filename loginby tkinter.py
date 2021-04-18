
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import pymysql

class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        self.uname=StringVar()
        self.passw=StringVar()
        self.Firstname=StringVar()
        self.Lastname=StringVar()
        self.Password=StringVar()
        self.Confirm=StringVar()
        
        
        self.passwordimage=ImageTk.PhotoImage(file="C://Users//hp//Desktop//New folder (2)//images//password.png")
        self.userimage=ImageTk.PhotoImage(file="C://Users//hp//Desktop//New folder (2)//images//user.png")
        self.logoimage=ImageTk.PhotoImage(file="C://Users//hp//Desktop//New folder (2)//images//logo.jpg")
        self.bgimage=ImageTk.PhotoImage(file="C://Users//hp//Desktop//New folder (2)//images//bg.jpg")


        bg=Label(self.root,image=self.bgimage).pack()
        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        
        Loginframe=Frame(self.root,bg=("white"))
        Loginframe.place(x=400,y=150)
        logo=Label(Loginframe,image=self.logoimage,bg="white").grid(row=0,columnspan=2,padx=10,pady=10)

        text1=Label(Loginframe,text="Username",font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        entry1=Entry(Loginframe,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15,"bold")).grid(row=1,column=1,padx=20)
        
        text2=Label(Loginframe,text="Password",font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        entry2=Entry(Loginframe,bd=5,relief=GROOVE,show="*",textvariable=self.passw,font=("",15,"bold")).grid(row=2,column=1,padx=20)
       
        self.but=Button(Loginframe,text="Login",width=5,command=self.login_,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=3,columnspan=2,padx=40,pady=15)    
        self.butn=Button(Loginframe,text="Register",width=6,command=self.admin,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=3,column=1,padx=30,pady=10)    



    def login_(self):

        if self.uname.get()=="" or self.passw.get()=="":
            messagebox.showerror("Error","Fill username and password")
            

        elif self.uname.get()=="Priyanshu" and self.passw.get()=="12345":
            self.register()
            

        else:
            messagebox.showerror("Error","Invalid Username or Password")
            

    def register(self):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title1=Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg="pink",fg="red",bd=10,relief=GROOVE)
        title1.place(x=0,y=0,relwidth=1)

        #variables

        self.name_=StringVar()
        self.roll_=StringVar()
        self.email_=StringVar()
        self.gender_=StringVar()
        self.contact_=StringVar()
        self.dob_=StringVar()       
        self.branch=StringVar()
        
        self.search_by=StringVar()
        self.search_tx=StringVar()
        

        frame1=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        frame1.place(x=0,y=78,width=490,height=618)

        title2=Label(frame1,text="Manage Students",font=("times new roman",30,"bold"),bg="pink",fg="black",bd=3,relief=GROOVE)
        title2.grid(row=0,columnspan=2,pady=5,sticky="w")

        text3=Label(frame1,text="Name",font=("times new roman",15,"bold"),bg="white",fg="green").grid(row=1,column=0,padx=10,pady=15,sticky="w")
        entry3=Entry(frame1,bd=4,relief=GROOVE,textvariable=self.name_,font=("",15,"bold")).grid(row=1,column=1,padx=20,pady=15)

        text4=Label(frame1,text="roll_no",font=("times new roman",15,"bold"),bg="white",fg="green").grid(row=2,column=0,padx=10,pady=15,sticky="w")
        entry4=Entry(frame1,bd=4,relief=GROOVE,textvariable=self.roll_,font=("",15,"bold")).grid(row=2,column=1,padx=20,pady=15)

        text5=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="green").grid(row=3,column=0,padx=10,pady=15,sticky="w")
        entry5=Entry(frame1,bd=4,relief=GROOVE,textvariable=self.email_,font=("",15,"bold")).grid(row=3,column=1,padx=20,pady=15)

        text6=Label(frame1,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="green").grid(row=4,column=0,padx=10,pady=15,sticky="w")
        combo=ttk.Combobox(frame1,textvariable=self.gender_,font=("times new roman",15,"bold"),state="readonly")
        combo['values']=("Male","Female","Other")
        combo.grid(row=4,column=1,padx=20)
      
        text7=Label(frame1,text="contact_no",font=("times new roman",15,"bold"),bg="white",fg="green").grid(row=5,column=0,padx=10,pady=15,sticky="w")
        entry7=Entry(frame1,bd=4,relief=GROOVE,textvariable=self.contact_,font=("",15,"bold")).grid(row=5,column=1,padx=20,pady=15)

        text8=Label(frame1,text="date_of_birth",font=("times new roman",15,"bold"),bg="white",fg="green").grid(row=6,column=0,padx=10,pady=15,sticky="w")
        entry8=Entry(frame1,bd=4,relief=GROOVE,textvariable=self.dob_,font=("",15,"bold")).grid(row=6,column=1,padx=20,pady=15)

        
        branch=Label(frame1,text="Branch",font=("times new roman",16,"bold"),bg="white",fg="green").grid(row=7,column=0,padx=10,pady=15,sticky="w")
        entryo=Entry(frame1,bd=4,relief=GROOVE,textvariable=self.branch,font=("",15,"bold")).grid(row=7,column=1,padx=20,pady=1)



        frame3=Frame(frame1,bd=4,relief=RIDGE,bg="crimson")
        frame3.place(x=5,y=530,width=429,height=65)

        btn2=Button(frame3,text="Add",width=7,command=self.add_students,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=0,column=0,padx=7,pady=10)    
        btn3=Button(frame3,text="Update",width=7,command=self.update_data,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=0,column=1,padx=4,pady=2)    
        btn4=Button(frame3,text="Delete",width=7,command=self.delete_data,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=0,column=2,padx=4,pady=2)    
        btn5=Button(frame3,text="Clear",width=7,command=self.clear_data,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=0,column=3,padx=4,pady=2)    
           
        
        frame2=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        frame2.place(x=490,y=78,width=860,height=619)    
    
        title10=Label(frame2,text="Search By",height=0,font=("times new roman",16,"bold"),bg="white",fg="green")
        title10.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        
        combo1=ttk.Combobox(frame2,textvariable=self.search_by,width=8,font=("times new roman",12,"bold"),state="readonly")
        combo1['values']=("roll_no","Name","Email")
        combo1.grid(row=0,column=1,padx=10,pady=10)
    
        entry11=Entry(frame2,width=15,textvariable=self.search_tx,relief=GROOVE,font=("",15,"bold")).grid(row=0,column=4,padx=20)
        btn6=Button(frame2,text="Search",width=6,command=self.search_data,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=0,column=5,padx=4,pady=10)  
        btn7=Button(frame2,text="Show All",width=6,command=self.fetch_data,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=0,column=6,padx=20,pady=10)  

        frame4=Frame(frame2,bd=4,relief=RIDGE,bg="crimson")
        frame4.place(x=10,y=65,width=800,height=500)    

        scroll_x=Scrollbar(frame4,orient=HORIZONTAL)
        scroll_y=Scrollbar(frame4,orient=VERTICAL)

        self.student_table=ttk.Treeview(frame4,columns=("Name","roll_no","Email","Gender","date_of_birth","contact_no","Branch"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("roll_no",text="roll_no")       
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("date_of_birth",text="date_of_birth")
        self.student_table.heading("contact_no",text="contact_no")
        self.student_table.heading("Branch",text="Branch")
        self.student_table['show']='headings'



        self.student_table.column("Name",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("date_of_birth",width=100)
        self.student_table.column("contact_no",width=100)
        self.student_table.column("Branch",width=100)
        
           
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.name_.get(),
                                                                        self.roll_.get(),
                                                                        self.email_.get(),
                                                                        self.gender_.get(),
                                                                        self.contact_.get(),
                                                                        self.dob_.get(),
                                                                        self.branch.get()
                                                                        ))
        
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()
        messagebox.showinfo("success","Added successfully")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    

    
    def clear_data(self):
        self.name_.set("")
        self.roll_.set("")
        self.email_.set("")
        self.gender_.set("")
        self.contact_.set("")
        self.dob_.set("")
        self.branch.set("")
       

    def get_cursor(self,eve):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents["values"]
        self.name_.set(row[0])
        self.roll_.set(row[1])
        self.email_.set(row[2])
        self.gender_.set(row[3])
        self.contact_.set(row[4])
        self.dob_.set(row[5])
        self.branch.set(row[6])       
          

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
      
        cur.execute("update students SET Name=%s,Email=%s,Gender=%s,contact_no=%s,date_of_birth=%s,Branch=%s where roll_no=%s",(
                                                                                            self.name_.get(),
                                                                                            self.email_.get(),
                                                                                            self.gender_.get(),
                                                                                            self.contact_.get(),
                                                                                            self.dob_.get(),
                                                                                            self.branch.get(),
                                                                                            self.roll_.get()
                                                                                                ))
                                                                                            
        con.commit()
        con.close()
        self.fetch_data()
        self.clear_data()
        messagebox.showinfo("success","Updated successfully")
    
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where Name=%s",self.name_.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear_data()
        messagebox.showinfo("success","Deleted successfully")

    
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        
        cur.execute("select * from students where " +str(self.search_by.get())+" LIKE '%"+str(self.search_tx.get())+"%'")


      
        #cur.execute("select * from students where"+str(self.search_by.get())+"LIKE '%"+str(self.search_tx.get())+"%'")



        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
  

        
    def admin(self):
        self.root=root
        self.root.title("Admin Registration")
        self.root.geometry("1350x700+0+0")

        
        

        title1=Label(self.root,text="Admin Registration",font=("times new roman",40,"bold"),bg="pink",fg="red",bd=10,relief=GROOVE)
        title1.place(x=0,y=0,relwidth=1)
     
        
        frame_reg1=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        frame_reg1.place(x=300,y=77,width=700,height=620)


        ss='Register Yourself'    
        sliderlabel=Label(frame_reg1,text=ss,font=("chiller",20,"italic bold"),relief=GROOVE,borderwidth=5,width=26,bg="cyan")
        sliderlabel.place(x=198,y=0)

        frame_reg2=Frame(self.root,bd=4,relief=RIDGE,bg="grey")
        frame_reg2.place(x=0,y=77,width=300,height=620)

        frame_reg2=Frame(self.root,bd=4,relief=RIDGE,bg="grey")
        frame_reg2.place(x=1000,y=77,width=350,height=620)
 
        
        
        reg_text1=Label(frame_reg1,text="First Name",font=("times new roman",18,"bold"),fg="green").grid(row=1,column=0,padx=90,pady=70,sticky="w")
        reg_entry1=Entry(frame_reg1,bd=4,relief=GROOVE,font=("",15,"bold")).grid(row=1,column=1,padx=20,pady=15)

        reg_text2=Label(frame_reg1,text="Last Name",font=("times new roman",18,"bold"),fg="green").grid(row=2,column=0,padx=90,pady=5,sticky="w")
        reg_entry2=Entry(frame_reg1,bd=4,relief=GROOVE,font=("",15,"bold")).grid(row=2,column=1,padx=20,pady=15)

        
        reg_text3=Label(frame_reg1,text="Password",font=("times new roman",18,"bold"),fg="green").grid(row=3,column=0,padx=90,pady=65,sticky="w")
        reg_entry3=Entry(frame_reg1,bd=4,relief=GROOVE,font=("",15,"bold")).grid(row=3,column=1,padx=20,pady=15)

        reg_text4=Label(frame_reg1,text="Confirm",font=("times new roman",18,"bold"),fg="green").grid(row=4,column=0,padx=90,pady=5,sticky="w")
        reg_entry4=Entry(frame_reg1,bd=4,relief=GROOVE,font=("",15,"bold")).grid(row=4,column=1,padx=20,pady=15)

        reg_btn=Button(frame_reg1,text="Submit",width=15,command=self.admin_data,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=8,columnspan=1,padx=15,pady=75)   
        reg_back=Button(frame_reg1,text="Back",width=6,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=8,column=1,padx=7,pady=75)   

    
    def admin_data(self):
        print('inside admin data')
        con=pymysql.connect(host="localhost",user="root",password="",database="stms")
        cur=con.cursor()
        cur.execute("insert into admin values(%s,%s,%s,%s)",(self.Firstname.get(),
                                                                        self.Lastname.get(),
                                                                        self.Password.get(),
                                                                        self.Confirm.get()
                                                                    ))
        con.commit()
        con.close()
        messagebox.showinfo("success","Added successfully")


        
root=Tk()
obj=Login_system(root)
root=mainloop()