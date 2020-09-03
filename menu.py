from os import system
from getch import getch
class Menu:
    def __init__(self,menu_name,opts,cancel=False):
        self.name = menu_name
        self.options=opts
        if cancel:
            self.options["\nx - cancel"] = 'x'
    def show(self):
        system('cls||clear')
        print (self.name)
        for i in self.options:
            print("%s"%i)
        inChr=''
        while (inChr not in (list(self.options.values() ) ) ):
            inChr=getch()
        return inChr
