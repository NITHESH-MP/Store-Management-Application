from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("D:\store management\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id=r[0]
class Database:
    def __init__(self, master,*args,**kwargs):
        self.master = master
        self.heading = Label(master,text="Add to the database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=400,y=0)
        
        
    #label for the window
        self.name_l = Label(master, text="Enter Product Name", font=('arial 18 bold'))
        self.name_l.place(x=0,y=70)
        
        self.stock_l = Label(master, text="Enter Stocks", font=('arial 18 bold'))
        self.stock_l.place(x=0,y=120)
        
        self.cp_l = Label(master, text="Enter Cost Price", font=('arial 18 bold'))
        self.cp_l.place(x=0,y=170)
        
        self.sp_l = Label(master, text="Enter Selling Price", font=('arial 18 bold'))
        self.sp_l.place(x=0,y=220)
        
        self.vendor_l = Label(master, text="Enter Vendor Name", font=('arial 18 bold'))
        self.vendor_l.place(x=0,y=270)
        
        self.vendor_phone_l = Label(master, text="Enter Vendor Phone Number", font=('arial 18 bold'))
        self.vendor_phone_l.place(x=0,y=320)
        
        self.id_l = Label(master, text="Enter ID", font=('arial 18 bold'))
        self.id_l.place(x=0,y=370)
        
        #entries for labels
        self.name_e  = Entry(master, width=25,font=('arial 18 bold'))
        self.name_e.place(x=380,y=70)
        
        self.stock_e  = Entry(master, width=25,font=('arial 18 bold'))
        self.stock_e.place(x=380,y=120)
        
        self.cp_e  = Entry(master, width=25,font=('arial 18 bold'))
        self.cp_e.place(x=380,y=170)

        self.sp_e  = Entry(master, width=25,font=('arial 18 bold'))
        self.sp_e.place(x=380,y=220)

        self.vendor_e  = Entry(master, width=25,font=('arial 18 bold'))
        self.vendor_e.place(x=380,y=270)
        
        self.vendor_phone_e = Entry(master, width=25,font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380,y=320)
        
        self.id_e = Entry(master,width=25, font=('arial 18 bold'))
        self.id_e.place(x=380,y=370)
        
        #buttons 
        self.btn_add = Button(master,text="Add to Database", width = 25 ,height = 2,bg='steelblue', fg='white' ,command=self.get_items)
        self.btn_add.place(x=520,y=420)
        
        self.btn_clear = Button(master,text="Clear all Fields", width = 18 ,height = 2,bg='lightgreen', fg='white', command=self.clear_all )
        self.btn_clear.place(x=350,y=420)
        
        #text box for the logs
        
        self.tBox = Text(master, width=60 ,height=18)
        self.tBox.place(x=750,y=70)
        
        self.tBox.insert(END, "ID has reached upto "+ str(id) )
        
        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Up>', self.clear_all)
        
    def get_items(self, *args,**kwargs):
        #get from entities
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()
        
        #dynamic entries
        self.totalcp = float(self.cp)*float(self.stock)
        self.totalsp = float(self.sp)*float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)

        if self.name =='' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("Error","Please fill all the entities.")
        else:
            sql="INSERt INTO inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno ) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone))
            conn.commit()
            #text box insert
            self.tBox.insert(END, "\n\nInserted "+ str(self.name) + " into the database with code " + str(self.id_e.get()))
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")
            
    def clear_all(self, *args, **kwargs):
        # Clear all entry fields
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)
        self.id_e.delete(0, END)
    
    

    

            
             

    
             
    
root=Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Add to database")
root.mainloop()