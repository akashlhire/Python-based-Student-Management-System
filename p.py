from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cx_Oracle
import tkinter as tk
import os
import csv
import bs4
import requests
from PIL import Image, ImageTk
#import ttk

a1="https://www.brainyquote.com"
res=requests.get("https://www.brainyquote.com/quote_of_the_day")
soup=bs4.BeautifulSoup(res.text,'lxml')

quote=soup.find('img',{"class":"p-qotd"})
print(quote)


a2=quote['data-img-url']
img=a1+a2

r=requests.get(img)

with open("image.gif","wb")as f:
	f.write(r.content)



root = tk.Tk()
# show no frame
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))

# take a .jpg picture you like, add text with a program like PhotoFiltre
# (free from http://www.photofiltre.com) and save as a .gif image file
image_file = "image.gif"
#assert os.path.exists(image_file)
# use Tkinter's PhotoImage for .gif files
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="brown")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()

# show the splash screen for 3000 milliseconds then destroy
root.after(3000, root.destroy)
root.mainloop()

root=Tk()
root.title("S. M. S. ")
root.geometry("400x400+200+200")



def f1():
	adSt.deiconify()
	root.withdraw()
def f3():
	viSt.deiconify()
	root.withdraw()
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
			
			
		cursor=con.cursor()
		sql="select * from student1 "
			
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=''
		for d in data:
			msg = "rno  " + str(d[0]) + " name  "+ str(d[1])+" marks  " + str(d[2]) +"\n"
			stData.insert(INSERT,msg)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("insert issue ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f6():
	upSt.deiconify()
	root.withdraw()

def f8():
	deSt.deiconify()
	root.withdraw()


def f13():
	
	con=None
	cursor=None
	try:
		SQL="SELECT * FROM student1"
 
		# Network drive somewhere
		filename="Output.csv"
		FILE=open(filename,"w");
		output=csv.writer(FILE)
 
		con=cx_Oracle.connect("system/abc123")
			
			
		cursor=con.cursor()
		
			
		cursor.execute(SQL)
		for row in cursor:
			output.writerow(row)
		cursor.close()
		con.close()	
		FILE.close()
		
		x=[]
		y=[]
		df=pd.read_csv("Output.csv",header=None)
		
		x=df[0]
		y=df[2]
		plt.bar(x,y,width=2.0)




		
		plt.title('Performance')

		plt.xlabel('ROLL NO')
		plt.ylabel('MARKS')

		plt.show()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("Failure ",e)

		
	



btnAdd=Button(root,text="Add",font=("arial",16,'bold'),width=10,command=f1)
btnView=Button(root,text="View",font=("arial",16,'bold'),width=10,command=f3)
btnUpdate=Button(root,text="Update",font=("arial",16,'bold'),width=10,command=f6)
btnDelete=Button(root,text="Delete",font=("arial",16,'bold'),width=10,command=f8)
btnGraph=Button(root,text="Graph",font=("arial",16,'bold'),width=10,command=f13)

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)



adSt=Toplevel(root)
adSt.title("Add Student")
adSt.geometry("400x400+200+200")
adSt.withdraw()


def f2():
	root.deiconify()
	adSt.withdraw()

def f5():
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		srno=entAddRno.get()
		if srno.isdigit() and int(srno)>0:
			rno=int(srno)
		else:
			messagebox.showerror("Error", "Please enter a valid rollno(integer)")
			entAddRno.focus()
			return
                        
		ename=entAddName.get()
		if ename.isalpha():
			name=ename
		else:
			messagebox.showerror("Error", "Please enter a valid name(string)")
			entAddName.focus()
			return
		emarks=entAddMarks.get()
		if emarks.isdigit() and int(emarks)>=0 and int(emarks)<101:
			marks=int(emarks)
		else:
			messagebox.showerror("Error", "Enter marks within limit of 0 to 100")
			entAddMarks.focus()
			return
			
		cursor=con.cursor()
		sql="insert into student1 values('%d','%s','%d')"
		args=(rno,name,marks)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount) +"rows inserted "
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("Failure ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		
lblAddRno=Label(adSt,text="enter rno ")
lblAddName=Label(adSt,text="enter Name ")
lblAddMarks=Label(adSt,text="enter Marks ")
entAddRno=Entry(adSt,bd=5)
entAddName=Entry(adSt,bd=5)
entAddMarks=Entry(adSt,bd=5)
btnAddSave=Button(adSt,text="Save",command=f5)
btnAddBack=Button(adSt,text="Back",command=f2)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddMarks.pack(pady=10)
entAddMarks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)


