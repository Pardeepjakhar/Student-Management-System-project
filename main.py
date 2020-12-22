from tkinter import *
import random
import time
from tkinter import Toplevel
from tkinter import messagebox,filedialog
import pandas
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql

def login():
    def submitdb():
        global con, mycursor
        host = hostentry.get()
        users = userentry.get()
        password = passentry.get()
        try:
            print("in try")
            con = pymysql.connect(host=host, user=users, password=password)
            mycursor = con.cursor()
            print("after that")
            messagebox.showinfo("Notification","Connected successfully")
        except:
            messagebox.showerror("Notification", "Data is incorrect please try again")
            return
        try:
            strr = "create database studentmanagement"
            mycursor.execute(strr)
            strr = "use studentmanagement"
            mycursor.execute(strr)
            strr = "Create table studentdata(id int,name varchar(15),Mobile_No varchar(12),Email varchar(30),Address varchar(100),Gender varchar(10),DOB varchar(20),Date varchar(15),Time varchar(15))"
            mycursor.execute(strr)
            strr = "alter table studentdata modify column id int not null"
            mycursor.execute(strr)
            strr = "alter table studentdata modify column id int primary key"
            mycursor.execute(strr)
            messagebox.showinfo("Notification", "Database is created and you are connectd to database", parent=droot)

        except:
            strr = "use studentmanagement"
            mycursor.execute(strr)
            messagebox.showinfo("Notification", "Now you are connectd to database", parent=droot)

        droot.destroy()

    droot = Toplevel()
    droot.grab_set()
    droot.title("Login ")
    droot.geometry("360x250+700+300")
    droot.config(bg="blue")
    droot.resizable(False, False)

    hostentry = StringVar()
    userentry = StringVar()
    passentry = StringVar()

    hostlb = Label(droot, text="Enter Host :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    hostlb.place(x=10, y=20)

    hostent = Entry(droot, textvariable=hostentry, font="lucida 15 bold", relief=GROOVE, width=14)
    hostent.place(x=193, y=20)

    userlb = Label(droot, text="Enter User:  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    userlb.place(x=10, y=80)
    userent = Entry(droot, textvariable=userentry, font="lucida 15 bold", relief=GROOVE, width=14)
    userent.place(x=193, y=80)

    passlb = Label(droot, text="Enter Password:  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    passlb.place(x=10, y=140)
    passent = Entry(droot, textvariable=passentry, font="lucida 15 bold", relief=GROOVE, width=14)
    passent.place(x=193, y=140)

    subbtan = Button(droot, text="Submit", font="lucida 15 bold", bg="red", activebackground="blue",
                     activeforeground="white", width=13, command=submitdb)
    subbtan.place(x=120, y=190)

    droot.mainloop()

def tick():
    strrdate=time.strftime("%d/%m/%y")
    strrtime=time.strftime("%H:%M:%S")
    clock.config(text="Date:-" + strrdate+"\n"+"Time:-"+strrtime)

    clock.after(200,tick)


color=["red","green","blue","pink","gray","cyan","gold","gold2"]
def Introlabelcolor():
    fg=random.choice(color)
    sliderlabel.config(fg=fg)
    sliderlabel.after(200,Introlabelcolor)
def Introlabel():
    global count,text
    if (count>=len(ss)):
        count=0
        text=""
        sliderlabel.config(text=text)
    else:
        text=text+ss[count]
        sliderlabel.config(text=text)
        count+=1
    sliderlabel.after(200,Introlabel)

def add():
    def addstudent():
        id=Identry.get()
        name=nameentry.get()
        mobile=mobentry.get()
        address = addressentry.get()
        email = emailentry.get()
        gender=genentry.get()
        dob=dobentry.get()
        date=time.strftime("%d/%m/%y")
        Time=time.strftime("%H:%M:%S")
        try:
            strr="insert into studentdata (id,name,Mobile_No,Email,Address,Gender,DOB,Date,Time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(id,name,mobile,email,address,gender,dob,date,Time)
            mycursor.execute(strr,val)
            con.commit()
            res=messagebox.askyesnocancel("Notificiation","id {},Name {} is Added succcess ",parent=addroot)
            if (res==True):
               Identry.set("")
               nameentry.set("")
               mobentry.set("")
               genentry.set("")
               dobentry.set("")
               addressentry.set("")
               emailentry.set("")
        except:
           messagebox.showerror("Notification","Id already Exist try another",parent=addroot)

        strr="select * from studentdata"
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    addroot = Toplevel(master=btnframe)
    addroot.grab_set()
    addroot.title("Login ")
    addroot.geometry("380x470+250+150")
    addroot.config(bg="blue")
    addroot.resizable(False, False)

    Identry = StringVar()
    nameentry = StringVar()
    mobentry = StringVar()
    genentry = StringVar()
    dobentry = StringVar()
    addressentry = StringVar()
    emailentry = StringVar()

    Id = Label(addroot, text="Enter Id :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    Id.place(x=10, y=20)

    ident = Entry(addroot, textvariable=Identry, font="lucida 15 bold", relief=GROOVE, width=14)
    ident.place(x=193, y=20)

    namelb = Label(addroot, text="Enter Name:  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    namelb.place(x=10, y=80)

    nament = Entry(addroot, textvariable=nameentry, font="lucida 15 bold", relief=GROOVE, width=14)
    nament.place(x=193, y=80)

    mobilelb = Label(addroot, text="Enter Mobile:  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    mobilelb.place(x=10, y=140)
    mobent = Entry(addroot, textvariable=mobentry, font="lucida 15 bold", relief=GROOVE, width=14)
    mobent.place(x=193, y=140)

    maillb = Label(addroot, text="Enter Mail :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    maillb.place(x=10, y=200)

    mailent = Entry(addroot, textvariable=emailentry, font="lucida 15 bold", relief=GROOVE, width=14)
    mailent.place(x=193, y=200)

    addresslb = Label(addroot, text="Enter Address :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    addresslb.place(x=10, y=260)

    addresstent = Entry(addroot, textvariable=addressentry, font="lucida 15 bold", relief=GROOVE, width=14)
    addresstent.place(x=193, y=260)

    genderlb = Label(addroot, text="Enter Gender :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    genderlb.place(x=10, y=320)

    genent = Entry(addroot, textvariable=genentry, font="lucida 15 bold", relief=GROOVE, width=14)
    genent.place(x=193, y=320)

    doblb = Label(addroot, text="Enter D.O.B",font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    doblb.place(x=10, y=380)

    dobent = Entry(addroot, textvariable=dobentry, font="lucida 15 bold", relief=GROOVE, width=14)
    dobent.place(x=193, y=380)

    addbtan = Button(addroot, text="Submit", font="lucida 15 bold", bg="red", activebackground="blue",
                     activeforeground="white", width=13,command=addstudent)
    addbtan.place(x=120, y=420)

    addroot.mainloop()
def search():
    def searc():
        id = Identry.get()
        name = nameentry.get()
        mobile = mobentry.get()
        address = addressentry.get()
        email = emailentry.get()
        gender = genentry.get()
        dob = dobentry.get()

        if id !='':
           strr="select * from studentdata where id=%s "
           mycursor.execute(strr,id)
           datas=mycursor.fetchall()
           studenttable.delete(*studenttable.get_children())
           for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)


        if name !='':
            strr = "select * from studentdata where  name=%s"
            #val = (id, name, mobile, email, address, gender, dob)
            print(list[i])
            mycursor.execute(strr)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)

        if mobile !='':
            strr="select * from studentdata where Mobile_No=%s"
            mycursor.execute(strr,mobile)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)



        if email !='':
            strr="select * from studentdata where Email=%s"
            mycursor.execute(strr,email)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)

        if address != '':
            strr = "select * from studentdata where Address=%s"
            mycursor.execute(strr, address)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        if gender !='':
            strr="select * from studentdata where Gender=%s"
            mycursor.execute(strr,gender)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)

        if dob != '':
            strr = "select * from studentdata where DOB=%s"
            mycursor.execute(strr, dob)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)


    searchroot = Toplevel(master=btnframe)
    searchroot.grab_set()
    searchroot.title("Login ")
    searchroot.geometry("380x500+250+130")
    searchroot.config(bg="red")
    searchroot.resizable(False, False)

    Identry = StringVar()
    nameentry = StringVar()
    mobentry = StringVar()
    genentry = StringVar()
    dobentry = StringVar()
    addressentry = StringVar()
    emailentry = StringVar()
    dateentry=StringVar()

    Id = Label(searchroot, text="Enter Id :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
               bg="gold2", anchor=W)
    Id.place(x=10, y=20)

    ident = Entry(searchroot, textvariable=Identry, font="lucida 15 bold", relief=GROOVE, width=14)
    ident.place(x=193, y=20)

    namelb = Label(searchroot, text="Enter Name:  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    namelb.place(x=10, y=70)

    nament = Entry(searchroot, textvariable=nameentry, font="lucida 15 bold", relief=GROOVE, width=14)
    nament.place(x=193, y=70)

    mobilelb = Label(searchroot, text="Enter Mobile:  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                     bg="gold2", anchor=W)
    mobilelb.place(x=10, y=120)
    mobent = Entry(searchroot, textvariable=mobentry, font="lucida 15 bold", relief=GROOVE, width=14)
    mobent.place(x=193, y=120)

    maillb = Label(searchroot, text="Enter Mail :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    maillb.place(x=10, y=170)

    mailent = Entry(searchroot, textvariable=emailentry, font="lucida 15 bold", relief=GROOVE, width=14)
    mailent.place(x=193, y=170)

    addresslb = Label(searchroot, text="Enter Address :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                      bg="gold2", anchor=W)
    addresslb.place(x=10, y=220)

    addresstent = Entry(searchroot, textvariable=addressentry, font="lucida 15 bold", relief=GROOVE, width=14)
    addresstent.place(x=193, y=220)

    genderlb = Label(searchroot, text="Enter Gender :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                     bg="gold2", anchor=W)
    genderlb.place(x=10, y=270)

    genent = Entry(searchroot, textvariable=genentry, font="lucida 15 bold", relief=GROOVE, width=14)
    genent.place(x=193, y=270)

    doblb = Label(searchroot, text="Enter D.O.B", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                  bg="gold2", anchor=W)
    doblb.place(x=10, y=320)

    dobent = Entry(searchroot, textvariable=dobentry, font="lucida 15 bold", relief=GROOVE, width=14)
    dobent.place(x=193, y=320)

    datelb = Label(searchroot, text="Enter Date:", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                  bg="gold2", anchor=W)
    datelb.place(x=10, y=370)

    datent = Entry(searchroot, textvariable=dateentry, font="lucida 15 bold", relief=GROOVE, width=14)
    datent.place(x=193, y=370)

    searchnbtan = Button(searchroot, text="Submit", font="lucida 15 bold", bg="blue", activebackground="red",
                     activeforeground="white", width=13,command=searc)
    searchnbtan.place(x=120, y=420)

    searchroot.mainloop()

def delet():
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values'][0]
    strr='delete from studentdata where id=%s'
    mycursor.execute(strr,pp)
    con.commit()
    messagebox.showinfo("Notofication"," Id {} is deleted successfully".format(pp))
    strr="select * from studentdata"
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vv)

def update():
    def updt():
        id = Identry.get()
        name = nameentry.get()
        mobile = mobentry.get()
        address = addressentry.get()
        email = emailentry.get()
        gender = genentry.get()
        dob = dobentry.get()
        time=timeentry.get()
        date=dateentry.get()
        strr="update studentdata set name=%s,Mobile_No=%s,Email=%s,Address=%s,Gender=%s,DOB=%s,Time=%s,Date=%s where id=%s"
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,time,date,id))
        con.commit()
        messagebox.showinfo('Notification',"Id {} is updated successfully".format(id),parent=updateroot)
        strr = "select * from studentdata"
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=btnframe)
    updateroot.grab_set()
    updateroot.title("Login ")
    updateroot.geometry("380x520+250+130")
    updateroot.config(bg="red")
    updateroot.resizable(False, False)

    Identry = StringVar()
    nameentry = StringVar()
    mobentry = StringVar()
    genentry = StringVar()
    dobentry = StringVar()
    addressentry = StringVar()
    emailentry = StringVar()
    dateentry=StringVar()
    timeentry=StringVar()

    Id = Label(updateroot, text="Update Id :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
               bg="gold2", anchor=W)
    Id.place(x=10, y=20)

    ident = Entry(updateroot, textvariable=Identry, font="lucida 15 bold", relief=GROOVE, width=14)
    ident.place(x=193, y=20)

    namelb = Label(updateroot, text="Update Name:  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    namelb.place(x=10, y=70)

    nament = Entry(updateroot, textvariable=nameentry, font="lucida 15 bold", relief=GROOVE, width=14)
    nament.place(x=193, y=70)

    mobilelb = Label(updateroot, text="Update Mobile:  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                     bg="gold2", anchor=W)
    mobilelb.place(x=10, y=120)
    mobent = Entry(updateroot, textvariable=mobentry, font="lucida 15 bold", relief=GROOVE, width=14)
    mobent.place(x=193, y=120)

    maillb = Label(updateroot, text="Update Mail :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    maillb.place(x=10, y=170)

    mailent = Entry(updateroot, textvariable=emailentry, font="lucida 15 bold", relief=GROOVE, width=14)
    mailent.place(x=193, y=170)

    addresslb = Label(updateroot, text="Update Address :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                      bg="gold2", anchor=W)
    addresslb.place(x=10, y=220)

    addresstent = Entry(updateroot, textvariable=addressentry, font="lucida 15 bold", relief=GROOVE, width=14)
    genderlb = Label(updateroot, text="Update Gender :  ", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                     bg="gold2", anchor=W)
    genderlb.place(x=10, y=270)

    genent = Entry(updateroot, textvariable=genentry, font="lucida 15 bold", relief=GROOVE, width=14)
    genent.place(x=193, y=270)

    doblb = Label(updateroot, text="Update D.O.B", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                  bg="gold2", anchor=W)
    doblb.place(x=10, y=320)
    addresstent.place(x=193, y=220)


    dobent = Entry(updateroot, textvariable=dobentry, font="lucida 15 bold", relief=GROOVE, width=14)
    dobent.place(x=193, y=320)

    datelb = Label(updateroot, text="Update Date:", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                  bg="gold2", anchor=W)
    datelb.place(x=10, y=370)

    datent = Entry(updateroot, textvariable=dateentry, font="lucida 15 bold", relief=GROOVE, width=14)
    datent.place(x=193, y=370)

    timelb = Label(updateroot, text="Enter Time:", font="lucida 15 bold", relief=GROOVE, width=13, borderwidth=3,
                   bg="gold2", anchor=W)
    timelb.place(x=10, y=420)

    timeent = Entry(updateroot, textvariable=timeentry, font="lucida 15 bold", relief=GROOVE, width=14)
    timeent.place(x=193, y=420)

    searchnbtan = Button(updateroot, text="Submit", font="lucida 15 bold", bg="blue", activebackground="red",
                     activeforeground="white", width=13,command=updt)
    searchnbtan.place(x=120, y=470)

    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values']
    if len(pp)!='':
        Identry.set(pp[0])
        nameentry.set(pp[1])
        mobentry.set(pp[2])
        emailentry.set(pp[3])
        addressentry.set(pp[4])

        genentry.set(pp[5])
        dobentry.set(pp[6])
        dateentry.set([7])
        timeentry.set([8])


    updateroot.mainloop()


def show():

    strr = "select * from studentdata"
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def export():
    ff=filedialog.asksaveasfilename()
    gg=studenttable.get_children()
    id, name,mobile,email,address,gender,dob,date,time=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=studenttable.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),time.append(pp[7]),date.append(pp[8])
    dd=['id','name','Mobile_No','Email','Address','Gender','DOB','Time','Date']
    df=pandas.DataFrame(list(zip(id, name,mobile,email,address,gender,dob,date,time)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification','Student data is Saved {}'.format(paths))


def Exit():
     res=messagebox.askyesnocancel("Notification","Do you want to exit")
     if res==True:
         root.destroy()

######################################################################### Main Root window is start here  #############################################################3

root=Tk()
root.config(bg="gold2")
root.geometry("1440x690+0+0")
root.title("Student Management System")
root.resizable(False,False)

######### Frames ######3
btnframe=Frame(root,bg="gold2",relief=GROOVE,borderwidth=6)
btnframe.place(x=20,y=70,width=350,height=610,)

welcome=Label(btnframe,text="------------Welcome-------------",width="30",font="arial 25 bold",bd=5,bg="gold2")
welcome.pack(side=TOP,expand=True)

addbtn=Button(btnframe,text="1.ADD Student" ,width="25",font="arial 13 bold",bd=5,bg="skyblue",relief=RIDGE,activebackground="blue",activeforeground="white",command=add)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(btnframe,text="2. Search Student" ,width="25",font="arial 13 bold",bd=5,bg="skyblue",relief=RIDGE,activebackground="blue",activeforeground="white",command=search)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(btnframe,text="3. Delete  Student" ,width="25",font="arial 13 bold",bd=5,bg="skyblue",relief=RIDGE,activebackground="blue",activeforeground="white",command=delet)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(btnframe,text="4. Update Student" ,width="25",font="arial 13 bold",bd=5,bg="skyblue",relief=RIDGE,activebackground="blue",activeforeground="white",command=update)
updatebtn.pack(side=TOP,expand=True)

showbtn=Button(btnframe,text="5.Show All" ,width="25",font="arial 13 bold",bd=5,bg="skyblue",relief=RIDGE,activebackground="blue",activeforeground="white",command=show)
showbtn.pack(side=TOP,expand=True)

exportbtn=Button(btnframe,text="6. Export Data" ,width="25",font="arial 13 bold",bd=5,bg="skyblue",relief=RIDGE,activebackground="blue",activeforeground="white",command=export)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(btnframe,text="7. Exit" ,width="25",font="arial 13 bold",bd=5,bg="skyblue",relief=RIDGE,activebackground="blue",activeforeground="white",command=Exit)
exitbtn.pack(side=TOP,expand=True)


########################################################################### This is show data frame here we se aal the data ########################

entryframe=Frame(root,bg="gold2",relief=GROOVE,borderwidth=6)
entryframe.place(x=370,y=70,width=1000,height=610)

style= ttk.Style()
style.configure("Treeview.Heading",font="lucida 15 bold", fg="black2")
style.configure("Treeview",fg="black",bg="red",font="times 13 bold" )

scroll_y=Scrollbar(entryframe,orient=VERTICAL)
scroll_x=Scrollbar(entryframe,orient=HORIZONTAL)

studenttable=Treeview(entryframe,column=("Id","Name","Mobile No","Email","Address","Gender","D.O.B","Added Date","Added Time"),yscrollcommand=scroll_y.set,
                      xscrollcommand=scroll_x.set)


scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading("Id",text="Id")
studenttable.heading("Name",text="Name")
studenttable.heading("Mobile No",text="Mobile No")
studenttable.heading("Email",text="Email")
studenttable.heading("Address",text="Address")
studenttable.heading("Gender",text="Gender")
studenttable.heading("D.O.B",text="D.O.B")
studenttable.heading("Added Date",text="Date")
studenttable.heading("Added Time",text="Time")
studenttable["show"]="headings"
studenttable.pack(fill=BOTH,expand=1)
studenttable.column("Id",width=50)
studenttable.column("Name",width=180)
studenttable.column("Mobile No",width=120)
studenttable.column("Email",width=200)
studenttable.column("Address",width=200)
studenttable.column("Gender",width=100)
studenttable.column("D.O.B",width=100)
studenttable.column("Added Date",width=100)
studenttable.column("Added Time",width=100)

############### Labels for sliders ##############
ss="Welcome to Student Management"
count=0
text=""

sliderlabel=Label(root,text=ss,relief=GROOVE,font="lucida 18 bold",bg="cyan",borderwidth=4,width=35)
sliderlabel.place(x=400,y=0)
Introlabel()
Introlabelcolor()

############33 Labels for clock    ##########
clock=Label(root ,bg="green",relief=GROOVE,font="lucida 15 bold",borderwidth=4)
clock.place(x=0,y=0)
tick()

###########33########### connection  Button   ###################

cbtn=Button(root,bg="green",text="Connect to database",relief=GROOVE,font="lucida 18 bold",borderwidth=4,
            activebackground="blue",activeforeground="white",command=login)
cbtn.place(x=1070,y=0)



root.mainloop()