from tkinter import *
import socket as s

def ipfinder():
    hostname = hostvar.get()
    hostvar.set(f'{hostname}')
    host = s.gethostbyname(hostname)
    ipvar.set(f'{host}')

root = Tk()
root.configure(background='bisque')
root.geometry('300x300')
root.title('IP finder')
Label(root, text='IP Finder', bg='red', font='arial 15 bold', padx='15',pady='5').pack(padx='10',pady='10')
host = Label(root, text='Host Name', padx='5',font='arial 10')
host.pack(padx='10',pady='10')
hostvar = StringVar()
hostvar.set(f'\t********')
hostentry = Entry(root, textvariable=hostvar, font='arial 10')
hostentry.pack()
ip = Label(root, text='IP Address',padx='5', font='arial 10')
ip.pack(padx='10',pady='10')
ipvar=StringVar()
ipvar.set(f'\t**********')
ipentry = Entry(root, textvariable=ipvar, font='arial 10')
ipentry.pack()
Button(root,text='Get my Ip',bg='gold', font='arial 10 bold', command=ipfinder).pack(padx='10',pady='10')
root.mainloop()
