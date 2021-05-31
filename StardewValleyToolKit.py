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
    calc.grid(row = 3, column = 4)
    amountdisplay = Label(cropwin, textvariable = seedamount)
    amountdisplay.grid(row = 2, column = 4)
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
    calc.grid(row = 3, column = 3)
    totalgeode = IntVar()
    text = Label(geodewin, textvariable = totalgeode)
    text.grid(row = 2, column=3)
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

# used to check how many seeds you need to buy after a harvest
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

# calculates the amount from the 4 given entrys
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

def villagers():
    global vildict,infoframe
    vildict = {
        "allvil":[
            "alex","elliot","harvey","sam","sebastian","shane","abigail","emily","haley","leah","maru","penny"
        ],
        "choices":[
            "Birthday", "Favourite Gifts"
        ],
        "alex":{
            "Birthday":"summer 13",
            "Favourite Gifts":["Complete Breakfast", "Salmon Dinner", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard", "Rabbit's Foot"]
        },
        "elliot":{
            "Birthday":"fall 5",
            "Favourite Gifts":["Crab Cakes", "Duck Feather", "Lobster", "Pomegranate", "Squid Ink", "Tom Kha Soup", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard", "Rabbit's Foot"]
        },
        "harvey":{
            "Birthday":"winter 14",
            "Favourite Gifts":["Coffee", "Pickles", "Super Meal", "Truffle Oil", "Wine", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard", "Rabbit's Foot"]
        },
        "sam":{
            "Birthday":"summer 17",
            "Favourite Gifts":["actus Fruit", "Maple Bar", "Pizza", "Tigerseye", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard", "Rabbit's Foot"]
        },
        "sebastian":{
            "Birthday":"winter 10",
            "Favourite Gifts":["Frozen Tear", "Obsidian", "Pumpkin Soup", "Sashimi", "Void Egg", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard", "Rabbit's Foot"]
        },
        "shane":{
            "Birthday":"spring 20",
            "Favourite Gifts":["Beer", "Hot Pepper", "Pepper Poppers", "Pizza", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard", "Rabbit's Foot"]
        },
        "abigail":{
            "Birthday":"fall 13",
            "Favourite Gifts":["Amethyst", "Banana Pudding", "Blackberry Cobbler", "Chocolate Cake", "Pufferfish", "Pumpkin", "Spicy Eel", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard", "Rabbit's Foot"]
        },
        "emily":{
            "Birthday":"spring 27",
            "Favourite Gifts":["Amethyst", "Aquamarine", "Cloth", "Emerald", "Jade", "Ruby", "Survival Burger", "Topaz", "Wool", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard", "Rabbit's Foot"]
        },
        "haley":{
            "Birthday":"spring 14",
            "Favourite Gifts":["Coconut", "Fruit Salad", "Pink Cake", "Sunflower", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Rabbit's Foot"]
        },
        "leah":{
            "Birthday":"winter 23",
            "Favourite Gifts":["Goat Cheese", "Poppyseed Muffin", "Salad", "Stir Fry", "Truffle", "Vegetable Medley", "Wine", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard", "Rabbit's Foot"]
        },
        "maru":{
            "Birthday":"summer 10",
            "Favourite Gifts":["Battery Pack", "Cauliflower", "Cheese Cauliflower", "Diamond", "Gold Bar", "Iridium Bar", "Miner's Treat", "Pepper Poppers", "Radioactive Bar", "Rhubarb Pie", "Strawberry", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard", "Rabbit's Foot"]
        },
        "penny":{
            "Birthday":"fall 2",
            "Favourite Gifts":["Diamond", "Emerald", "Melon", "Poppy", "Poppyseed Muffin", "Red Plate", "Roots Platter", "Sandfish", "Tom Kha Soup", "Golden Pumpkin", "Magic Rock Candy", "Pearl", "Prismatic Shard"]
        },
    }
    vilwindow = Toplevel(main)
    
    scrollboxframe = Frame(vilwindow,bd = 5)
    scrollboxframe.grid(row=1,column=1,sticky=N+S)

    scrollboxframe2 = Frame(scrollboxframe)
    scrollboxframe2.pack()

    secondoption = Frame(vilwindow, bd = 5)
    secondoption.grid(row=1, column= 2)

    infoframe = Frame(vilwindow,width = 200,bd=5)
    infoframe.grid(row=1,column=3,sticky=N+S)

    Villselect = Listbox(scrollboxframe2,height=10,selectmode = SINGLE)
    scroll = Scrollbar(scrollboxframe2)
    scroll.pack(side=RIGHT,fill = BOTH)

    x=0
    while x != len(vildict["allvil"]):
        Villselect.insert(x,vildict["allvil"][x])
        Villselect.pack()
        x+=1
    Villselect.config(yscrollcommand = scroll.set)
    scroll.config(command = Villselect.yview)

    Birth = BooleanVar()
    fav = BooleanVar()

    birthcheck  = Checkbutton(secondoption,text="Birthday", variable=Birth, onvalue=True, offvalue=False)
    birthcheck.pack(anchor=NW)

    favcheck = Checkbutton(secondoption,text="Favourite", variable=fav, onvalue=True, offvalue=False)
    favcheck.pack(anchor=NW)

    infobutt = Button(scrollboxframe,text ="get info",command=lambda:vilinfo(Villselect,Birth,fav))
    infobutt.pack()

def vilinfo(vil,C1,C2):
    for child in infoframe.winfo_children():
        child.destroy()
    entry = vil.curselection()
    entry = str(entry)
    entry = entry.translate({ord(","): None})
    entry = entry.translate({ord("("): None})
    entry = entry.translate({ord(")"): None})
    selectedvillager = vildict["allvil"][int(entry)]
    if C1.get() == True:
        birthdayframe = Frame(infoframe)
        birthdayframe.pack(side = LEFT)
        Birthday = Label(birthdayframe,text="Birthday: "+vildict[selectedvillager]["Birthday"],)
        Birthday.pack(side = LEFT)

    if C2.get() == True:
        favoutiteframe = Frame(infoframe)
        favoutiteframe.pack(side = LEFT)
        favoutites = Text(favoutiteframe,height=10,width = 25)
        favoutites.insert(INSERT,"Favourite Gifts: ")

        favscroll = Scrollbar(favoutiteframe)
        favscroll.pack(side=RIGHT,fill = BOTH)

        for x in vildict[selectedvillager]["Favourite Gifts"]:
            favoutites.insert(INSERT,"\n"+x)
        favoutites.pack()

        favoutites.config(yscrollcommand = favscroll.set)
        favscroll.config(command = favoutites.yview)
    
main = Tk()
label = Label(main, text = "Stardew Valley Tools")
label.pack(side = TOP)
sprinkbutton = Button(main,text = "crop space calculator",width = 22, command = lambda:crop()) 
sprinkbutton.pack(side = TOP)
geodebutton = Button(main,text = "buying geodes from Krobus",width = 22, command = lambda:geode()) 
geodebutton.pack(side = TOP)
replacebutton = Button(main,text = "replacing grown crops",width = 22, command = lambda:replace()) 
replacebutton.pack(side = TOP)
vilagerbutton = Button(main,text = "villagers",width = 22, command = lambda:villagers()) 
vilagerbutton.pack(side = TOP)

main.mainloop()
