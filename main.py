VERSION = "frmr 1.0"
print ("loading %s . . ."%VERSION)
print ("... modules")
import world
import menu
import player
from shutil import rmtree
from os import mkdir

print ("... prefabs")

fh=world.loadLevel("farmHouse","Inside Farm House")
of=world.loadLevel("outsideFarmHouse","Outside Farm House")
ob=world.loadLevel("outsideBarn","Outside Barn")
br=world.loadLevel("barn","Inside Barn")
fo=world.loadLevel("fieldOutskirts","Field Outskirts")
lf=world.loadLevel("fieldl","Field")
te=world.loadLevel("the_exchange","Jack's Drop and Stop")
            
theWorld = [[lf,fh,br],
            [fo,of,ob],
            [te,0,0]]

p=player.Player(theWorld, [0,1])
p.pos=[5,10]
#load save file
opts={"(s)tart game":'s',"(r)eset save":'r',"(q)uit game":'q'}
mainMenu = menu.Menu(VERSION+"\n\nMain Menu",opts)

choice=mainMenu.show()

if choice == "s":
    while True:
        p.turn()
elif choice == "r":
    if menu.Menu("Reset save file?",{"(Y)es":"Y","(n)o":"n"}).show() == "Y":
        try:
            rmtree("save")
        except FileNotFoundError:
            pass
    mkdir("save")
    mkdir("save//levelData")
    print("Save file reset! See you soon!")
elif choice == "q":
    exit(1)
