import tkinter
import os
from tkinter import *
from tkinter import messagebox

wn = Tk()
wn.title('QR Code Scanner and generator')
wn.geometry('500x300')

def helloCallBack():
   os.system('python QrcodeGenerator.py')
def halloCallBack():
   os.system('python qrcodescanner.py')

headingFrame = Frame(wn,bg="azure",bd=1)
headingFrame.place(relx=0.10,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Welcome", bg='azure', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


button = Button(wn, text='Scan QR',font=('Courier',15,'normal'),command=halloCallBack)
button.place(x=90,y=100, relwidth=0.26, relheight=0.10)

button = Button(wn, text='Create QR',font=('Courier',15,'normal'),command=helloCallBack)
button.place(x=240,y=100, relwidth=0.26, relheight=0.10)

wn.mainloop()