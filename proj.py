from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext
import cx_Oracle

root=Tk()
root.title("S. M. S.")  #S.M.S.--->student management system
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
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=''
		for d in data:
			msg=msg + "rno" + str(d[0]) + "name" + str(d[1]) + "marks" + str(d[2]) + "\n"
		stData.insert(INSERT,msg)
	

	except cx_Oracle.DatabaseError as e:
		print("select issue",e)
	
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()


btnAdd=Button(root, text="Add", font=("arial", 16, 'bold'),width=10, command=f1)
btnView=Button(root, text="View", font=("arial", 16, 'bold'),width=10, command=f3)
btnUpdate=Button(root, text="Update", font=("arial", 16, 'bold'),width=10)
btnDelete=Button(root, text="Delete", font=("arial", 16, 'bold'),width=10)
btnGraph=Button(root, text="Graph", font=("arial", 16, 'bold'),width=10)


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
		srno=int(entAddRno.get())
		name=entAddName.get()
		marks=int(entAddMarks.get())

		cursor=con.cursor()
		sql="insert into student values('%d', '%s', '%d')"
		args=(rno,name,marks)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount) + "rows inserted"
		messagebox.showinfo("Success",msg)

	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()


lblAddRno = Label(adSt, text="enter rno")
lblAddName = Label(adSt, text="enter name")
lblAddMarks = Label(adSt, text="enter marks")
entAddRno=Entry(adSt, bd=5)
entAddName=Entry(adSt, bd=5)
entAddMarks=Entry(adSt, bd=5)
btnAddSave=Button(adSt, text="Save", command=f5)
btnAddBack=Button(adSt, text="Back", command=f2)

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

viSt=Toplevel(root)   #Toplevel-->another GUI
viSt.title("View Student")
viSt.geometry("400x400+200+200")
viSt.withdraw()

stData=scrolledtext.ScrolledText(viSt, width=30, height=5)
btnViewBack=Button(viSt, text="Back", command=f4)

stData.pack(pady=10)
btnViewBack.pack(pady=10)


root.mainloop()