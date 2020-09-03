import menu
from time import gmtime
from calendar import timegm

MENU_CHOICES=["a","b","c","d","e","f","A","B","C","D","E","F"]

def get_key(val,my_dict): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key

def tile(tile,player):
    for i in list(player.TILE_TABLE.values()):
        if tile in i:
            tile_name = get_key(i,player.TILE_TABLE)
            time = player.worldPos.dataAt(*player.pos)[3] - timegm(gmtime())
            m=menu.Menu(f"Remove this {tile_name} from the ground?",{"(Y)es":"y","(N)o":"n"})
            choice=m.show()
            if choice == "y":
                print("remove?")
            return
        
        if tile.lower() in i and tile.lower()!=tile:
            tile_name = get_key(i,player.TILE_TABLE)
            m=menu.Menu(f"This {tile_name} is ready for harvest!\nProceed to harvest it?",{"(Y)es":"y","(N)o":"n"})
            choice=m.show()
            if choice == "y":
                player.inv[tile_name.upper()] = 1
            return
                
    if tile == "B":
        m=menu.Menu("This is a bed, would you like to sleep and save your game?",{"(Y)es":"y","(N)o":"n"})
        choice=m.show()
        return
    if tile == "*":
        opts = {}
        keyDict = {}
        x=0
        for a in player.inv:
            name=MENU_CHOICES[x]+" - "+"%s (%s)"%(a,player.inv[a])
            opts[name] = MENU_CHOICES[x]
            keyDict[MENU_CHOICES[x]] = a
            x+=1
        m=menu.Menu("There is enough space here to plant something small.",opts,True)
        choice=m.show()
        if not (choice == "x"):
            player.inv[keyDict[choice]]-=1
            player.worldPos.saveData([player.pos[1],player.pos[0],player.TILE_TABLE[keyDict[choice]][0],timegm(gmtime())],player.TILE_TABLE)
        return
    if tile == "x":
        opts = {"a - crop1":"a","b - crop2":"b"}
        m=menu.Menu("There is enough space here to plant something large.",opts,True)
        choice=m.show()
        return
        