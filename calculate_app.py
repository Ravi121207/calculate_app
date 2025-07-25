from tkinter import*

root=Tk()
root.title("calulate")
root.geometry("470x500")

root.config(bg="green")

def press(key):
    entry.insert(END,key)
    
def clear():
    entry.delete(0,END)
    
def delete_one():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])
    
def calculate():
    try:
        result=eval(entry.get())
        entry.delete(0,END)
        entry.insert(END,str(result))
    except:
        entry.delete(0,END)
        entry.insert(END,"Error")
        
    
entry=Entry(root,width=23,font=("arial",21,"bold"),justify="right",relief=RIDGE)
entry.place(x=50,y=20)

frm2=Frame(root,width=370,height=320,background="gray")
frm2.place(x=50,y=100)

btn1=Button(frm2,text="7",font=("arial",20,"bold"),width=3,command=lambda:press("7"))
btn1.place(x=50,y=70)

btn2=Button(frm2,text="8",font=("arial",20,"bold"),width=3,command=lambda:press("8"))
btn2.place(x=120,y=70)

btn3=Button(frm2,text="9",font=("arial",20,"bold"),width=3,command=lambda:press("9"))
btn3.place(x=190,y=70)

btn4=Button(frm2,text="4",font=("arial",20,"bold"),width=3,command=lambda:press("4"))
btn4.place(x=50,y=130)

btn5=Button(frm2,text="5",font=("arial",20,"bold"),width=3,command=lambda:press("5"))
btn5.place(x=120,y=130)

btn6=Button(frm2,text="6",font=("arial",20,"bold"),width=3,command=lambda:press("6"))
btn6.place(x=190,y=130)

btn7=Button(frm2,text="1",font=("arial",20,"bold"),width=3,command=lambda:press("1"))
btn7.place(x=50,y=190)

btn8=Button(frm2,text="2",font=("arial",20,"bold"),width=3,command=lambda:press("2"))
btn8.place(x=120,y=190)

btn9=Button(frm2,text="3",font=("arial",20,"bold"),width=3,command=lambda:press("3"))
btn9.place(x=190,y=190)

btn10=Button(frm2,text="00",font=("arial",20,"bold"),width=3,command=lambda:press("00"))
btn10.place(x=50,y=250)

btn11=Button(frm2,text="0",font=("arial",20,"bold"),width=3,command=lambda:press("0"))
btn11.place(x=120,y=250)

btn12=Button(frm2,text=".",font=("arial",20,"bold"),width=3,command=lambda:press("."))
btn12.place(x=190,y=250)

btn13=Button(frm2,text="*",font=("arial",20,"bold"),width=3,command=lambda:press("*"))
btn13.place(x=260,y=70)

btn14=Button(frm2,text="-",font=("arial",20,"bold"),width=3,command=lambda:press("-"))
btn14.place(x=260,y=130)

btn15=Button(frm2,text="+",font=("arial",20,"bold"),width=3,command=lambda:press("+"))
btn15.place(x=260,y=190)

btn16=Button(frm2,text="=",font=("arial",20,"bold"),width=3,command=calculate)
btn16.place(x=260,y=250)

btn17=Button(frm2,text="AC",font=("arial",20,"bold"),width=3,command=clear)
btn17.place(x=50,y=10)

btn18=Button(frm2,text="%",font=("arial",20,"bold"),width=3,command=lambda:press("%"))
btn18.place(x=120,y=10)

btn19=Button(frm2,text="X",font=("arial",20,"bold"),width=3,command=delete_one)
btn19.place(x=190,y=10)

btn20=Button(frm2,text="/",font=("arial",20,"bold"),width=3,command=lambda:press("/"))
btn20.place(x=260,y=10)
root.mainloop()