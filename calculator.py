from tkinter import *

def calc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief=FLAT, textvariable=display, justify='right', bd=30, bg="blue").pack(side=TOP, expand=YES, fill=BOTH)

        for clearBut in (["CE"],["C"]):
            erase = calc(self, TOP)
            for ch in clearBut:
                button(erase, LEFT, ch, lambda storeObj = display, q = ch: storeObj.set(''))

        for num in ("789/", "456*", "123-", "0.+"):
            FunctionNum = calc(self, TOP)
            for ch in num:
                button(FunctionNum, LEFT, ch, lambda storeObj=display, q=ch: storeObj.set(storeObj.get() + q))    
        
        EqualsButton = calc(self, TOP)
        for ch in "=":
            if ch == '=':
                btnEquals = button(EqualsButton, LEFT, ch)
                btnEquals.bind('<ButtonRelease-1>', lambda e, s=self, storeObj=display: s.calc(storeObj), '+')

            else:
                btnEquals = button(EqualsButton, LEFT, ch, lambda storeObj=display, s='%s '%ch: storeObj.set(storeObj.get()+s)) 
                
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

if __name__ == '__main__':
    app().mainloop()