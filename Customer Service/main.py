from tkinter import *
from tkinter import font
from PIL import ImageTk,Image
import time
import random

#clock 
def clock():
    text=time.strftime("%H:%M:%S %p")
    timeg.config(text=text)
    date=time.strftime("%x\n %A")
    dateg.config(text=date)
    timeg.after(200,clock)

#function to clear entry feilds
def clearit():
    Donut1_e.delete(0, END)
    Donut2_e.delete(0, END)
    Donut3_e.delete(0, END)
    Bread1_e.delete(0, END)
    Bread2_e.delete(0, END)
    Bread3_e.delete(0, END)
    Cakes1_e.delete(0, END)
    Cakes2_e.delete(0, END)
    Cakes3_e.delete(0, END)
    Ccakes1_e.delete(0, END)
    Ccakes2_e.delete(0, END)
    Ccakes3_e.delete(0, END)
    Cof1_e.delete(0, END)
    Cof2_e.delete(0, END)
    Cof3_e.delete(0, END)
    Tp1_e.delete(0, END)
    Fr2_e.delete(0, END)
    Fb3_e.delete(0, END)
    Sub_total_e.delete(0, END)
    GSTcal_e.delete(0, END)
    Totalbill_e.delete(0, END)
    name_e.delete(0, END)
    Phone_e.delete(0, END)
    Billno_e.delete(0, END)
    zero()

#subtotal and bill no generator calls 
def putit():
    current1=int(Donut1_e.get())*4.95
    current2=int(Donut2_e.get())*4.85
    current3=int(Donut3_e.get())*4.85
    current4=int(Bread1_e.get())*5.58
    current5=int(Bread2_e.get())*5.39
    current6=int(Bread3_e.get())*5.49
    current7=int(Cakes1_e.get())*12.98
    current8=int(Cakes2_e.get())*12.39
    current9=int(Cakes3_e.get())*12.48
    current10=int(Ccakes1_e.get())*2.99
    current11=int(Ccakes2_e.get())*2.79
    current12=int(Ccakes3_e.get())*2.89
    current13=int(Cof1_e.get())*3.95
    current14=int(Cof2_e.get())*2.95
    current15=int(Cof3_e.get())*4.59
    current16=int(Tp1_e.get())*2.49
    current17=int(Fr2_e.get())*3.59
    current18=int(Fb3_e.get())*3.69


    subtot=current1+current2+current3+current4+current5+current6+current7+current8+current9+current10+current11+current12+current13+current14+current15+current16+current17+current18
    Sub_total_e.delete(0, END)
    Sub_total_e.insert(0, '$'+str(subtot)[:7])
    gst=int(subtot)*(4.45/100)
    GSTcal_e.delete(0, END)
    GSTcal_e.insert(0, '$'+str(gst)[:5])
    billtotal= float(subtot) + float(gst)
    Totalbill_e.delete(0, END)
    Totalbill_e.insert(0, '$'+str(billtotal)[:8])
    random.shuffle(my_list)
    g=out()
    Billno_e.delete(0, END)
    Billno_e.insert(0, str(g))
    Customername=name_e.get()
    CustomerPhone=Phone_e.get()
    


#function to input 0 as default value
def zero():
    Donut1_e.insert(0, "0")
    Donut2_e.insert(0, "0")
    Donut3_e.insert(0, "0")
    Bread1_e.insert(0, "0")
    Bread2_e.insert(0, "0")
    Bread3_e.insert(0, "0")
    Cakes1_e.insert(0, "0")
    Cakes2_e.insert(0, "0")
    Cakes3_e.insert(0, "0")
    Ccakes1_e.insert(0, "0")
    Ccakes2_e.insert(0, "0")
    Ccakes3_e.insert(0, "0")
    Cof1_e.insert(0, "0")
    Cof2_e.insert(0, "0")
    Cof3_e.insert(0, "0")
    Tp1_e.insert(0, "0")
    Fr2_e.insert(0, "0")
    Fb3_e.insert(0, "0")
    Sub_total_e.insert(0, "$"+"0")
    GSTcal_e.insert(0, "$"+"0")
    Totalbill_e.insert(0, "$"+"0")

def generatedbillno():
    date=time.strftime("%x")
    return date

my_list = list(range(1111,9999))                               
random.shuffle(my_list)
now=generatedbillno()

