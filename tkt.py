import tkinter
win = tkinter.Tk()
win.title("Batch 2-pm") #to add title 
win.configure(bg='gray')  #background colour set to white
win.minsize(400,400)  #setting minimum size to the window
win.maxsize(600,600)   #setting maximum size to the window

def submit():
    # print(e1.get())
    # l3.config(text=e1.get())
    f=open('reg.txt','a')
    f.write(e1.get()+'\t')
    if var1.get()==1:
        print('male')
        f.write('male'+'\n')
    else:
        print('female')
        f.write('female'+'\n')
    

l1=tkinter.Label(win,text='Registration',bg='gray')
l1.place(x=175,y=15)
l2=tkinter.Label(win,text='Name',bg='gray')
l2.place(x=85,y=55)
e1=tkinter.Entry(win)
e1.place(x=145,y=55)
l4=tkinter.Label(win,text='gender',bg='gray',)
l4.place(x=65,y=95)
var1=tkinter.IntVar()

#radio button
r1=tkinter.Radiobutton(win,text='male',bg='gray',variable=var1,value=1)
r1.place(x=145,y=95)
r2=tkinter.Radiobutton(win,text='female',bg='gray',variable=var1,value=2)
r2.place(x=235,y=95)
#button
btn1=tkinter.Button(win,text='submit',bg='black',fg='white',activebackground='black',activeforeground='white',padx=20, pady=1,command=submit)
# btn1.pack()  # pack method to pack the button so it is visible
btn1.place(x=175,y=170)

# l3=tkinter.Label(win,bg='gray')
# l3.place(x=165,y=245)

win.mainloop()


