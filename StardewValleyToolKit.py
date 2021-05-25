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
    calc.grid(row = 2, column = 3)
    amountdisplay = Label(cropwin, textvariable = seedamount)
    amountdisplay.grid(row = 3, column = 3)

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

def geode():
    global totalgeode

    geodewin = Toplevel(main)
    label = Label(geodewin,text = "total money")
    label.grid(row = 1, column = 1)
    money = Entry(geodewin, bd = 5)
    money.focus_set()
    money.grid(row = 2, column = 1)
    calc = Button(geodewin, text= "Calculate", command =lambda: geodecalc(money.get()))
    calc.grid(row = 1, column = 2)
    totalgeode = IntVar()
    text = Label(geodewin, textvariable = totalgeode)
    text.grid(row = 2, column=2)

def geodecalc(x):
    global totalgeode
    total = int(x)/325
    total = floor(total)
    totalgeode.set(total)
    

main = Tk()
label = Label(main, text = "Stardew Valley Tools")
label.pack(side = TOP)
sprinkbutton = Button(main,text = "crop space calculator", command = lambda:crop()) 
sprinkbutton.pack(side = TOP)
geodebutton = Button(main,text = "buying geodes from crobus", command = lambda:geode()) 
geodebutton.pack(side = TOP)

main.mainloop()
