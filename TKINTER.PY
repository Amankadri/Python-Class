import tkinter

sc = tkinter.Tk()
sc.title("MY APP")
sc.geometry("500x500")

lbl = tkinter.Label(sc,text="welcome to tkinter", font=('arial',12,'bold'))
lbl.place(x=10, y=20)

btn= tkinter.Button(sc,text="Click here",background="black",foreground="white")
btn.place(x=10,y=10)

sc.mainloop()