def f4():
	root.deiconify()
	viSt.withdraw()

viSt=Toplevel(root)
viSt.title("View Student")
viSt.geometry("400x400+200+200")
viSt.withdraw()


stData=scrolledtext.ScrolledText(viSt,width=30,height=5)
btnViewBack=Button(viSt,text="Back",command=f4)

stData.pack(pady=10)
btnViewBack.pack(pady=10)



def f7():
	root.deiconify()
	upSt.withdraw()
def f10():
	con=None
	cursor=None
	try:
		
		con=cx_Oracle.connect("system/abc123")
		srno=entUpRno.get()
		if srno.isdigit() and int(srno)>0:
			rno=int(srno)
		else:
			messagebox.showerror("Error", "Please enter a valid rollno(integer)")
			entUpRno.focus()
			return
               
		ename=entUpName.get()
		if ename.isalpha():
			name=ename
		else:
			messagebox.showerror("Error", "Please enter a valid name(string)")
			entUpName.focus()
			return
		
			
		cursor=con.cursor()
		sql="update student1 set name = '%s' where rno = '%d'"
		
		args=(name,rno)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount) +"rows updated "
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("Failure ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f11():
	con=None
	cursor=None
	try:
		
		con=cx_Oracle.connect("system/abc123")
		srno=entUpRno.get()
		if srno.isdigit() and int(srno)>0:
			rno=int(srno)
		else:
			messagebox.showerror("Error", "Please enter a valid rollno(integer)")
			entUpRno.focus()
			return
		emarks=entUpMarks.get()
		
		if emarks.isdigit() and int(emarks)>=0 and int(emarks)<101:
			marks=int(emarks)
		else:
			messagebox.showerror("Error", "Please enter marks within limit of 0 to 100")
			entUpMarks.focus()
			return
		
			
		cursor=con.cursor()
		sql="update student1 set marks = '%d' where rno = '%d'"
		
		args=(marks,rno)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount) +"rows updated "
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("Failure ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
	

upSt=Toplevel(root)
upSt.title("Update Student")
upSt.geometry("400x400+200+200")
upSt.withdraw()

lblUpRno=Label(upSt,text="Enter rno ")
lblUpName=Label(upSt,text="Update Name ")
lblUpMarks=Label(upSt,text="Update Marks ")
entUpRno=Entry(upSt,bd=5)
entUpName=Entry(upSt,bd=5)
entUpMarks=Entry(upSt,bd=5)
btnUpName=Button(upSt,text="Update Name",command=f10)
btnUpMarks=Button(upSt,text="Update Marks",command=f11)

btnUpBack=Button(upSt,text="Back",command=f7)

lblUpRno.pack(pady=10)
entUpRno.pack(pady=10)
lblUpName.pack(pady=10)
entUpName.pack(pady=10)
lblUpMarks.pack(pady=10)
entUpMarks.pack(pady=10)
btnUpName.pack(pady=10)
btnUpMarks.pack(padx=10)
btnUpBack.pack(pady=10)

def f9():
	root.deiconify()
	deSt.withdraw()
def f12():
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		srno=entDeRno.get()
		if srno.isdigit() and int(srno)>0:
			rno=int(srno)
		else:
			messagebox.showerror("Error", "Please enter a valid rollno(integer)")
			entDeRno.focus()
			return
               
		
			
		cursor=con.cursor()
		sql="delete from student1 where rno ='%d'"
		args=(rno)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount) +"rows deleted "
		messagebox.showinfo("Success",msg)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		print("Failure ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()


deSt=Toplevel(root)
deSt.title("Delete Student")
deSt.geometry("400x400+200+200")
deSt.withdraw()

lblDeRno=Label(deSt,text="Enter rno ")
entDeRno=Entry(deSt,bd=5)
btnDeSave=Button(deSt,text="Delete",command=f12)
btnDeBack=Button(deSt,text="Back",command=f9)

lblDeRno.pack(pady=10)
entDeRno.pack(pady=10)
btnDeSave.pack(pady=10)
btnDeBack.pack(pady=10)





root.mainloop()
