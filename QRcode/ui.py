# -*- coding:utf-8 -*-
import tkinter as tk
from PIL import Image,ImageTk
import time
import datetime
from qr import getimage

wj = r'C:\Users\dan\Desktop\code'
level = 'L'
root = tk.Tk()
res = tk.StringVar()
res.set(1)
text = tk.Text(root, width=30, height=20)
url = tk.Text(root,width=30, height=1,)
url2 = tk.Text(root, width=30, height=1, )

def main():
    root.minsize(800, 500)
    # root.maxsize(500, 300)
    root.title('QR code')
    edit(root)
    radio(root)
    # image(root)
    root.mainloop()

def edit(root):
    global url
    global url2
    label = tk.Label(root, text='输入URL')
    label.place(x=20,y=20)
    url = tk.Text(root,width=30, height=1,)
    url.place(x=20,y=50)
    labe2 = tk.Label(root, text='输入存放路径')
    labe2.place(x=20, y=80)
    url2 = tk.Text(root, width=30, height=1, )
    url2.place(x=20, y=110)


def func():
    global level
    level = res.get()
    print(res.get())

def go():
    global wj
    t = time.time()
    print('go')

    name = str(int(t))
    name += str(level)
    name += '.png'

    getimage(r'www.baidu.com',level,name,wj)


    wj += '\\'
    urlname = wj + name

    image(root,urlname)



def image(root,urlandname):
    img_open = Image.open(urlandname)
    # img_open.show()
    img_png = ImageTk.PhotoImage(img_open)

    label_img = tk.Label(root, image=img_png)
    label_img.config(image=img_png)
    label_img.image = img_png

    label_img.place(x=300,y=10)
    root.update_idletasks()


def radio(root):
    radio1 = tk.Radiobutton(
        root,
        text="L",
        value='L',
        variable=res,
        command=func
    )
    radio2 = tk.Radiobutton(
        root,
        text="M",
        value='M',
        variable=res,
        command=func
    )
    radio3 = tk.Radiobutton(
        root, text="Q",
        value='Q',
        variable=res,
        command=func
    )
    radio4 = tk.Radiobutton(
        root, text="H",
        value='H',
        variable=res,
        command=func
    )

    # 显示单选框
    radio1.place(x=20,y=135)
    radio2.place(x=70,y=135)
    radio3.place(x=120,y=135)
    radio4.place(x=170,y=135)

    button1 = tk.Button(root,
                             text="确定",
                             width=5,
                             height=1,
                             command=go
                             )
    button1.place(x=185,y=165)


main()


