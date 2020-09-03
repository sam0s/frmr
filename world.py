from os import system
from time import gmtime
from calendar import timegm
from yaml import load as yload
import player

class WorldSpace:
    def __init__(self,name,tiles):
        self.tiles = tiles
        self.name = name
        self.dat=[]
        
    def dataAt(self,x,y):
        for i in self.dat:
            if i[1] == x:
                if i[0] == y:
                    return i
                    
                    
    def saveData(self,new,tiles):
        try:
            self.dat.append(new)
            file = open("save//levelData//"+self.loc+".dat",'w')
            print(self.dat,file=file)
            file.close()
            self.loadData(tiles)
        except FileNotFoundError:
            pass
    
    def loadData(self,tiles):
        try:
            file = open("save//levelData//"+self.loc+".dat",'r')
            self.dat=yload(file.read())
            file.close()
            if not self.dat:
                file = open("save//levelData//"+self.loc+".dat",'w')
                self.dat=[]
                print("[]",file=file)
                file.close()
            if self.dat:
                for item in self.dat:
                    self.tiles[item[1]][item[0]] = item[2]
                    for a in [i for i in list(tiles.values())]:
                        if a[0] == item[2]:
                            if item[3]+a[1] < int(timegm(gmtime())):
                                self.tiles[item[1]][item[0]] = item[2].upper()
        except FileNotFoundError:
            self.dat=[]
            file = open("save//levelData//"+self.loc+".dat","w")
            print("[]",file=file)
            file.close()

    def show(self,playerPos):
        system('cls||clear')
        print (self.name)
        x=0
        y=0
        for row in self.tiles:
            for block in row:
                if [y,x]==playerPos:
                    print("\033[1m"+"@"+"\033[0m",end="")
                else:
                    print (block,end="")
                x+=1
            print ("\n",end="")
            x=0
            y+=1

def loadLevel(loc,name):
    file = open("prefab//"+loc+".pfb")
    content = file.read()
    tiles = []
    tempTiles = []
    for i in content:
        if i == ".":
            tiles.append(tempTiles)
            tempTiles=[]
            break
        if i == "\n":
            tiles.append(tempTiles)
            tempTiles=[]
            continue
        tempTiles.append(i)
    a=WorldSpace(name,tiles)
    a.loc = loc
    return a

class shopInterface:
    def __init__(self,player):
        self.player = player
        self.itemlist=["Carrot"]
        opts = {}
        keyDict = {}
        x=0
        for a in self.itemlist:
            name=MENU_CHOICES[x]+" - "+"%s (%s)"%(a,self.itemlist[a])
            opts[name] = MENU_CHOICES[x]
            keyDict[MENU_CHOICES[x]] = a
            x+=1
    def show(self,buysell):
        system("cls||clear")
        print(f"Store -- {buysell}")
        print(f"Welcome! What would you like to {buysell}?")
        print(itemlist)
        
        
        
        
        