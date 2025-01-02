import tkinter as tk
from tkinter import font
from PIL import ImageTk,Image
from tkinter import messagebox


def home():
    root=tk.Tk()
    root.geometry("900x800")
    root.configure(bg="cyan4")

    frame=tk.Frame(root,width=20,height=30)
    frame.place(rely=0.0)
    img=ImageTk.PhotoImage(Image.open("big.jpg"))
    label=tk.Label(frame,image=img).pack()

    frame=tk.Frame(root,bg='orange',height=90,width=1600).place(relx=0.0,rely=0.1)
    f=font.Font(root,weight="bold",family="times new roman",size=40)
    x=tk.Label(frame,text="K2 BUS TICKET BOOKING",font=f)
    x.configure(bg="orange",fg="black")
    x.place(relx=0.3,rely=0.1)


    f=font.Font(weight="bold",family="times new roman",size=20)
    t="""**THE ROAD IS MAY BE
               LONG BUT THE MEMORIES
                    ARE FOREVER**"""
    tk.Label(root,text=t,font=f,bg="black",fg="white").place(relx=0.30,rely=0.40)

    
    but1=font.Font(weight="bold",family="Trebuchet MS",size=20)
    mani1_but=tk.Button(root,text="TICKET BOOKING",command=main1,font=but1)
    mani1_but.place(relx=0.30,rely=0.70)

    mani2_but=tk.Button(root,text="BUS DETAILS",command=bus_dt,font=but1)
    mani2_but.place(relx=0.50,rely=0.70)


    root.mainloop()
    
def main1():
    root1=tk.Tk()
    root1.geometry("900x900")
    
    f=font.Font(root1,weight="bold",family="times new roman",size=40)
    x=tk.Label(root1,text="K2 BUS TICKET BOOKING",font=f)
    x.configure(bg="orange",fg="black")
    x.place(relx=0.2,rely=0.1)


    frame=tk.Frame(root1,bg="grey",height=550,width=455)
    frame.place(relx=0.30,rely=0.20)

    home=tk.Label(root1,text="HOME",font='arial 10')
    home.place(relx=0.70,rely=0.01)
    ho=tk.Label(root1,text="|",font='arial 10')
    ho.place(relx=0.73,rely=0.01)
    ab=tk.Label(root1,text="ABOUT US",font='arial 10')
    ab.place(relx=0.74,rely=0.01)
    ho1=tk.Label(root1,text="|",font='arial 10')
    ho1.place(relx=0.79,rely=0.01)
    tc=tk.Label(root1,text="TERMS&CONDITIONS",font='arial 10')
    tc.place(relx=0.80,rely=0.01)
    

    name=tk.Label(root1,text="NAME:",font='arial 18',bg="grey")
    name.place(relx=0.32,rely=0.22)
    l1=tk.Entry(root1,width=20,font='arial 18')
    l1.place(relx=0.42,rely=0.22)
    dob=tk.Label(root1,text="DOB:",font='arial 18',bg="grey")
    dob.place(relx=0.32,rely=0.32)
    l2=tk.Entry(root1,width=20,font='arial 18')
    l2.place(relx=0.42,rely=0.32)
    plac=tk.Label(root1,text="EMAIL ID:",font='arial 18',bg="grey")
    plac.place(relx=0.32,rely=0.42)
    l3=tk.Entry(root1,width=20,font='arial 18')
    l3.place(relx=0.42,rely=0.42)
    number=tk.Label(root1,text="PNONE NO:",font='arial 18',bg="grey")
    number.place(relx=0.32,rely=0.52)
    l4=tk.Entry(root1,width=20,font='arial 18')
    l4.place(relx=0.42,rely=0.52)
    add=tk.Label(root1,text="ADDRESS:",font='arial 18',bg="grey")
    add.place(relx=0.32,rely=0.62)
    l5=tk.Entry(root1,width=20,font='arial 18')
    l5.place(relx=0.42,rely=0.62)

    bn=tk.Label(root1,text="BUS NO:",font='arial 18',bg="grey")
    bn.place(relx=0.32,rely=0.72)
    l6=tk.Entry(root1,width=20,font='arial 18')
    l6.place(relx=0.42,rely=0.72)

    sn=tk.Label(root1,text="SEAT NO:",font='arial 18',bg="grey")
    sn.place(relx=0.32,rely=0.72)
    l6=tk.Entry(root1,width=20,font='arial 18')
    l6.place(relx=0.42,rely=0.72)
    
    ft=tk.Label(root1,text="FROM-TO :",font='arial 18',bg="grey")
    ft.place(relx=0.32,rely=0.82)
    l7=tk.Entry(root1,width=20,font='arial 18')
    l7.place(relx=0.42,rely=0.82)



    def ma1():
        name=l1.get()
        dob=l2.get()
        place=l3.get()
        num=l4.get()

        if name and dob and place and num:
            messagebox.showinfo("WELCOME","Your ticket is booking......THANKING YOU")
        else:
            messagebox.showerror("failed","fill the all vales")

    mani1_but=tk.Button(root1,text="BOOKING",command=ma1,width=10,font='arial 15',bg="grey")
    mani1_but.place(relx=0.45,rely=0.90)


