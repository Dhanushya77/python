import tkinter
import mysql.connector
con = mysql.connector.connect(host='localhost',user='dhanushya', password='dhanushya@',database='reg')
con.autocommit=True
cur = con.cursor()
try:
    # cur.execute("create database reg")
    cur.execute("create table details(id int, name text, age text, gender text)")
except:
    pass

win = tkinter.Tk()
win.title("Registration Form")
win.configure(bg='gray')
win.minsize(400,400)
win.maxsize(700,700)

def submit():
        if var1.get()==1:
            gender="male" 
        else:
            gender="female"
        cur.execute("insert into details(id,name,age,gender)values(%s,%s,%s,%s)",(e1.get(),e2.get(),e3.get(),gender))
    
    
l1=tkinter.Label(win,text='id',bg='gray')
l1.place(x=85,y=25)
e1=tkinter.Entry(win)
e1.place(x=125,y=25)

l2=tkinter.Label(win,text='Name',bg='gray')
l2.place(x=65,y=70)
e2=tkinter.Entry(win)
e2.place(x=125,y=70)

l3=tkinter.Label(win,text='Age',bg='gray')
l3.place(x=75,y=115)
e3=tkinter.Entry(win)
e3.place(x=125,y=115)

l4=tkinter.Label(win,text='Gender',bg='gray')
l4.place(x=60,y=160)
var1=tkinter.IntVar()

r1=tkinter.Radiobutton(win,text='male',bg='gray',variable=var1,value=1)
r1.place(x=125,y=160)
r2=tkinter.Radiobutton(win,text='female',bg='gray',variable=var1,value=2)
r2.place(x=215,y=160)

btn1=tkinter.Button(win,text='submit',bg='black',fg='white',activebackground='black',activeforeground='white',padx=20, pady=1,command=submit)
btn1.place(x=160,y=215)


win.mainloop()