from tkinter import *

window = Tk()

window.geometry("400x400")
window.configure(bg="blue")

appLabel = Label(window,text="Simple Interest Calculator",bg="black",fg="white",font=("Calibri", 20),bd=5)
appLabel.place(x=50,y=20)

principalLabel = Label(window,text="Principal(in rupees) : ",bg="black",fg="white",font=("Calibri", 12),bd=1)
principalLabel.place(x=20,y=90)
principal = Entry(window , text = "" , bd=2, width = 22)
principal.place(x=120,y=90)

rateLabel = Label(window,text="Rate(only number) : ",bg="black",fg="white",font=("Calibri", 12),bd=1)
rateLabel.place(x=20,y=180)
rate = Entry(window , text = "" , bd=2, width = 22)
rate.place(x=160,y=180)

timeLabel = Label(window,text="Time(in years) : ",bg="black",fg="white",font=("Calibri", 12),bd=1)
timeLabel.place(x=20,y=180)
time = Entry(window , text = "" , bd=2, width = 22)
time.place(x=160,y=180)

def calculateSI():
    SI = principal*rate*time/100
    SI = round(SI,1)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()


















