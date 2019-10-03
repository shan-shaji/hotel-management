from tkinter import*
from datetime import date
import random
import time

root = Tk()
root.geometry("1500x700+20+50")
root.title("Hotel Management System")
root.config(background='#23374d')

Tops = Frame(root, bg="white", width=1500, height=50, relief=SUNKEN)
Tops.pack(side=TOP)
Tops.config(background='#23374d')

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)
f1.config(background='#23374d')

# ------------------TIME--------------
localtime = time.asctime(time.localtime(time.time()))
# -----------------INFO TOP------------
lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Hotel Management System",
                fg="white", bd=0, anchor='w', background='#23374d')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 20, ), text=localtime,
                fg="white", bg="#23374d", anchor=W)
lblinfo.grid(row=1, column=0)


def Ref():
    # ---------------------------------------------------------------
    x = random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)
    cof = name.get()
    single_room = float(singleroom_o.get())
    double = float(Burger.get())
    cofi = float(Filet.get())
    cochee = float(Cheese_burger.get())
    codr = float(Drinks.get())
    check_in2 = str(check_in.get())
    check_out2 = str(check_out.get())

    # -----------date--------------------------------------------------
    check_in1 = check_in2.split("/")
    check_out1 = check_out2.split("/")
    f_date = date(int(check_in1[2]), int(check_in1[1]), int(check_in1[0]))
    l_date = date(int(check_out1[2]), int(check_out1[1]), int(check_out1[0]))
    delta = l_date - f_date
    number_d = delta.days

    if number_d == 0:
        singleroom = single_room*300
        doubleroom = double*500
        costoffilet = cofi*50
        costofcheeseburger = cochee*50
        costofdrinks = codr*35
    else:
        # ------------------------------------------------------------------
        singleroom = single_room*300*number_d
        doubleroom = double*500*number_d
        costoffilet = cofi*50
        costofcheeseburger = cochee*50
        costofdrinks = codr*35
    # ----------------------calculation---------------------------------
    costofmeal = "Rs.", str('%.2f' % (
        singleroom + doubleroom + costoffilet + costofcheeseburger + costofdrinks))
    PayTax = ((singleroom + doubleroom + costoffilet +
               costofcheeseburger + costofdrinks)*.18)
    Totalcost = (singleroom + doubleroom + costoffilet +
                 costofcheeseburger + costofdrinks)
    Ser_Charge = ((singleroom + doubleroom + costoffilet +
                   costofcheeseburger + costofdrinks)/100)
    Service = "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs.", str(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs.", str('%.2f' % PayTax)
    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()


def reset():
    rand.set("")
    name.set("")
    singleroom_o.set("0")
    Burger.set("0")
    Filet.set("0")
    Subtotal.set("0")
    Total.set("0")
    Service_Charge.set("0")
    Drinks.set("0")
    Tax.set("0")
    cost.set("0")
    Cheese_burger.set("0")
    check_in.set("")
    check_out.set("")


# ---------------------------------------------------------------------------------------
rand = StringVar()
name = StringVar()
singleroom_o = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()
check_in = StringVar()
check_out = StringVar()
# ----------------------------------------------------------------------------------------------------------
check_in4 = Label(f1, font=('aria', 16, 'bold'), text='Checkin',
                  fg='#eeeeee', bd=0, anchor='w', background='#23374d')
check_in4.grid(row=0, column=0)

checkdate = Entry(f1, font=('aria', '16', 'bold'), textvariable=check_in, bd=0, insertwidth=4,
                  bg="#1089ff", justify='right', highlightbackground="#23374d", highlightcolor="#23374d", fg="white")
checkdate.grid(row=0, column=1)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=1, column=0)

check_out4 = Label(f1, font=('aria', 16, 'bold'), text='Checkout',
                   fg='#eeeeee', bd=0, anchor='w', background='#23374d')
check_out4.grid(row=2, column=0)
checkoutdate = Entry(f1, font=('aria', '16', 'bold'), textvariable=check_out, bd=0, insertwidth=4,
                     bg="#1089ff", justify='right', highlightbackground="#23374d", highlightcolor="#23374d", fg="white")
checkoutdate.grid(row=2, column=1)
# ------------------------------------------------------------------------------------------------------------

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=3, column=0)


lblname = Label(f1, font=('aria', 16, 'bold'), text="Name",
                fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblname.grid(row=4, column=0)
txtname = Entry(f1, font=('ariel', 16, 'bold'), textvariable=name, bd=0, insertwidth=4, bg="#1089ff",
                justify='right', highlightbackground="#23374d", highlightcolor="#23374d", fg="white")
txtname.grid(row=4, column=1)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=5, column=0)

lblsingleroom_o = Label(f1, font=('aria', 16, 'bold'), text="Single Room",
                        fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblsingleroom_o.grid(row=6, column=0)
txtsingleroom_o = Entry(f1, font=('ariel', 16, 'bold'), textvariable=singleroom_o, bd=0, insertwidth=4,
                        bg="#1089ff", justify='right', highlightbackground="#23374d", highlightcolor="#23374d", fg="white")
txtsingleroom_o.grid(row=6, column=1)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=7, column=0)

