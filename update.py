from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("D:/store management/Database/store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id=r[0]
class Database:
    def __init__(self, master,*args,**kwargs):
        self.master = master
        self.heading = Label(master,text="Update the database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=400,y=0)

        #label and entry for the id
        self.id_le = Label(master, text="Enter ID", font=('arial 18 bold'))
        self.id_le.place(x=0,y=70)
        
        self.id_leb  = Entry(master, width=10,font=('arial 18 bold'))
        self.id_leb.place(x=380,y=70)
        
        self.btn_search = Button(master, text="Search", width=15, height=2, bg='orange',command=self.search)
        self.btn_search.place(x=550,y=70)
        
        #label for the window
        self.name_l = Label(master, text="Enter Product Name", font=('arial 18 bold'))
        self.name_l.place(x=0,y=120)
        
        self.stock_l = Label(master, text="Enter Stocks", font=('arial 18 bold'))
        self.stock_l.place(x=0,y=170)
        
        self.cp_l = Label(master, text="Enter Cost Price", font=('arial 18 bold'))
        self.cp_l.place(x=0,y=220)
        
        self.sp_l = Label(master, text="Enter Selling Price", font=('arial 18 bold'))
        self.sp_l.place(x=0,y=270)
        
        self.vendor_l = Label(master, text="Enter Vendor Name", font=('arial 18 bold'))
        self.vendor_l.place(x=0,y=320)
        
        self.vendor_phone_l = Label(master, text="Enter Vendor Phone Number", font=('arial 18 bold'))
        self.vendor_phone_l.place(x=0,y=370)
        
        
        
        #entries for labels
        
        
        self.name_e  = Entry(master, width=25,font=('arial 18 bold'))
        self.name_e.place(x=380,y=120)
        
        self.stock_e  = Entry(master, width=25,font=('arial 18 bold'))
        self.stock_e.place(x=380,y=170)
        
        self.cp_e  = Entry(master, width=25,font=('arial 18 bold'))
        self.cp_e.place(x=380,y=220)

        self.sp_e  = Entry(master, width=25,font=('arial 18 bold'))
        self.sp_e.place(x=380,y=270)

        self.vendor_e  = Entry(master, width=25,font=('arial 18 bold'))
        self.vendor_e.place(x=380,y=320)
        
        self.vendor_phone_e = Entry(master, width=25,font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380,y=370)
        
        
        
        #buttons 
        self.btn_update = Button(master,text="Update Database", width = 25 ,height = 2,bg='steelblue', fg='white',command=self.update)
        self.btn_update.place(x=520,y=420)
        
        
        #text box for the logs
        
        self.tBox = Text(master, width=60 ,height=18)
        self.tBox.place(x=750,y=70)
        
        self.tBox.insert(END, "ID has reached upto "+ str(id))
    
    def search(self, *args, **kwargs):
        sql = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(), ))
        for r in result:
            self.n1 =r[1] #name
            self.n2 =r[2] #stock
            self.n3 =r[3] #cp
            self.n4 =r[4] #sp
            self.n5 =r[5] #totalcp
            self.n6 =r[6] #totalsp
            self.n7 =r[7] #assumed_profit
            self.n8 =r[8] #vendor
            self.n9 =r[9] #vendor_phoneno
        conn.commit()
        
        #insert the entities to update
        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.n1))
        
        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n2))
        
        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n3))
        
        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n4))
        
        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n8))
        
        self.vendor_phone_e.delete(0, END)
        self.vendor_phone_e.insert(0, str(self.n9))
        
    def update(self, *args,** kwargs):
        #get from entities
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.vendor_e.get()
        self.u6 = self.vendor_phone_e.get()
        
        #dynamic entries
        self.u7 = float(self.u3)*float(self.u2)
        self.u8 = float(self.u4)*float(self.u2)
        self.u9 = float(self.u8 - self.u7)
        
        sql="UPDATE inventory SET name=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, assumed_profit=?, vendor=?, vendor_phoneno=? WHERE id=?"
        c.execute(sql,(self.u1, self.u2, self.u3, self.u4, self.u7, self.u8, self.u9, self.u5, self.u6, self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Database Updated")
        
        
        
root=Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Update the database")
root.mainloop()