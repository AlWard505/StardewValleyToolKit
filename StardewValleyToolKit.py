from tkinter import *
from math import *

def crop():
    global seedamount
    
    cropwin = Toplevel(main)
    
    sprinksmall = Entry(cropwin, bd = 5)
    sprinksmall.focus_set()
    sprinksmall.grid(row = 2, column = 1)
    
    sprinkmedium = Entry(cropwin, bd = 5)
    sprinkmedium.focus_set()
    sprinkmedium.grid(row = 2, column = 2)
    
    sprinklarge = Entry(cropwin, bd = 5)
    sprinklarge.focus_set()
    sprinklarge.grid(row = 4, column = 1)
    
    sprinkbiggest = Entry(cropwin, bd = 5)
    sprinkbiggest.focus_set()
    sprinkbiggest.grid(row = 4, column = 2)
    
    slab = Label(cropwin, text ="sprinkler")
    slab.grid(row = 1, column = 1)
    
    mlab = Label(cropwin, text ="quality sprinkler")
    mlab.grid(row = 1, column = 2)
    
    llab = Label(cropwin, text ="iridium sprinkler")
    llab.grid(row = 3, column = 1)
    
    hlab = Label(cropwin, text = "iridium with booster")
    hlab.grid(row = 3, column = 2)
    
    seedamount = IntVar()
    
    calc = Button(cropwin, text= "Calculate", command =lambda: Calculate(sprinksmall.get(),sprinkmedium.get(),sprinklarge.get(),sprinkbiggest.get()))
    calc.grid(row = 2, column = 4)
    amountdisplay = Label(cropwin, textvariable = seedamount)
    amountdisplay.grid(row = 3, column = 4)
    frame = Frame(cropwin, width=15)
    frame.grid(row = 2, column=3)

def Calculate(x,c,y,z):
    global seedamount
    try:
        smallseeds = int(x) * 4
    except:
        smallseeds = 0

    try:
        mediumseeds = int(c) * 8
    except:
        mediumseeds = 0

    try:
        largeseeds = int(y) * 24
    except:
        largeseeds = 0

    try:
        hugeseeds = int(z) *48
    except:
        hugeseeds = 0
    
    seedamount.set(int(smallseeds) + int(mediumseeds) + int(largeseeds) + int(hugeseeds))

#this function allows the user to open a new tab#
#this tab will let them calculate how many geodes they can buy while still having enough remaining money to crack said geodes open
def geode():
    global totalgeode

    geodewin = Toplevel(main)
    label = Label(geodewin,text = "total money")
    label.grid(row = 1, column = 1)
    money = Entry(geodewin, bd = 5)
    money.focus_set()
    money.grid(row = 2, column = 1)
    label2 = Label(geodewin,text = "current geodes")
    label2.grid(row = 3, column = 1)
    currentgeodes = Entry(geodewin, bd = 5)
    currentgeodes.focus_set()
    currentgeodes.grid(row = 4, column = 1)
    calc = Button(geodewin, text= "Calculate", command =lambda: geodecalc(money.get(),currentgeodes.get()))
    calc.grid(row = 2, column = 3)
    totalgeode = IntVar()
    text = Label(geodewin, textvariable = totalgeode)
    text.grid(row = 3, column=3)
    frame = Frame(geodewin, width=15)
    frame.grid(row = 2, column=2)

# this function is used in the main geode funciton
# calculates how many geodes can be purchased by taking the input from the entry and dividing by 325 before rounding down
# its importtant that it rounds down and not just round in general so you dont end up with one geode you can crack open
def geodecalc(x,y):
    global totalgeode
    try:
        temp = int(x)-(25*int(y))
    except:
        try:
            temp = int(x)
        except:
            temp = 0
    try:
        
        total = int(temp)/325
        total = floor(total)
    except:
        total = 0
    totalgeode.set(total)

def replace():
    global totalrep
    rewindow = Toplevel(main)

    regla = Label(rewindow, text = "regular quality")
    regla.grid(row=1,column=1)
    reg = Entry(rewindow, bd = 5)
    reg.focus_set()
    reg.grid(row = 1, column = 2)

    silla = Label(rewindow, text = "silver quality")
    silla.grid(row=2,column=1)
    sil = Entry(rewindow, bd = 5)
    sil.focus_set()
    sil.grid(row = 2, column = 2)

    golla = Label(rewindow, text = "golden quality")
    golla.grid(row=3,column=1)
    gol = Entry(rewindow, bd = 5)
    gol.focus_set()
    gol.grid(row = 3, column = 2)

    irila = Label(rewindow, text = "iridium quality")
    irila.grid(row=4,column=1)
    iri = Entry(rewindow, bd = 5)
    iri.focus_set()
    iri.grid(row = 4, column = 2)


    
    totalrep = IntVar()
    text = Label(rewindow, textvariable = totalrep)
    text.grid(row = 2, column=4)
    addbut = Button(rewindow, text = "Calculate", command=lambda: repcalc(reg.get(),sil.get(),gol.get(),iri.get()))
    addbut.grid(row=3,column = 4)
    frame = Frame(rewindow, width=15)
    frame.grid(row = 2, column=3)

def repcalc(x,y,z,c):
    global totalrep

    try:
        xtemp = int(x)
    except:
        xtemp = 0

    try:
        ytemp = int(y)
    except:
        ytemp = 0

    try:
        ztemp = int(z)
    except:
        ztemp = 0

    try:
        ctemp = int(c)
    except:
        ctemp = 0 

    total = xtemp + ytemp + ztemp + ctemp
    totalrep.set(total)
    print(totalrep)


main = Tk()
label = Label(main, text = "Stardew Valley Tools")
label.pack(side = TOP)
sprinkbutton = Button(main,text = "crop space calculator", command = lambda:crop()) 
sprinkbutton.pack(side = TOP)
geodebutton = Button(main,text = "buying geodes from crobus", command = lambda:geode()) 
geodebutton.pack(side = TOP)
replacebutton = Button(main,text = "replacing grown crops", command = lambda:replace()) 
replacebutton.pack(side = TOP)

main.mainloop()
