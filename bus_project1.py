import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk,Image


def home():
    parent=tk.Tk()
    parent.geometry("500x500")
    parent.configure(bg="darkolivegreen4")

    frame=tk.Frame(parent,width=500,height=250)
    frame.place(relx=0.0)
    img=ImageTk.PhotoImage(Image.open("big.jpg"))
    
    frame1=tk.Frame(parent,bg='orange',height=90,width=1600).place(relx=0.0,rely=0.1)
    f=font.Font(parent,weight="bold",family="times new roman",size=40)
    x=tk.Label(frame1,text="bus ticket booking system",font=f)
    x.configure(bg="orange",fg="black")
    x.place(relx=0.3,rely=0.1)

    
    label=tk.Label(frame,image=img).pack()
    f=font.Font(weight="bold",family="Trebuchet MS",size=20)
    b=tk.Button(parent,text="customer_Login",bg="skyblue",activebackground="#FC92C4",command=customer_login).place(relx=.10,rely=.5)
    c=tk.Button(parent,text="customer_register",bg="skyblue",activebackground="#FC92C4",command=customer_register).place(relx=.30,rely=.5)
    d=tk.Button(parent,text="ticket_details",bg="skyblue",activebackground="#FC92C4",command=ticket_details).place(relx=.50,rely=.5)
    e=tk.Button(parent,text="running_buses",bg="skyblue",activebackground="#FC92C4",command=running_buses).place(relx=.65,rely=.5)
    f=tk.Button(parent,text="bus_booknow",bg="skyblue",activebackground="#FC92C4",command=running_buses).place(relx=.78,rely=.5)
    

    parent.mainloop()
    

def customer_login():      
    parent = tk.Tk()
    parent.geometry("600x600")
    parent.title("Login Form")
    

    frame1=tk.Frame(parent,bg="yellow",height=20,width=1900).place(anchor='w',relx=.0,rely=.0)
    label_wel=tk.Label(parent,text="bus ticket booking",font=("times new roman",20),bg="#000000",fg="#DC143C")
    label_wel.configure(bg="darkolivegreen4")
    label_wel.pack(pady=20)


    font_21=font.Font(weight="bold",family="trebuchet Ms",size=30)
    tk.Label(parent,text="username",bg="#0052cc",font=(font_21)).place(relx=0.1,rely=0.15)
    entry_username=tk.Entry(parent,width=20,font='arial 18')
    entry_username.place(relx=0.3,rely=0.15)
         

    font_22=font.Font(weight="bold",family="trebuchet Ms",size=30)
    tk.Label(parent,text="password",bg="#0052cc",font=(font_22)).place(relx=0.1,rely=0.30)
    entry_passw=tk.Entry(parent,width=20,font='arial 18')
    entry_passw.place(relx=0.3,rely=0.30)


    def login():
       userid =entry_username.get()
       passw =entry_passw.get()
   
       if userid and passw:
           messagebox.showinfo("Login Successful", "Welcome to our bank")
       else:
           messagebox.showerror("Login Failed", "Invalid username or password")



    font_button=font.Font(weight="bold",family="trebuchet Ms",size=30)
    login_button=tk.Button(parent,text="login",bg="lightgreen",activebackground="#90ee90",command=login,font=(font_button))
    login_button.place(relx=0.40,rely=0.45)


