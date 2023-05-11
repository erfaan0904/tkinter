import tkinter as tk
from tkinter import messagebox
dtp = tk.Tk()
dtp.geometry("800x300")
dtp.title("Lesson percentage calculator") # Adding a title
def show_info():
    messagebox.showinfo("Show info", "showing informations")
def COLP():  #Calculation Of Lesson Percentage
    global rq, wq, tq
    rq = rq.get("1.0",'end-1c')
    wq = wq.get("1.0",'end-1c')
    tq = tq.get("1.0",'end-1c')
    rq, wq, tq = int(rq), int(wq), int(tq)
    lq = (((rq * 3) - wq) / (tq * 3)) * 100
    tk.messagebox.showinfo(title = "lesson percentage", message = "Your lesson percentage calculator : {} : درصد درس شما".format(lq))
l1 = tk.Label(dtp, text = 'Enter the number of correct selected questions : ', font = 20)
l1.grid(row = 0, column = 0,  padx = 1, pady = 20)
l2 = tk.Label(dtp, text = 'Enter the number of wrongly selected questions : ', font = 20)
l2.grid(row = 1, column = 0,  padx = 1, pady = 20)
l3 = tk.Label(dtp, text = 'Enter the number of total course questions : ',     font = 20)
l3.grid(row = 2, column = 0,  padx = 1, pady = 20)
l4 = tk.Label(dtp, text = ': تعداد سؤالات انتخاب شده صحیح را وارد کنید',     font = 20)
l4.grid(row = 0, column = 10, padx = 1, pady = 20)
l5 = tk.Label(dtp, text = ': تعداد سؤالات انتخاب شده اشتباه را وارد کنید',   font = 20)
l5.grid(row = 1, column = 10, padx = 1, pady = 20)
l6 = tk.Label(dtp, text = ': تعداد کل سوالات را وارد کنید',                   font = 20)
l6.grid(row = 2, column = 10, padx = 1, pady = 20)

rq = tk.Text(dtp, font = 20,  height = 1, width = 5, bg = 'white')
rq.grid(row = 0,  column = 1, columnspan = 4)
wq = tk.Text(dtp, font = 20,  height = 1, width = 5, bg = 'white')
wq.grid(row = 1,  column = 1, columnspan = 4)
tq = tk.Text(dtp, font = 20,  height = 1, width = 5, bg = 'white')
tq.grid(row = 2,  column = 1, columnspan = 4)
b1 = tk.Button(dtp,text='calculate | محاسبه', command = lambda:COLP(), font = 20, bg = 'white')
b1.grid(row = 3,  column = 1, padx = 20,  pady = 20)

dtp.mainloop()