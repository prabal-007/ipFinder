from tkinter import *
import socket

def ipfinder():
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    print(f"Host name = {hostname}")
    print(f'IP address = {host}')

root = Tk()
root.configure(background='bisque')
root.geometry('400x400')
root.title('IP finder')
Label(root, text='IP Finder', bg='red', font='arial 15 bold', padx='15',pady='5').pack(padx='10',pady='10')
host = Label(root, text='Host Name',font='arial 10')
host.pack(padx='10',pady='10')
hostentry = Entry(root, font='arial 10')
hostentry.pack()
ip = Label(root, text='IP Address',font='arial 10')
ip.pack(padx='10',pady='10')
ipentry = Entry(root, font='arial 10')
ipentry.pack()
Button(root,text='Get Ip',font='arial 10 bold', command=ipfinder).pack(padx='10',pady='10')
root.mainloop()
