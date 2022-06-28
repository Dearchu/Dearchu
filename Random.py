from tkinter import *
from PIL import Image, ImageTk
import random

menu1 = {1: ['ข้าวกะเพราหมูสับไข่ดาว', './randomfoods/p1.jpg'],
        2: ['ผัดไท', './randomfoods/p2.jpg'],
        3: ['ข้าวผัดกุ้ง', './randomfoods/p3.jpg'],
        4: ['ข้าวพะโล้หมู', './randomfoods/p4.jpg'],
        5: ['ผัดซีอิ๊วหมู', './randomfoods/p5.jpg'],
        6: ['คะน้าหมูกรอบราดข้าว', './randomfoods/p6.jpg'],
        7: ['ข้าวหมูทอดกระเทียมไข่ดาว', './randomfoods/p7.jpg'],
        8: ['แกงเขียวหวานไก่', './randomfoods/p8.jpg'],
        9: ['ลาบหมู', './randomfoods/p9.jpg'],
        10: ['ลูกชิ้นปิ้ง', './randomfoods/p10.jpg']}

menu2 = {1: ['บิงซูสตอร์เบอร์รี่', './randomfoods/s1.jpg'],
        2: ['คัพเค้ก', './randomfoods/s2.jpg'],
        3: ['ข้าวเหนียวมะม่วง', './randomfoods/s3.jpg'],
        4: ['บัวลอย', './randomfoods/s4.jpg'],
        5: ['ฮันนี่โทสต์', './randomfoods/s5.jpg'],
        6: ['เครปญี่ปุ่น', './randomfoods/s6.jpg'],
        7: ['บัวลอยเผือก', './randomfoods/s7.jpg'],
        8: ['สลัดผลไม้', './randomfoods/s8.jpg'],
        9: ['บวดฟักทอง', './randomfoods/s9.jpg'],
        10: ['ไอศครีม', './randomfoods/s10.jpg']}


# ---------------------------- หน้าที่ 4 ----------------------------
def result(frame):
    global m, n
    frame.destroy()
    frame = Frame(root, width=700, height=720, bg='#e6ccff')
    frame.pack(expand=True, fill='both')
    f1 = Frame(frame, bg='#e6ccff')
    f1.grid(row=0, column=0, padx=20, pady=25)
    Label(f1, text='อาหารวันนี้', width=18, height=2, fg='#cc0066', bg='#ff9999', font=('Sarabun', 16, 'bold')).pack(pady=10)
    img1 = ImageTk.PhotoImage((Image.open(menu1[n][1])).resize((300, 300), Image.ANTIALIAS))
    Label(f1, image=img1, bg='#cc9900').pack(pady=30)
    Label(f1, text=menu1[n][0], width=20, height=1, fg='#990099', bg='#e6ccff',
          font=('Sarabun', 14, 'bold')).pack(pady=10)

    f2 = Frame(frame, bg='#e6ccff')
    f2.grid(row=0, column=1, padx=20, pady=25)
    Label(f2, text='ขนมหวานวันนี้', width=18, height=2, fg='#cc0066', bg='#ff9999',
               font=('Sarabun', 16, 'bold')).pack(pady=10)
    img2 = ImageTk.PhotoImage((Image.open(menu2[m][1])).resize((300, 300), Image.ANTIALIAS))
    Label(f2, image=img2, bg='#cc9900').pack(pady=30)
    Label(f2, text=menu2[m][0], width=20, height=1, fg='#990099', bg='#e6ccff',
          font=('Sarabun', 14, 'bold')).pack(pady=10)

    f3 = Frame(frame, bg='#e6ccff')
    f3.grid(row=1, column=0, columnspan=2, pady=30)
    b1 = Button(f3, text='Restart', width=10, height=1, fg='#ffe6e6', bg='#990033',
                font=('Courier New', 16, 'bold'), command=lambda: start(frame))
    b1.pack(pady=25)
    frame.mainloop()

