from tkinter import*

wind = Tk()
wind.title("Calculator")
display = Entry(wind,width=40)
display.grid(row=0,column=0,columnspan = 4)
exp = ""
def click(clickedvalue):
    global exp
    exp = exp + str(clickedvalue)
    display.delete(0,END)
    display.insert(0,exp)
def equal():
    global exp
    res = eval(exp)
    display.delete(0,END)
    display.insert(0,res)
def clear():
    global exp
    display.delete(0,END)
    exp = ""
bu9 = Button(wind,text="9",height=4,width=10,command = lambda: click(9)).grid(row = 1, column = 0)
bu8 = Button(wind,text="8",height=4,width=10,command = lambda: click(8)).grid(row = 1, column = 1)
bu7 = Button(wind,text="7",height=4,width=10,command = lambda: click(7)).grid(row = 1, column = 2)
bu_plus = Button(wind,text="+",height=4,width=10,command = lambda: click("+")).grid(row = 1, column = 3)

bu6 = Button(wind,text="6",height=4,width=10,command = lambda: click(6)).grid(row = 2, column = 0)
bu5 = Button(wind,text="5",height=4,width=10,command = lambda: click(5)).grid(row = 2, column = 1)
bu4 = Button(wind,text="4",height=4,width=10,command = lambda: click(4)).grid(row = 2, column = 2)
bum = Button(wind,text="-",height=4,width=10,command = lambda: click("-")).grid(row = 2, column = 3)

bu3 = Button(wind,text="3",height=4,width=10,command = lambda: click(3)).grid(row = 3, column = 0)
bu2 = Button(wind,text="2",height=4,width=10,command = lambda: click(2)).grid(row = 3, column = 1)
bu1 = Button(wind,text="1",height=4,width=10,command = lambda: click(1)).grid(row = 3, column = 2)
bumu= Button(wind,text="*",height=4,width=10,command = lambda: click("*")).grid(row = 3, column = 3)

buc= Button(wind,text="C",height=4,width=10,command = clear).grid(row = 4, column = 0)
bue= Button(wind,text="=",height=4,width=10,command = equal).grid(row = 4, column = 1)
bu0= Button(wind,text="0",height=4,width=10,command = lambda: click(0)).grid(row = 4, column = 2)
bud= Button(wind,text="/",height=4,width=10,command = lambda: click("/")).grid(row = 4, column = 3)


wind.mainloop()