def out():

    a=now[:2] 
    b=now[3:5] 
    c=str(my_list[0])
    d=str(a)+str(b)+str(c)
    return d




root= Tk()

root = root
root.title("Billerr")
root.iconbitmap('icon.ico')

#image loading.
logo_img= ImageTk.PhotoImage(Image.open("Ldesign1.png"))
logo_imgl= Label(image=logo_img).grid(row=0,column=1,columnspan=9)

men_img= ImageTk.PhotoImage(Image.open("menu.png"))
men_imgl= Label(image=men_img).grid(row=7,column=4,columnspan=4,rowspan=10)

#time loading.
timeg= Label(root,font=("Century Gothic",30,'bold'),fg='#FF8300')
timeg.grid(row=0,column=0,columnspan=4)

dateg= Label(root,font=("Century Gothic",30,'bold'),fg='#FF8300')
dateg.grid(row=0,column=8,columnspan=3)
clock()

#labeling top.
cus_name=Label(root,text='Name:',font=("Lucida Handwriting",14),fg='#FB6090').grid(row=1,column=0)
name_e= Entry(root, width=32, font=("Lucida Handwriting",12))
name_e.grid(row=1,column=1,columnspan=3)

cus_Phone=Label(root,text=' Phone no: ',font=("Lucida Handwriting",14),fg='#E43D40').grid(row=1,column=4)
Phone_e= Entry(root, width=30,font=("Lucida Handwriting",12))
Phone_e.grid(row=1,column=5)

cus_Billno=Label(root,text=' Bill no: ',font=("Lucida Handwriting",14),fg='#821D30').grid(row=1,column=7)
Billno_e= Entry(root, width=34,font=("Lucida Handwriting",12))
Billno_e.grid(row=1,column=8,columnspan=2)

#labeling menu.
Space=Label(root, text='     ',font=("Verdana",12)).grid(row=2,column=0)

Heading1=Label(root, text=' DONUTS:',font=("Segoe Script",14),fg='#cd6917').grid(row=3,column=0)

Donut1=Label(root, text='Chocolate',font=("Mistral",18),fg='#6b482b').grid(row=4,column=0)
Donut1_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Donut1_e.grid(row=4,column=1)

Donut2=Label(root, text='Strawberry',font=("Mistral",18),fg='#DB1F48').grid(row=5,column=0)
Donut2_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Donut2_e.grid(row=5,column=1)

Donut3=Label(root, text='Vanilla',font=("Mistral",18),fg='#3CACAE').grid(row=6,column=0)
Donut3_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Donut3_e.grid(row=6,column=1)

Space=Label(root, text='     ',font=("Verdana",12)).grid(row=7,column=0)

Heading2=Label(root, text=' BREADS:',font=("Segoe Script",14),fg='#cd6917').grid(row=8,column=0)

Bread1=Label(root, text='Focaccia',font=("Mistral",18),fg='#6b482b').grid(row=9,column=0)
Bread1_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Bread1_e.grid(row=9,column=1)

Bread2=Label(root, text='Multi Grain',font=("Mistral",18),fg='#DB1F48').grid(row=10,column=0)
Bread2_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Bread2_e.grid(row=10,column=1)

Bread3=Label(root, text='Baguette',font=("Mistral",18),fg='#3CACAE').grid(row=11,column=0)
Bread3_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Bread3_e.grid(row=11,column=1)

Space=Label(root, text='     ',font=("Verdana",12)).grid(row=12,column=0)

Heading3=Label(root, text=' CAKES:',font=("Segoe Script",14),fg='#cd6917').grid(row=13,column=0)

Cakes1=Label(root, text='Apple Pie',font=("Mistral",18),fg='#6b482b').grid(row=14,column=0)
Cakes1_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Cakes1_e.grid(row=14,column=1)

Cakes2=Label(root, text='Cheese Cake',font=("Mistral",18),fg='#DB1F48').grid(row=15,column=0)
Cakes2_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Cakes2_e.grid(row=15,column=1)

Cakes3=Label(root, text='Tiramisu',font=("Mistral",18),fg='#3CACAE').grid(row=16,column=0)
Cakes3_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Cakes3_e.grid(row=16,column=1)

Space=Label(root, text='     ',font=("Verdana",12)).grid(row=18,column=0)

Heading4=Label(root, text=' CUPCAKES:',font=("Segoe Script",14),fg='#cd6917').grid(row=3,column=2)