# ---------------------------- หน้าที่ 3 ----------------------------
state2 = 1
def randomsweet():
    global m, p, t, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, state2
    if state2 >= 5:
        state2 = 1
        frame.destroy()
    else:
        m = random.choice(range(1, 11))
        if m == 1:
            p.config(image=img1)
            t.config(text=menu2[1][0])
            state2 += 1
        elif m == 2:
            p.config(image=img2)
            t.config(text=menu2[2][0])
            state2 += 1
        elif m == 3:
            p.config(image=img3)
            t.config(text=menu2[3][0])
            state2 += 1
        elif m == 4:
            p.config(image=img4)
            t.config(text=menu2[4][0])
            state2 += 1
        elif m == 5:
            p.config(image=img5)
            t.config(text=menu2[5][0])
            state2 += 1
        elif m == 6:
            p.config(image=img6)
            t.config(text=menu2[6][0])
            state2 += 1
        elif m == 7:
            p.config(image=img7)
            t.config(text=menu2[7][0])
            state2 += 1
        elif m == 8:
            p.config(image=img8)
            t.config(text=menu2[8][0])
            state2 += 1
        elif m == 9:
            p.config(image=img9)
            t.config(text=menu2[9][0])
            state2 += 1
        elif m == 10:
            p.config(image=img10)
            t.config(text=menu2[10][0])
            state2 += 1
    frame.after(50, randomsweet)

def sweets(frame):
    global m, p, t, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10
    frame.destroy()
    frame = Frame(root, width=700, height=720, bg='#e68a00')
    frame.pack(expand=True, fill='both')

    Label(frame, text='เมนูขนมหวาน', width=35, height=2, fg='#ffcccc', bg='#660000', font=('Sarabun', 16, 'bold')).pack(pady=10)

    m = random.choice(range(1, 11))
    img1 = ImageTk.PhotoImage((Image.open(menu2[1][1])).resize((360, 360), Image.ANTIALIAS))
    img2 = ImageTk.PhotoImage((Image.open(menu2[2][1])).resize((360, 360), Image.ANTIALIAS))
    img3 = ImageTk.PhotoImage((Image.open(menu2[3][1])).resize((360, 360), Image.ANTIALIAS))
    img4 = ImageTk.PhotoImage((Image.open(menu2[4][1])).resize((360, 360), Image.ANTIALIAS))
    img5 = ImageTk.PhotoImage((Image.open(menu2[5][1])).resize((360, 360), Image.ANTIALIAS))
    img6 = ImageTk.PhotoImage((Image.open(menu2[6][1])).resize((360, 360), Image.ANTIALIAS))
    img7 = ImageTk.PhotoImage((Image.open(menu2[7][1])).resize((360, 360), Image.ANTIALIAS))
    img8 = ImageTk.PhotoImage((Image.open(menu2[8][1])).resize((360, 360), Image.ANTIALIAS))
    img9 = ImageTk.PhotoImage((Image.open(menu2[9][1])).resize((360, 360), Image.ANTIALIAS))
    img10 = ImageTk.PhotoImage((Image.open(menu2[10][1])).resize((360, 360), Image.ANTIALIAS))

    p = Label(frame, bg='#ffe066')
    p.pack(pady=10)

    t = Label(frame, text='', width=30, height=1, fg='#ffe066', bg='#e68a00', font=('Sarabun', 14, 'bold'))
    t.pack(pady=10)

    b1 = Button(frame, text='สุ่มใหม่', width=10, height=1, fg='#cccc00', bg='#003333', font=('Sarabun', 14, 'bold'), command=lambda: sweets(frame))
    b1.pack(pady=30)

    frame2 = Frame(frame, background='#e6ccff')
    frame2.pack(expand=True, fill='both')

    Button(frame2, text='Next ' + '\u276f\u276f\u276f', bd=0, fg='#4d2600', bg='#e6ccff', font=('Courier New', 14, 'bold'),
           command=lambda: result(frame)).pack(padx=10, pady=10, side=RIGHT)
    randomsweet()
    frame.mainloop()


