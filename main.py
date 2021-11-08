from tkinter import *
from tkinter.messagebox import *
import math as m
from typing import Sized
from audio_helper import PutarSuara
import threading
Welcome = Tk()

# Penggunaan Fungsi (Text,Voice assist)
font = ('serif', 20, 'bold')
ob = PutarSuara()


# Definisi beberapa fungsi
def hapusdikit():
    ex = SockText.get()
    ex = ex[0:len(ex) - 1]
    SockText.delete(0, END)
    SockText.insert(0, ex)


def hapussemua():
    SockText.delete(0, END)


def tekan_tombol(event):
    global p
    print("Tombol Tertekan")
    b = event.widget
    text = b['text']
    print(text)
    t = threading.Thread(target=ob.speak, args=(text,))
    t.start()

    if text == 'x':
        SockText.insert(END, "*")
        return

    if text == '=':
        try:
            ex = SockText.get()
            anser = eval(ex)
            SockText.delete(0, END)
            SockText.insert(0, anser)
        except Exception as e:
            print("Terjadi Kesalahan", e)
            showerror("Isi bidang dengan benar terlebih dahulu!", e)
        return

    SockText.insert(END, text)


# Buat tampilan Canvas1 (Welcome page) dan window (Kalkulator page)
window = Tk()
window.title('Ngr SockDash! - Kalkulator Sederhana')
window.geometry('400x380')
bg = PhotoImage(file = "img/SockBanner.png")
WelcomePage = Canvas( Welcome, width = 400,
                 height = 400)
WelcomePage.pack(fill = "both", expand = True)

WelcomePage.create_image( 0, 0, image = bg, 
                     anchor = "nw")

# Kotak display kalkulator
SockText = Entry(window, justify=RIGHT,background='black',fg='white',font =('arial', 20, 'bold'))
SockText.pack(side=TOP, pady=20, fill=X, padx=20)

# Parameter untuk frame tombol
SockFrame = Frame(window)
SockFrame.pack(side=TOP, padx=10)

# Pengaturan letak tombol
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(SockFrame, text=str(temp), font=font, width=5, relief='raised', activebackground='blue',
                     activeforeground='white', bg='black',fg='white')
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', tekan_tombol)

zeroBtn = Button(SockFrame, text='0', font=font, width=5, relief='raised', activebackground='blue',
                 activeforeground='white',bg='black',fg='white')
zeroBtn.grid(row=3, column=0)

dotBtn = Button(SockFrame, text='.', font=font, width=5, relief='ridge', activebackground='blue',
                activeforeground='white',bg='black',fg='white')
dotBtn.grid(row=3, column=1)

equalBtn = Button(SockFrame, text='=', font=font, width=5, relief='ridge', activebackground='blue',
                  activeforeground='white',bg='black',fg='white')
equalBtn.grid(row=3, column=2)

plusBtn = Button(SockFrame, text='+', font=font, width=5, relief='ridge', activebackground='blue',
                 activeforeground='white',bg='black',fg='white')
plusBtn.grid(row=0, column=3)

minusBtn = Button(SockFrame, text='-', font=font, width=5, relief='ridge', activebackground='blue',
                  activeforeground='white',bg='black',fg='white')
minusBtn.grid(row=1, column=3)

multBtn = Button(SockFrame, text='x', font=font, width=5, relief='ridge', activebackground='blue',
                 activeforeground='white',bg='black',fg='white')
multBtn.grid(row=2, column=3)

divideBtn = Button(SockFrame, text='/', font=font, width=5, relief='ridge', activebackground='blue',
                   activeforeground='white',bg='black',fg='white')
divideBtn.grid(row=3, column=3)

clearBtn = Button(SockFrame, text='←', font=font, width=11, relief='ridge', activebackground='blue',
                  activeforeground='white', command=hapusdikit,bg='black',fg='white')
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(SockFrame, text='AC', font=font, width=11, relief='ridge', activebackground='blue',
                     activeforeground='white',bg='black',fg='white', command=hapussemua)
allClearBtn.grid(row=4, column=2, columnspan=2)

# Mengaitken tombol ke button pada design
plusBtn.bind('<Button-1>', tekan_tombol)
minusBtn.bind('<Button-1>', tekan_tombol)
multBtn.bind('<Button-1>', tekan_tombol)
divideBtn.bind('<Button-1>', tekan_tombol)
zeroBtn.bind('<Button-1>', tekan_tombol)
dotBtn.bind('<Button-1>', tekan_tombol)
equalBtn.bind('<Button-1>', tekan_tombol)


def oke(event):
    print('hi')
    e = Event()
    e.widget = equalBtn
    tekan_tombol(e)


SockText.bind('<Return>', oke)

scFrame = Frame(window)


sinBtn = Button(scFrame, text='SIN', font=font, width=5, relief='ridge', activebackground='blue',
                activeforeground='orange')
sinBtn.grid(row=1, column=0)

cosBtn = Button(scFrame, text='COS', font=font, width=5, relief='ridge', activebackground='blue',
                activeforeground='orange')
cosBtn.grid(row=1, column=1)

tanBtn = Button(scFrame, text='TAN', font=font, width=5, relief='ridge', activebackground='blue',
                activeforeground='orange')
tanBtn.grid(row=1, column=2)

sqrtBtn = Button(scFrame, text='√', font=font, width=5, relief='ridge', activebackground='blue',
                 activeforeground='orange')
sqrtBtn.grid(row=1, column=3)

powBtn = Button(scFrame, text='^', font=font, width=5, relief='ridge', activebackground='blue',
                activeforeground='orange')
powBtn.grid(row=1, column=4)

normalcalc = True


def calculate_sc(event):
    print('btn..')
    btn = event.widget
    text = btn['text']
    print(text)
    ex = SockText.get()
    answer = ''
    if text == 'TAN':
        print("cal TAN")
        answer = m.tan(m.degrees(float(ex)))
    elif text == 'SIN':
        print("cal SIN")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'COS':
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'TAN':
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√':
        print('Akar')
        answer = m.sqrt(int(ex))
    elif text == '^':
        print('**')
        base, pow = ex.split('.')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))

    SockText.delete(0, END)
    SockText.insert(0, answer)


def sc_click():
    global normalcalc
    if normalcalc:
        SockFrame.pack_forget()
        # Tambah frame menu
        scFrame.pack(side=TOP, pady=20)
        SockFrame.pack(side=TOP)
        window.geometry('500x500')
        print("Tampilan Handal.")
        normalcalc = False
    else:
        print('Tampilan Standard.')
        scFrame.pack_forget()
        window.geometry('400x380')
        normalcalc = True


# Mengaitkan beberapa tombol tambahan di kalkulator handal
sqrtBtn.bind("<Button-1>", calculate_sc)
powBtn.bind("<Button-1>", calculate_sc)
sinBtn.bind("<Button-1>", calculate_sc)
cosBtn.bind("<Button-1>", calculate_sc)
tanBtn.bind("<Button-1>", calculate_sc)

fontMenu = ('', 15)
menubar = Menu(window, font=fontMenu)

mode = Menu(menubar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label="Kalkulator Handal", command=sc_click)

menubar.add_cascade(label="Fitur", menu=mode)

window.config(menu=menubar)

window.mainloop()
