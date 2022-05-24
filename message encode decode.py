from tkinter import *
import base64
from tkinter import messagebox

root = Tk()

root.geometry("1200x6000")

root.title("TechVidvan Message Encryption and Decryption")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

bot = Frame(root, width=800, relief=SUNKEN)
bot.pack(side=LEFT)

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="TechVidvan\nSECRET MESSAGING  ",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

lblMsg = Label(bot, font=('arial', 16, 'bold'),
               text="MESSAGE", bd=16, anchor="w")

lblMsg.grid(row=1, column=0)

txtMsg = Entry(bot, font=('arial', 16, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="powder blue", justify='right')

txtMsg.grid(row=1, column=1)

lblkey = Label(bot, font=('arial', 16, 'bold'),
               text="KEY (Only Integer)", bd=16, anchor="w")

lblkey.grid(row=2, column=0)

txtkey = Entry(bot, font=('arial', 16, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="powder blue", justify='right')

txtkey.grid(row=2, column=1)

lblmode = Label(bot, font=('arial', 16, 'bold'),
                text="MODE(e for encrypt, d for decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=3, column=0)

txtmode = Entry(bot, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="powder blue", justify='right')

txtmode.grid(row=3, column=1)

lblResult = Label(bot, font=('arial', 16, 'bold'),
                  text="The Result-", bd=16, anchor="w")

lblResult.grid(row=2, column=2)

txtResult = Entry(bot, font=('arial', 16, 'bold'),
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="powder blue", justify='right')

txtResult.grid(row=2, column=3)


def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()



def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)


def Results():
    msg = Msg.get()
    k = key.get()
    m = mode.get()
    m.lower()
    if (m == 'e'):
        Result.set(encode(k, msg))
    elif(m== 'd'):
        Result.set(decode(k, msg))
    else:
        messagebox.showinfo('TechVidvan', 'Wrong mode entered. Try again.')
        



def qExit():
    root.destroy()



def Reset():
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


btnTotal = Button(bot, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Show Message", bg="powder blue",
                  command=Results).grid(row=7, column=1)

btnReset = Button(bot, padx=16, pady=8, bd=16,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="green",
                  command=Reset).grid(row=7, column=2)

btnExit = Button(bot, padx=16, pady=8, bd=16,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Exit", bg="red",
                 command=qExit).grid(row=7, column=3)

root.mainloop()