# ---------------------------- หน้าที่ 2 ----------------------------
state1 = 1
def randomfood():
    global n, p, t, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, state1

    if state1 >= 5:
        state1 = 1
        frame.destroy()
    else:
        n = random.choice(range(1, 11))
        if n == 1:
            p.config(image=img1)
            t.config(text=menu1[1][0])
            state1 += 1
        elif n == 2:
            p.config(image=img2)
            t.config(text=menu1[2][0])
            state1 += 1
        elif n == 3:
            p.config(image=img3)
            t.config(text=menu1[3][0])
            state1 += 1
        elif n == 4:
            p.config(image=img4)
            t.config(text=menu1[4][0])
            state1 += 1
        elif n == 5:
            p.config(image=img5)
            t.config(text=menu1[5][0])
            state1 += 1
        elif n == 6:
            p.config(image=img6)
            t.config(text=menu1[6][0])
            state1 += 1
        elif n == 7:
            p.config(image=img7)
            t.config(text=menu1[7][0])
            state1 += 1
        elif n == 8:
            p.config(image=img8)
            t.config(text=menu1[8][0])
            state1 += 1
        elif n == 9:
            p.config(image=img9)
            t.config(text=menu1[9][0])
            state1 += 1
        elif n == 10:
            p.config(image=img10)
            t.config(text=menu1[10][0])
            state1 += 1
    frame.after(50, randomfood)

def foods(frame):
    global n, p, t, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10
    frame.destroy()
    frame = Frame(root, width=700, height=720, bg='#331a00')
    frame.pack(expand=True, fill='both')
    Label(frame, text='เมนูอาหาร', width=35, height=2, fg='#ffcce6', bg='#660033', font=('Sarabun', 16, 'bold')).pack(pady=10)
    n = random.choice(range(1, 11))
    img1 = ImageTk.PhotoImage((Image.open(menu1[1][1])).resize((360, 360), Image.ANTIALIAS))
    img2 = ImageTk.PhotoImage((Image.open(menu1[2][1])).resize((360, 360), Image.ANTIALIAS))
    img3 = ImageTk.PhotoImage((Image.open(menu1[3][1])).resize((360, 360), Image.ANTIALIAS))
    img4 = ImageTk.PhotoImage((Image.open(menu1[4][1])).resize((360, 360), Image.ANTIALIAS))
    img5 = ImageTk.PhotoImage((Image.open(menu1[5][1])).resize((360, 360), Image.ANTIALIAS))
    img6 = ImageTk.PhotoImage((Image.open(menu1[6][1])).resize((360, 360), Image.ANTIALIAS))
    img7 = ImageTk.PhotoImage((Image.open(menu1[7][1])).resize((360, 360), Image.ANTIALIAS))
    img8 = ImageTk.PhotoImage((Image.open(menu1[8][1])).resize((360, 360), Image.ANTIALIAS))
    img9 = ImageTk.PhotoImage((Image.open(menu1[9][1])).resize((360, 360), Image.ANTIALIAS))
    img10 = ImageTk.PhotoImage((Image.open(menu1[10][1])).resize((360, 360), Image.ANTIALIAS))

    p = Label(frame, bg='#b35900')
    p.pack(pady=10)

    t = Label(frame, text='', width=30, height=1, fg='#ffa64d', bg='#331a00', font=('Sarabun', 14, 'bold'))
    t.pack(pady=10)

    b1 = Button(frame, text='สุ่มใหม่', width=10, height=1, fg='#cccc00', bg='#003333', font=('Sarabun', 14, 'bold'), command=lambda: foods(frame))
    b1.pack(pady=30)

    frame2 = Frame(frame, background='#e6ccff')
    frame2.pack(expand=True, fill='both')

    Button(frame2, text='Next ' + '\u276f\u276f\u276f', bd=0, fg='#4d2600', bg='#e6ccff', font=('Courier New', 14, 'bold'),
           command=lambda: sweets(frame)).pack(padx=10, pady=10, side=RIGHT)
    randomfood()
    frame.mainloop()


# ---------------------------- หน้าที่ 1 ----------------------------
def start(frame):
    frame.destroy()
    frame = Frame(root, width=700, height=720)
    frame.pack()
    bg = Image.open("./randomfoods/bg.jpg")
    bg = bg.resize((700, 720), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)
    bg_lb = Label(frame, image=bg)
    bg_lb.place(x=0, y=0, relwidth=1, relheight=1)

    b1 = Button(frame, text='Random Foods & Sweets Menu', width=28, height=1, fg='white', bg='#003333',
                font=('Courier New', 24, 'bold'), command=lambda: foods(frame))
    b1.pack(pady=300)

    frame.pack_propagate(0)
    frame.mainloop()


root = Tk()
root.title('Foods & Sweets Generator')
root.resizable(0, 0)
root.geometry('700x720')
root.iconbitmap("./randomfoods/foodicon.ico")
frame = Frame(root)
frame.pack()
start(frame)

root.mainloop()