def bus_dt():
    root2=tk.Tk()
    root2.geometry("900x900")
    
    f=font.Font(root2,weight="bold",family="times new roman",size=40)
    x=tk.Label(root2,text="K2 BUS TICKET BOOKING",font=f)
    x.configure(bg="orange",fg="black")
    x.place(relx=0.2,rely=0.1)

    r1=tk.Label(root2,text="BUS_NO",font="arial 18",bg="grey")
    r1.place(relx=0.09,rely=0.25)
    r2=tk.Label(root2,text="TIMING",font="arial 18",bg="grey")
    r2.place(relx=0.18,rely=0.25)
    r3=tk.Label(root2,text="BUS_NAME",font="arial 18",bg="grey")
    r3.place(relx=0.29,rely=0.25)
    r4=tk.Label(root2,text=" FROM -- TO",font="arial 18",bg="grey")
    r4.place(relx=0.45,rely=0.25)
    r5=tk.Label(root2,text="DURATION",font="arial 18",bg="grey" )
    r5.place(relx=0.70,rely=0.25)
    #one
    t1=tk.Label(root2,text="1001",font="arial 18")
    t1.place(relx=0.10,rely=0.30)
    no1=tk.Label(root2,text="8.00pm",font="arial 18")
    no1.place(relx=0.17,rely=0.30)
    n1=tk.Label(root2,text="SR BUS",font="arial 18")
    n1.place(relx=0.30,rely=0.30)
    c1=tk.Label(root2,text="COIMBATORE TO CHNNAI",font="arial 18")
    c1.place(relx=0.40,rely=0.30)
    tr1=tk.Label(root2,text="3-4HOURS",width=10,font="arial 18")
    tr1.place(relx=0.70,rely=0.30)
    #two
    n2=tk.Label(root2,text="MINI BUS",width=20,font='arial 18')
    n2.place(relx=0.22,rely=0.36)
    c2=tk.Label(root2,text="CHENNAI TO TRICHY",font="arial 18")
    c2.place(relx=0.40,rely=0.36)
    tr2=tk.Label(root2,text="5-6HOURS",width=10,font="arial 18")
    tr2.place(relx=0.70,rely=0.36)
    t2=tk.Label(root2,text="1023",font="arial 18")
    t2.place(relx=0.10,rely=0.36)
    no2=tk.Label(root2,text="9.00pm",font="arial 18")
    no2.place(relx=0.17,rely=0.36)
    #three
    n3=tk.Label(root2,text="CG BUS",width=20,font='arial 18')
    n3.place(relx=0.22,rely=0.42)
    c3=tk.Label(root2,text="MAYILADUTHURAI TO CHENNAI",font="arial 18")
    c3.place(relx=0.40,rely=0.42)
    tr3=tk.Label(root2,text="6-7HOURS",width=10,font="arial 18")
    tr3.place(relx=0.70,rely=0.42)
    t3=tk.Label(root2,text="3421",font="arial 18")
    t3.place(relx=0.10,rely=0.42)
    no3=tk.Label(root2,text="8.00am",font="arial 18")
    no3.place(relx=0.17,rely=0.42)
    #zero
    n0=tk.Label(root2,text="PRIYA BUS",width=20,font='arial 18')
    n0.place(relx=0.22,rely=0.48)
    c0=tk.Label(root2,text="TUTICORIN TO CHENNAI",font="arial 18")
    c0.place(relx=0.40,rely=0.48)
    tr0=tk.Label(root2,text="9-8HOURS",width=10,font="arial 18")
    tr0.place(relx=0.70,rely=0.48)
    t0=tk.Label(root2,text="3981",font="arial 18")
    t0.place(relx=0.10,rely=0.48)
    no0=tk.Label(root2,text="6.00am",font="arial 18")
    no0.place(relx=0.17,rely=0.48)
    #four
    n4=tk.Label(root2,text="MANO BUS",width=20,font='arial 18')
    n4.place(relx=0.22,rely=0.54)
    c4=tk.Label(root2,text="SALEM TO CHENNAI",font="arial 18")
    c4.place(relx=0.40,rely=0.54)
    tr4=tk.Label(root2,text="4-5HOURS",width=10,font="arial 18")
    tr4.place(relx=0.70,rely=0.54)
    t4=tk.Label(root2,text="1221",font="arial 18")
    t4.place(relx=0.10,rely=0.54)
    no4=tk.Label(root2,text="12.00pm",font="arial 18")
    no4.place(relx=0.17,rely=0.54)
    #five
    n5=tk.Label(root2,text="DON BUS",width=20,font='arial 18')
    n5.place(relx=0.22,rely=0.60)
    c5=tk.Label(root2,text="MADURAI TO MAYILADUTHURAI",font="arial 18")
    c5.place(relx=0.40,rely=0.60)
    tr5=tk.Label(root2,text="5-6HOURS",width=10,font="arial 18")
    tr5.place(relx=0.70,rely=0.60)
    t5=tk.Label(root2,text="3761",font="arial 18")
    t5.place(relx=0.10,rely=0.60)
    no5=tk.Label(root2,text="3.00am",font="arial 18")
    no5.place(relx=0.17,rely=0.60)
    #six
    n6=tk.Label(root2,text="TOUR BUS",width=20,font='arial 18')
    n6.place(relx=0.22,rely=0.66)
    c6=tk.Label(root2,text="THANJAVUR TO MADURAI",font="arial 18")
    c6.place(relx=0.40,rely=0.66)
    tr6=tk.Label(root2,text="5-6HOURS",width=10,font="arial 18")
    tr6.place(relx=0.70,rely=0.66)
    t6=tk.Label(root2,text="4567",font="arial 18")
    t6.place(relx=0.10,rely=0.66)
    no6=tk.Label(root2,text="9.00am",font="arial 18")
    no6.place(relx=0.17,rely=0.66)
    #seven
    n7=tk.Label(root2,text="PK BUS",width=20,font='arial 18')
    n7.place(relx=0.22,rely=0.72)
    c7=tk.Label(root2,text="KANNIYAKUMARI TO SALEM",font="arial 18")
    c7.place(relx=0.40,rely=0.72)
    tr7=tk.Label(root2,text="6-7HOURS",width=10,font="arial 18")
    tr7.place(relx=0.70,rely=0.72)
    t7=tk.Label(root2,text="3231",font="arial 18")
    t7.place(relx=0.10,rely=0.72)
    no7=tk.Label(root2,text="8.00am",font="arial 18")
    no7.place(relx=0.17,rely=0.72)
    #eight
    n8=tk.Label(root2,text="NALAM BUS",width=20,font='arial 18')
    n8.place(relx=0.22,rely=0.78)
    c8=tk.Label(root2,text="TRICHY TO SALEM",font="arial 18")
    c8.place(relx=0.40,rely=0.78)
    tr8=tk.Label(root2,text="3-4HOURS",width=10,font="arial 18")
    tr8.place(relx=0.70,rely=0.78)
    t8=tk.Label(root2,text="9421",font="arial 18")
    t8.place(relx=0.10,rely=0.78)
    no8=tk.Label(root2,text="7.00pm",font="arial 18")
    no8.place(relx=0.17,rely=0.78)
    #nine
    n9=tk.Label(root2,text="ZEB BUS",width=20,font='arial 18')
    n9.place(relx=0.22,rely=0.84)
    c9=tk.Label(root2,text="RAMANADHAPURAM TO CHENNAI",font="arial 18")
    c9.place(relx=0.40,rely=0.84)
    tr9=tk.Label(root2,text="8-9HOURS",width=10,font="arial 18")
    tr9.place(relx=0.70,rely=0.84)
    t9=tk.Label(root2,text="3491",font="arial 18")
    t9.place(relx=0.10,rely=0.84)
    no9=tk.Label(root2,text="2.00pm",font="arial 18")
    no9.place(relx=0.17,rely=0.84)

home()

    
