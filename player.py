from yaml import load as yload
weareonwindows=0
try:
    from getch import getch
except ModuleNotFoundError:
    weareonwindows=1
    import msvcrt
import gameInteractions,menu

f=open("tiles.txt")
TILE_TABLE = yload(f.read())
f.close()

class Player:
    def __init__(self,myWorld,where):
        self.pos=[]
        self.goingtohell=0
        self.TILE_TABLE=TILE_TABLE
        self.inv={}
        for i in self.TILE_TABLE:
            self.inv[i] = 1
        self.myWorld = myWorld
        self.where = where
        #actual world obj
        self.worldPos = self.myWorld[self.where[0]][self.where[1]]
        f=open("keybindings.txt")
        self.actions=yload(f.read())
        f.close()
        if type(self.actions)!=type({"1":1}):
            exit(1)

    def turn(self):
        self.worldPos.show(self.pos)
        print("World Pos: %s\nSpace Pos: %s"%(self.where,self.pos))
        print("?")
        inChr=''
        while (inChr not in (list(self.actions ) ) ):
            inChr=msvcrt.getch().decode('ASCII')
        self.action(inChr)

    def moveWorld(self,direction):
        if direction == "down":
            self.where[0]+=1
            self.worldPos = self.myWorld[self.where[0]][self.where[1]]
            self.pos[0]=1
        if direction == "up":
            self.where[0]-=1
            self.worldPos = self.myWorld[self.where[0]][self.where[1]]
            self.pos[0]=5
        if direction == "left":
            self.where[1]-=1
            self.worldPos = self.myWorld[self.where[0]][self.where[1]]
            self.pos[1]=18
        if direction == "right":
            self.where[1]+=1
            self.worldPos = self.myWorld[self.where[0]][self.where[1]]
            self.pos[1]=1
        self.worldPos.loadData(self.TILE_TABLE)

    def showInventory(self):
        opts={}
        print(self.inv)
        input()
        for a in self.inv:
            opts["%s (%s)"%(a,self.inv[a])]="x"
        m=menu.Menu("Your inventory.",opts,True)
        choice=m.show()

    def action(self,act):
        a = self.actions[act]
        lastPos = [self.pos[0],self.pos[1]]
        if a == "inventory":
            self.showInventory()
        if a == "quit":
            exit(1)
        if a == "interact":
            gameInteractions.tile(self.worldPos.tiles[self.pos[0]][self.pos[1]],self)
        if a == "up":
            self.pos[0]-=1
        if a == "down":
            self.pos[0]+=1
        if a == "left":
            self.pos[1]-=1
        if a == "right":
            self.pos[1]+=1
        try:
            (self.worldPos.tiles[self.pos[0]][self.pos[1]])
            if self.pos[0]==-1:
                raise IndexError('move up')
            if self.pos[1]==-1:
                raise IndexError('move left')
        except IndexError:
            self.pos = lastPos
            self.moveWorld(self.actions[act])
        if (self.worldPos.tiles[self.pos[0]][self.pos[1]]) == "#":
            self.pos = lastPos
        print(self.actions[act])