Ccakes1=Label(root, text='Chocolate',font=("Mistral",18),fg='#6b482b').grid(row=4,column=2)
Ccakes1_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Ccakes1_e.grid(row=4,column=3)

Ccakes2=Label(root, text='Strawberry',font=("Mistral",18),fg='#DB1F48').grid(row=5,column=2)
Ccakes2_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Ccakes2_e.grid(row=5,column=3)

Ccakes3=Label(root, text='Vanilla',font=("Mistral",18),fg='#3CACAE').grid(row=6,column=2)
Ccakes3_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Ccakes3_e.grid(row=6,column=3)

Space=Label(root, text='     ',font=("Verdana",12)).grid(row=7,column=2)

Heading5=Label(root, text=' COFFEE:',font=("Segoe Script",14),fg='#cd6917').grid(row=8,column=2)

Cof1=Label(root, text='Americano',font=("Mistral",18),fg='#6b482b').grid(row=9,column=2)
Cof1_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Cof1_e.grid(row=9,column=3)

Cof2=Label(root, text='Expresso',font=("Mistral",18),fg='#DB1F48').grid(row=10,column=2)
Cof2_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Cof2_e.grid(row=10,column=3)

Cof3=Label(root, text='Cappuccino',font=("Mistral",18),fg='#3CACAE').grid(row=11,column=2)
Cof3_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Cof3_e.grid(row=11,column=3)

Space=Label(root, text='     ',font=("Verdana",12)).grid(row=12,column=2)

Heading6=Label(root, text=' ADDITIONALS:',font=("Segoe Script",14),fg='#cd6917').grid(row=13,column=2)

Tp1=Label(root, text='Toppings',font=("Mistral",18),fg='#6b482b').grid(row=14,column=2)
Tp1_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Tp1_e.grid(row=14,column=3)

Fr2=Label(root, text='Fro Shake',font=("Mistral",18),fg='#DB1F48').grid(row=15,column=2)
Fr2_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Fr2_e.grid(row=15,column=3)

Fb3=Label(root, text='Fro Bake',font=("Mistral",18),fg='#3CACAE').grid(row=16,column=2)
Fb3_e=Entry(root, width=2,font=("Lucida Handwriting",12))
Fb3_e.grid(row=16,column=3)

#labeling Totals.
Sp=Label(root, text=' ', font=("Verdana",18)).grid(row=3,column=10)
Sub_total=Label(root, text='Sub total:', font=("Lucida Handwriting",18),fg='#E9A200').grid(row=3,column=8,columnspan=2)
Sub_total_e=Entry(root, width=17,font=("Lucida Handwriting",25),fg='green')
Sub_total_e.grid(row=4,column=8,rowspan=2,columnspan=2)



GSTcal=Label(root, text='Taxes:', font=("Lucida Handwriting",18),fg='#B32800').grid(row=7,column=8,columnspan=2)
GSTcal_e=Entry(root, width=17,font=("Lucida Handwriting",25),fg='blue')
GSTcal_e.grid(row=8,column=8,rowspan=2,columnspan=2)


Totalbill=Label(root, text='Total:', font=("Lucida Handwriting",24),fg='#7F0000').grid(row=11,column=8,columnspan=2)
Totalbill_e=Entry(root, width=17,font=("Lucida Handwriting",25),fg='red')
Totalbill_e.grid(row=12,column=8,rowspan=2,columnspan=2)


#text below Menu image.
t1=Label(root, text='Levain Bakery!', font=("Lucida Calligraphy",20),fg='blue').grid(row=3,column=4,columnspan=4,rowspan=2)
t2=Label(root, text='340 LAFAYETTE ST. NYC 10012', font=("Lucida Calligraphy",16),fg='#FF8300').grid(row=5,column=4,columnspan=4,rowspan=2)
t2=Label(root, text='', font=("Verdana",20)).grid(row=18,column=4,columnspan=4)


#adding buttons
clear_img= ImageTk.PhotoImage(Image.open("clear1.jpg"))
clearimg = Button(root, image = clear_img,
             borderwidth = 0, command=clearit)
clearimg.grid(row=14,column=8)

total_img= ImageTk.PhotoImage(Image.open("total1.jpg"))
totalimg = Button(root, image = total_img,
             borderwidth = 0, command=putit)
totalimg.grid(row=14,column=9)





zero()



root.mainloop()

