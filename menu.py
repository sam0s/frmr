from os import system
weareonwindows=0
try:
    from getch import getch
except ModuleNotFoundError:
    weareonwindows=1
    import msvcrt
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
            inChr=msvcrt.getch().decode('ASCII')
        return inChr