def customer_register():
    parent = tk.Tk()
    parent.geometry("600x600")
    parent.title("register Form")
    label_wel=tk.Label(parent,text="bus ticket booking",font=("times new roman",30),bg="#000000",fg="#DC143C")
    label_wel.configure(bg="darkolivegreen4")
    label_wel.pack(pady=30)

    
    font_21=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="bus_number:",bg="cyan4",font=font_21).place(relx=0.1,rely=0.15)
    entry_bus_number=tk.Entry(parent,width=20,font='arial 18')
    entry_bus_number.place(relx=0.3,rely=0.15)

    font_22=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="bus_name:",bg="cyan4",font=font_22).place(relx=0.1,rely=0.25)
    entry_bus_name=tk.Entry(parent,width=20,font='arial 18')
    entry_bus_name.place(relx=0.3,rely=0.25)

    font_23=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="bus_route:",bg="cyan4",font=font_23).place(relx=0.1,rely=0.35)
    entry_bus_route=tk.Entry(parent,width=20,font='arial 18')
    entry_bus_route.place(relx=0.3,rely=0.35)

    font_24=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="seat_charge",bg="cyan4",font=font_24).place(relx=0.1,rely=0.45)
    entry_seat_charge=tk.Entry(parent,width=20,font='arial 18')
    entry_seat_charge.place(relx=0.3,rely=0.45)

    
    def register():
        bus_number = entry_bus_number.get()
        bus_name = entry_bus_name.get()
        bus_route=entry_bus_route.get()
        seat_charge=entry_seat_charge.get()

   
        if bus_number  and bus_name  and  bus_route and seat_charge:
            messagebox.showinfo("Login Successful", "Welcome to our bank")
        else:
           messagebox.showerror("Login Failed", "Invalid username or password")


    font_button=font.Font(weight="bold",family="trebuchet Ms",size=30)
    register_button=tk.Button(parent,text="register",bg="lightgreen",activebackground="#90ee90",command=register,font=(font_button))
    register_button.place(relx=0.40,rely=0.55)

def ticket_details():
    parent = tk.Tk()
    parent.geometry("600x600")
    parent.title("ticket Form")
    label_wel=tk.Label(parent,text="bus ticket booking",font=("times new roman",30),bg="#000000",fg="#DC143C")
    label_wel.configure(bg="darkolivegreen4")
    label_wel.pack(pady=30)

    
    font_21=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="booking_id:",bg="cyan4",font=font_21).place(relx=0.1,rely=0.15)
    entry_booking_id=tk.Entry(parent,width=20,font='arial 18')
    entry_booking_id.place(relx=0.3,rely=0.15)

    font_22=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="bus_name:",bg="cyan4",font=font_22).place(relx=0.1,rely=0.25)
    entry_bus_name=tk.Entry(parent,width=20,font='arial 18')
    entry_bus_name.place(relx=0.3,rely=0.25)

    font_23=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="contact_no:",bg="cyan4",font=font_23).place(relx=0.1,rely=0.35)
    entry_contact_no=tk.Entry(parent,width=20,font='arial 18')
    entry_contact_no.place(relx=0.3,rely=0.35)

    
    def booknow():
        booking_id = entry_booking_id.get()
        bus_name = entry_bus_name.get()
        contact_no=entry_contact_no.get()
        
        if booking_id  and bus_name  and  contact_no:
            messagebox.showinfo("Login Successful", "Welcome to our bank")
        else:
           messagebox.showerror("Login Failed", "Invalid username or password")


    font_button=font.Font(weight="bold",family="trebuchet Ms",size=30)
    booknow_button=tk.Button(parent,text="booknow",bg="lightgreen",activebackground="#90ee90",command=booknow,font=(font_button))
    booknow_button.place(relx=0.40,rely=0.55)    


