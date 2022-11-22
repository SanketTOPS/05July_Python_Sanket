import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox

window=tkinter.Tk()

window.geometry('500x600')
window.config(bg='lightblue')
window.title("FirstApp")

#tkinter.Label(text='Firstname:').pack()
#tkinter.Label(text='Lastname:').pack()

#tkinter.Label(text='Firstname:').place(x=0,y=0)
#tkinter.Label(text='Lastname:').place(x=0,y=30)

tkinter.Label(text='Firstname:',bg='lightblue',font='Cambria 15 bold',fg='red').grid(row=0,column=0,sticky='W')
tkinter.Label(text='Lastname:',bg='lightblue',font='Cambria 15 bold',fg='red').grid(row=1,column=0,sticky='W')

tkinter.Entry().grid(row=0,column=1,sticky='W')
tkinter.Entry().grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=0,text='Male',bg='lightblue',font='Cambria 15 bold',fg='red').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1,text='Female',bg='lightblue',font='Cambria 15 bold',fg='red').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text='Python',bg='lightblue',font='Cambria 15 bold',fg='red').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text='iOS',bg='lightblue',font='Cambria 15 bold',fg='red').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text='JAVA',bg='lightblue',font='Cambria 15 bold',fg='red').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text='PHP',bg='lightblue',font='Cambria 15 bold',fg='red').grid(row=6,column=0,sticky='W')


city=['Ahmedabad','Rajkot','Surat','Baroda','Navsari']
Combobox(values=city).grid(row=7,column=0,sticky='W')

def btnclick():
    #print("This is Button!")
    #messagebox.showerror('Error','Somthing went wrong...Try again!')
    #messagebox.showwarning('Warning','Your disk is full!')
    #messagebox.showinfo('Success','Your profile has been created!')

    #messagebox.askokcancel('Download','Do you want to continue?')
    #messagebox.askquestion('Download','Do you want to continue?')
    #messagebox.askretrycancel('Download','Do you want to continue?')
    #messagebox.askyesno('Download','Do you want to continue?')
    messagebox.askyesnocancel('Download','Do you want to continue?')

tkinter.Button(text='Submit',command=btnclick).place(x=220,y=300)
tkinter.mainloop()
