from tkinter import *
from tkinter import messagebox

window = Tk() #window setup for Tk
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel()) #set the window in the center/front of the screen
window.withdraw() #hide it from site

#messagebox.showinfo('Question','Do you have red hair')
if messagebox.askyesno('Question','Do you have red hair',icon="error") == True:
    print("yes")
else:
    print("no")
window.deiconify()
window.destroy()
window.quit()