def running_buses():
    parent = tk.Tk()
    parent.geometry("600x600")
    parent.title("book form")
    label_wel=tk.Label(parent,text="bus ticket booking",font=("times new roman",30),bg="#000000",fg="#DC143C")
    label_wel.configure(bg="darkolivegreen4")
    label_wel.pack(pady=30)

    
    font_21=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="bus_number:",bg="cyan4",font=font_21).place(relx=0.1,rely=0.15)
    entry_bus_number=tk.Entry(parent,width=20,font='arial 18')
    entry_bus_number.place(relx=0.3,rely=0.15)

    font_22=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="bus_name:",bg="cyan4",font=font_22).place(relx=0.1,rely=0.25)
    entry_bus_name=tk.Entry(parent,width=20,font='arial 18')
    entry_bus_name.place(relx=0.3,rely=0.25)

    font_23=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="bus_route:",bg="cyan4",font=font_23).place(relx=0.1,rely=0.35)
    entry_bus_route=tk.Entry(parent,width=20,font='arial 18')
    entry_bus_route.place(relx=0.3,rely=0.35)

    font_24=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="bus_time",bg="cyan4",font=font_24).place(relx=0.1,rely=0.45)
    entry_bus_time=tk.Entry(parent,width=20,font='arial 18')
    entry_bus_time.place(relx=0.3,rely=0.45)

    font_25=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="seat_charge",bg="cyan4",font=font_25).place(relx=0.1,rely=0.55)
    entry_seat_charge=tk.Entry(parent,width=20,font='arial 18')
    entry_seat_charge.place(relx=0.3,rely=0.55)

    
    def sumit():
        bus_number = entry_bus_number.get()
        bus_name = entry_bus_name.get()
        bus_route=entry_bus_route.get()
        bus_time=entry_bus_time.get()
        seat_charge=entry_seat_charge.get()

   
        if bus_number  and bus_name  and  bus_route and bus_time and seat_charge:
            messagebox.showinfo("Login Successful", "Welcome to our bank")
        else:
           messagebox.showerror("Login Failed", "Invalid username or password")


    font_button=font.Font(weight="bold",family="trebuchet Ms",size=30)
    sumit_button=tk.Button(parent,text="sumit",bg="lightgreen",activebackground="#90ee90",command=sumit,font=(font_button))
    sumit_button.place(relx=0.40,rely=0.65)

def bus_booknow():
    parent = tk.Tk()
    parent.geometry("600x600")
    parent.title("book form")
    label_wel=tk.Label(parent,text="bus ticket booking",font=("times new roman",30),bg="#000000",fg="#DC143C")
    label_wel.configure(bg="darkolivegreen4")
    label_wel.pack(pady=30)

    
    font_21=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="name:",bg="cyan4",font=font_21).place(relx=0.1,rely=0.15)
    entry_name=tk.Entry(parent,width=20,font='arial 18')
    entry_name.place(relx=0.1,rely=0.15)

    font_22=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="ticket_id:",bg="cyan4",font=font_22).place(relx=0.1,rely=0.25)
    entry_ticket_id=tk.Entry(parent,width=20,font='arial 18')
    entry_ticket_id.place(relx=0.1,rely=0.25)

    font_23=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="booking_date:",bg="cyan4",font=font_23).place(relx=0.1,rely=0.35)
    entry_booking_date=tk.Entry(parent,width=20,font='arial 18')
    entry_booking_date.place(relx=0.1,rely=0.35)

    font_24=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="bus_time",bg="cyan4",font=font_24).place(relx=0.1,rely=0.45)
    entry_bus_time=tk.Entry(parent,width=20,font='arial 18')
    entry_bus_time.place(relx=0.1,rely=0.45)

    font_25=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="phone_no",bg="cyan4",font=font_24).place(relx=0.1,rely=0.45)
    entry_bus_time=tk.Entry(parent,width=20,font='arial 18')
    entry_bus_time.place(relx=0.1,rely=0.55)

    font_26=font.Font(weight="bold",family="Trebuchet MS",size=30)
    tk.Label(parent,text="seat_charge",bg="cyan4",font=font_24).place(relx=0.1,rely=0.55)
    entry_seat_charge=tk.Entry(parent,width=20,font='arial 18')
    entry_seat_charge.place(relx=0.1,rely=0.65)

    
    def busbook():
        name = entry_name.get()
        ticket_id = entry_ticket_id.get()
        booking_date=entry_booking_date.get()
        bus_time=entry_bus_time.get()
        seat_charge=entry_seat_charge.get()

   
        if name  and ticket_id and  booking_date and bus_time and seat_charge:
            messagebox.showinfo("Login Successful", "Welcome to our bank")
        else:
           messagebox.showerror("Login Failed", "Invalid username or password")


    font_button=font.Font(weight="bold",family="trebuchet Ms",size=30)
    busbook_button=tk.Button(parent,text="busbook",bg="lightgreen",activebackground="#90ee90",command=busbook,font=(font_button))
    busbook_button.place(relx=0.40,rely=0.75)
    
    

home()    

    

    
    
