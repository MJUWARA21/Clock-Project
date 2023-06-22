from tkinker import *
From tkinker.ttk import *

from time import strtime

root = Tk()
root.title("clock")
def time():
    string = strftime('%H:%M:%S %P')
    label.config(text=string)
    label.after(1000,time)

label = Label(root, front=("ds-digital",80) background = "cyan", foreground = "black")
label.pack(anchor= 'center')
time()
mainloop()