lblburger = Label(f1, font=('aria', 16, 'bold'), text="Double Room",
                  fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblburger.grid(row=8, column=0)
txtburger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Burger, bd=0, insertwidth=4,
                  bg="#1089ff", justify='right', highlightbackground="#23374d", highlightcolor="#23374d", fg="white")
txtburger.grid(row=8, column=1)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=9, column=0)

lblFilet = Label(f1, font=('aria', 16, 'bold'), text="Pizza Meal",
                 fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblFilet.grid(row=10, column=0)
txtFilet = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Filet, bd=0, insertwidth=4, bg="#1089ff",
                 justify='right', highlightbackground="#23374d", highlightcolor="#23374d", fg="white")
txtFilet.grid(row=10, column=1)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=11, column=0)

lblCheese_burger = Label(f1, font=('aria', 16, 'bold'), text="    Cheese Burger   ",
                         fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblCheese_burger.grid(row=12, column=0)
txtCheese_burger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Cheese_burger, bd=0, insertwidth=4,
                         bg="#1089ff", justify='right', highlightbackground="#23374d", highlightcolor="#23374d", fg="white")
txtCheese_burger.grid(row=12, column=1)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=13, column=0)

lblDrinks = Label(f1, font=('aria', 16, 'bold'), text="Drinks",
                  fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblDrinks.grid(row=15, column=0)
txtDrinks = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Drinks, bd=0, insertwidth=4,
                  bg="#1089ff", justify='right', highlightbackground="#23374d", highlightcolor="#23374d", fg="white")
txtDrinks.grid(row=15, column=1)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=16, column=0)

# --------------------------------------------------------------------------------------
spacing = Label(f1, font=('aria', 16, 'bold'), text="                   ",
                fg="#eeeeee", bd=0, anchor='w', background='#23374d')
spacing.grid(row=0, column=2)

lblreference = Label(f1, font=('aria', 16, 'bold'), text="Order No.",
                     fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblreference.grid(row=0, column=3)
txtreference = Label(f1, font=('ariel', 16, 'bold'), textvariable=rand,
                     bd=0, bg="#23374d", justify='right', width=20)
txtreference.grid(row=0, column=4)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=1, column=2)
spacing = Label(f1, font=('aria', 16, 'bold'), text="                   ",
                fg="#eeeeee", bd=0, anchor='w', background='#23374d')
spacing.grid(row=1, column=2)

lblcost = Label(f1, font=('aria', 16, 'bold'), text="Cost",
                fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblcost.grid(row=2, column=3)
txtcost = Label(f1, font=('ariel', 16, 'bold'),
                textvariable=cost, bd=0, bg="#23374d", justify='right')
txtcost.grid(row=2, column=4)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=3, column=2)
spacing = Label(f1, font=('aria', 16, 'bold'), text="                   ",
                fg="#eeeeee", bd=0, anchor='w', background='#23374d')
spacing.grid(row=3, column=2)

lblService_Charge = Label(f1, font=('aria', 16, 'bold'), text="Service Charge",
                          fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblService_Charge.grid(row=4, column=3)
txtService_Charge = Label(f1, font=('ariel', 16, 'bold'),
                          textvariable=Service_Charge, bd=0, bg="#23374d", justify='right')
txtService_Charge.grid(row=4, column=4)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=5, column=2)
spacing = Label(f1, font=('aria', 16, 'bold'), text="                   ",
                fg="#eeeeee", bd=0, anchor='w', background='#23374d')
spacing.grid(row=5, column=2)

lblTax = Label(f1, font=('aria', 16, 'bold'), text="Tax",
               fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblTax.grid(row=6, column=3)
txtTax = Label(f1, font=('ariel', 16, 'bold'), textvariable=Tax,
               bd=0, bg="#23374d", justify='right')
txtTax.grid(row=6, column=4)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=7, column=2)
spacing = Label(f1, font=('aria', 16, 'bold'), text="                   ",
                fg="#eeeeee", bd=0, anchor='w', background='#23374d')
spacing.grid(row=7, column=2)

