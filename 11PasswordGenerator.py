from tkinter import *
from tkinter.ttk import *#SOS to bazo gia na use combobox
from ttkthemes import ThemedTk
import requests, json
import pyperclip
import random

screen = ThemedTk(theme="smog") #creates window
screen.configure(themebg="smog")

screen.title("Password Generator") # Title
screen.geometry('452x120') #window dimensions - megethos
screen.resizable(height=False, width=False)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$&"

letnum = letters + numbers

lenusy = letters + numbers +symbols

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$&"

def copy():
    copied = passwordentry.get()
    pyperclip.copy(copied)

  # Generate password based on the selected complexity
def generate():
    pick = chce.get()
    print(chce)
    passwordentry.delete(0, END)
    length = int(tms.get())
    password = ''
    if pick == 1:
        print("low")
        for i in range(length):
            a = random.choice(letters)
            password += a
    elif pick == 2:
        print("mid")
        for f in range(length):
            a = random.choice(letnum)
            password += a
    elif pick == 3:
        print("high")
        for h in range(length):
            a = random.choice(lenusy)
            password += a
    else:
        print("WRONG VALUE")
    passwordentry.insert(END,password)

# Function to encrypt the password using a Caesar cipher with a fixed key
def encrypt():
    passf = passwordentry.get()
    encryptentry.delete(0,END)
    key = 69
    passenc = ''
    for m in passf:
        if m in characters:
            pos = characters.index(m)
            newpos = (pos + key) % len(characters)
            passenc += characters[newpos]
        else:
            passenc +=m

    encryptentry.insert(END,passenc)

    print("encrypt")


def decrypt(): # Function to decrypt the password using the same Caesar cipher key
    passf = encryptentry.get()
    decryptentry.delete(0, END)
    key = 69
    passenc = ''
    for m in passf:
        if m in characters:
            pos = characters.index(m)
            newpos = (pos - key) % len(characters)
            passenc += characters[newpos]
        else:
            passenc += m

    decryptentry.insert(END,passenc)

    print("decrypt")

#GUI
passwordlbl = Label(screen,text = "Password")
passwordentry = Entry(screen)
copybtn = Button(screen,text="Copy",command=copy)
generatebtn = Button(screen,text="Generate",command=generate)
lengthlbl = Label(screen,text = "Length")
lengthentry = Entry(screen)
encryptlbl = Label(screen,text = "Encrypted Password")
encryptentry = Entry(screen)
decryptlbl = Label(screen,text = "Decrypted Password")
decryptentry = Entry(screen)
encryptbtn = Button(screen,text="Encrypt",command=encrypt)
decryptbtn = Button(screen,text="Decrypt",command=decrypt)

tms = Combobox(screen,state='readonly')
tms['values']=('8','9','10','11','12','13','14','15','16','18','20','32','69')#tuple
tms.current(1)
chce = IntVar()#variable with integers

rblow = Radiobutton(screen,text="Low",value=1,variable=chce)
rbmid = Radiobutton(screen,text="Medium",value=2,variable=chce)
rbhigh = Radiobutton(screen,text="High",value=3, variable =chce)


#Grid
passwordlbl.grid(row=0, column=0)
passwordentry.grid(row=0, column=1)
copybtn.grid(row=0, column=2)
generatebtn.grid(row=0, column=3)
lengthlbl.grid(row=1, column=0)
tms.grid(row=1, column=1)
rblow.grid(row=1, column=2)
rbmid.grid(row=1, column=3)
rbhigh.grid(row=1, column=4)
encryptlbl.grid(row=2, column=0)
encryptentry.grid(row=2, column=1)
decryptlbl.grid(row=3, column=0)
decryptentry.grid(row=3, column=1)
encryptbtn.grid(row=2, column=2)
decryptbtn.grid(row=3, column=2)

screen.mainloop() #teleftaia entolh klenei programma
