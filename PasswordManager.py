import tkinter as tk
import random
import string
my_w = tk.Tk()
my_w.geometry("510x80") 
my_w.title("Password Ganator") # Adding a title
global data 

l1 = tk.Label(my_w, text='Password',font=20) # added one Label 
l1.grid(row=0,column = 0,padx = 1,pady =20) 
e1 = tk.Text(my_w,font = 20,height = 1, width=30, bg='white') # text box
e1.grid(row = 0,column = 1,columnspan = 4) 

def PG(): #Password Generator
  e1.delete("1.0","end")
  length   = 24
  lower    = string.ascii_lowercase
  upper    = string.ascii_uppercase
  num      = string.digits
  symbols  = string.punctuation
  all      = lower + upper + num + symbols
  temp     = random.sample(all,length)
  password = "".join(temp)
  # password generatoe source (line 16 to line 23): 
  # https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9
  e1.insert(tk.END,password)
b1 = tk.Button(my_w,text='create password', command = lambda:PG(), font = 20, bg = 'white')
b1.grid(row = 0, column = 15, padx = 20, pady = 20)
my_w.mainloop()