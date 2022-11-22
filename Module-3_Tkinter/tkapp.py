import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox

screen=tkinter.Tk()
screen.title("FirstApp")
screen.geometry("400x500")
screen.config(background='gold')

#tkinter.Label(text='Firstname:').pack()
#tkinter.Label(text='Lastname:').pack()

#tkinter.Label(text='Firstname:',bg='gold',fg='red',font='Calibri 15 bold').place(x=0,y=0)
#tkinter.Label(text='Lastname:',bg='gold',fg='red',font='Calibri 15 bold').place(x=0,y=30)

tkinter.Label(text='Firstname:',bg='gold',fg='red',font='Calibri 15 bold').grid(row=0,column=0,sticky='W')
tkinter.Label(text='Lastname:',bg='gold',fg='red',font='Calibri 15 bold').grid(row=1,column=0,sticky='W')
tkinter.Entry().grid(row=0,column=1,sticky='W')
tkinter.Entry().grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=0,text='Male',bg='gold',fg='red',font='Calibri 15 bold').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1,text='Female',bg='gold',fg='red',font='Calibri 15 bold').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text='iOS',bg='gold',fg='red',font='Calibri 15 bold').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text='Python',bg='gold',fg='red',font='Calibri 15 bold').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text='JAVA',bg='gold',fg='red',font='Calibri 15 bold').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text='React',bg='gold',fg='red',font='Calibri 15 bold').grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Rajkot','Baroda','Surat','Jamnagar','Navsari']
Combobox(values=city).grid(row=7,column=0)

def btnclick():
    #print("This is button click!")
    #messagebox.showerror("Error","Somthing went wrong...try again!")
    #messagebox.showinfo("Success","Your account has been created!")
    #messagebox.showwarning("Warning","Your disk is full!")

    #messagebox.askokcancel("Downlaod","Do you want to continue?")
    #messagebox.askquestion("Downlaod","Do you want to continue?")
    #messagebox.askretrycancel("Downlaod","Do you want to continue?")
    #messagebox.askyesno("Downlaod","Do you want to continue?")
    messagebox.askyesnocancel("Downlaod","Do you want to continue?")

tkinter.Button(text='Submit',font='Calibri 15 bold',command=btnclick).place(x=170,y=270)
screen.mainloop()