lblSubtotal = Label(f1, font=('aria', 16, 'bold'), text="Subtotal",
                    fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblSubtotal.grid(row=8, column=3)
txtSubtotal = Label(f1, font=('ariel', 16, 'bold'),
                    textvariable=Subtotal, bd=0, bg="#23374d", justify='right')
txtSubtotal.grid(row=8, column=4)

spacing = Label(f1, font=('aria', 16, 'bold'), fg="#eeeeee",
                bd=0, anchor='w', background='#23374d')
spacing.grid(row=9, column=2)
spacing = Label(f1, font=('aria', 16, 'bold'), text="                   ",
                fg="#eeeeee", bd=0, anchor='w', background='#23374d')
spacing.grid(row=9, column=2)

lblTotal = Label(f1, font=('aria', 16, 'bold'), text="Total",
                 fg="#eeeeee", bd=0, anchor='w', background='#23374d')
lblTotal.grid(row=10, column=3)
txtTotal = Label(f1, font=('ariel', 16, 'bold'),
                 textvariable=Total, bd=0, bg="#23374d", justify='right')
txtTotal.grid(row=10, column=4)

# -----------------------------------------buttons------------------------------------------by


btnTotal = Button(f1, padx=16, pady=8, bd=0, fg="white", font=('ariel', 16, 'bold'), width=10,
                  text="TOTAL", bg="#1089ff", command=Ref, highlightbackground="#23374d", highlightcolor="#23374d")
btnTotal.grid(row=2, column=6)

btnreset = Button(f1, padx=16, pady=8, bd=0, fg="white", font=('ariel', 16, 'bold'), width=10,
                  text="RESET", bg="#1089ff", command=reset, highlightbackground="#23374d", highlightcolor="#23374d")
btnreset.grid(row=4, column=6)

btnexit = Button(f1, padx=16, pady=8, bd=0, fg="white", font=('ariel', 16, 'bold'), width=10,
                 text="EXIT", bg="#1089ff", command=qexit, highlightbackground="#23374d", highlightcolor="#23374d")
btnexit.grid(row=6, column=6)

txtTotal = Label(f1, font=('ariel', 16, 'bold'),
                 text="             ", bd=0, bg="#23374d", justify='right')
txtTotal.grid(row=2, column=5)
txtTotal = Label(f1, font=('ariel', 16, 'bold'),
                 text="             ", bd=0, bg="#23374d", justify='right')
txtTotal.grid(row=4, column=5)
txtTotal = Label(f1, font=('ariel', 16, 'bold'),
                 text="             ", bd=0, bg="#23374d", justify='right')
txtTotal.grid(row=6, column=5)
txtTotal = Label(f1, font=('ariel', 16, 'bold'),
                 text="             ", bd=0, bg="#23374d", justify='right')
txtTotal.grid(row=8, column=5)
# -----------------------------function pop-up---------------------------------------------------------------


def price():
    roo = Tk()
    roo.geometry("390x100+700+400")
    roo.title("Price List")
    roo.config(background="#23374d")
    lblinfo = Label(roo, font=('aria', 15, 'bold'),
                    text="ROOM TYPE", fg="#eeeeee", bd=0, background="#23374d")
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="                ",
                    fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE",
                    fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo.grid(row=0, column=6)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="  SINGLE ROOM",
                    background="#23374d", fg="#eeeeee", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1000",
                    fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo.grid(row=1, column=6)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="  DOUBLE ROOM",
                    fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1500",
                    fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo.grid(row=2, column=6)
    roo.mainloop()


btnprice = Button(f1, padx=16, pady=8, bd=0, fg="white", font=('ariel', 16, 'bold'), width=10,
                  text="PRICE", bg="#1089ff", command=price, highlightbackground="#23374d", highlightcolor="#23374d")
btnprice.grid(row=8, column=6)


def price_1():
    root1 = Tk()
    root1.geometry("390x150+700+400")
    root1.title("Price List")
    root1.config(background="#23374d")
    lblinfo1 = Label(root1, font=('aria', 15, 'bold'),
                     text="MEALS TYPE", fg="#eeeeee", bd=0, background="#23374d")
    lblinfo1.grid(row=0, column=0)
    lblinfo1 = Label(root1, font=('aria', 15, 'bold'), text="                ",
                     fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo1.grid(row=0, column=3)
    lblinfo1 = Label(root1, font=('aria', 15, 'bold'), text="PRICE",
                     fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo1.grid(row=0, column=6)
    lblinfo1 = Label(root1, font=('aria', 15, 'bold'), text="  PIZZA MEAL",
                     background="#23374d", fg="#eeeeee", anchor=W)
    lblinfo1.grid(row=1, column=0)
    lblinfo1 = Label(root1, font=('aria', 15, 'bold'), text="50",
                     fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo1.grid(row=1, column=6)
    lblinfo1 = Label(root1, font=('aria', 15, 'bold'), text="  CHEESE BURGER",
                     fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo1.grid(row=2, column=0)
    lblinfo1 = Label(root1, font=('aria', 15, 'bold'), text="50",
                     fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo1.grid(row=2, column=6)
    lblinfo1 = Label(root1, font=('aria', 15, 'bold'), text="DRINKS",
                     fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo1.grid(row=3, column=0)
    lblinfo1 = Label(root1, font=('aria', 15, 'bold'), text="35",
                     fg="#eeeeee", background="#23374d", anchor=W)
    lblinfo1.grid(row=3, column=6)
    root1.mainloop()


btnprice2 = Button(f1, padx=16, pady=8, bd=0, fg="white", font=('ariel', 16, 'bold'), width=10,
                   text="MEALS", bg="#1089ff", command=price_1, highlightbackground="#23374d", highlightcolor="#23374d")
btnprice2.grid(row=10, column=6)


reset()
root.mainloop()
