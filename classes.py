import random, time, colors
from os import system as bash

#variables
silver_num_count = 0
silver_count = []

def DisplayInventory(inventory):
    #returns inventory in a listed format
    amtcount = []
    amtcountunique = []
    for i in range(len(inventory)):
        if inventory[i] not in amtcountunique:
            amtcount.append([inventory[i], 1])
            amtcountunique.append(inventory[i])
        else:
            for x in amtcount:
                if inventory[i] == x[0]:
                    x[1]+=1
    bash("clear")
    print(colors.gray + "You have:")
    for i in amtcount:
        print(colors.orange + str(i[1]) + " x " + str(i[0]) + colors.stopcolor)
def Custom_Input():
    return input(colors.gray + ">>> " + colors.stopcolor).strip().lower()
class Scene:
    def __init__(self, name, items_available=[], water=random.choice([True,False])):
        self.name = name
        self.items_available = items_available
        self.water = water
    def __eq__(self, b):
        #compare to a string or a Scene
        return self.name==str(b)
    def __str__(self):
        return self.name
class Clock:
    def __init__(self, night=False, hour=0):
        self.night = night
        self.hour = hour
    def isnight(self):
        return self.night
    def add(self, hours):
        self.hour += hours
        if self.hour >= 12:
            self.hour -= 12
            self.night = not self.night
    def report(self):
        if self.night:
            time.sleep(0.01)
            return colors.gray + "There are "+str(12-self.hour)+" hours of night time left \u23FE" + colors.stopcolor
        else:
            time.sleep(0.01)
            return colors.yellow + "There are "+str(12-self.hour)+" hours of day time left \u2600" + colors.stopcolor
class Village:
    def __init__(self, inventory, name, relation, population, content, content2):
        inventory = inventory
        self.name = name
        self.relation = relation
        self.population = population
        self.content = content
        self.content2 = content2
    def Loot(self, inventory):
        inventory.append(self.content)
        inventory.append(self.content2)
        print(colors.orange + "You looted:",self.content,self.content2)
        return inventory
    def Add_Silver(self, x):
        global silver_num_count
        silver_num_count += x
        for i in range(silver_num_count):
            silver_count.append("Silver")
    def TradeList(self, inventory):
        DisplayInventory(silver_count)
        #list of tradable items
        print(colors.orange + "\n>>> Trading List <<<" + colors.stopcolor)
        print(colors.orange + "1. Bow Drill: " + colors.gray + "2 x Silver > " + colors.orange + "1 x Bow Drill" + colors.stopcolor)
        print(colors.orange + "2. Bandages: " + colors.gray + "1 x Silver > " + colors.orange + "2 x Bandages" + colors.stopcolor)
        print(colors.orange + "3. Bone Knife: " + colors.gray + "3 x Silver > " + colors.orange + "1 x Bone Knife" + colors.stopcolor)
        print(colors.orange + "4. Water Bottle: " + colors.gray + "2 x Silver > " + colors.orange + "1 x Water Bottle" + colors.stopcolor + "\n")
        print(colors.blue + "Orange is what you are trading, Gray is what you need to trade it." + colors.stopcolor)
        print(colors.blue + "Which one do you want to trade?" + colors.stopcolor + "\n")
    def TradeItem(self, inventory, required_materials, crafted):
        #returns inventory with new or not new items.
        amtcount = []
        amtcountunique = []
        consumestr = ""
        for i in range(len(required_materials)):
            if required_materials[i] not in amtcountunique:
                amtcount.append([required_materials[i], 1])
                amtcountunique.append(required_materials[i])
            else:
                for x in amtcount:
                    if required_materials[i] == x[0]:
                        x[1]+=1
        for i in amtcount:
            consumestr = consumestr + str(i[1])+" x "+str(i[0]) + " "
        craftedstr = str(crafted[1])+" x "+str(crafted[0])
        print(colors.blue + "Crafting " + str(craftedstr) + " will consume " + str(consumestr) + colors.stopcolor)
        print(colors.gray + "Are you sure?" + colors.stopcolor)
        print(colors.gray + "Y / N" + colors.stopcolor)
        confirmation = Custom_Input()
        bash("clear")
        if confirmation == "y":
            try:
                for i in required_materials:
                    inventory.remove(i)
                for i in range(int(crafted[1])):
                    inventory.append(crafted[0])
                return inventory
            except:
                bash("clear")
                print(colors.gray + "You are missing some indgredients" + colors.stopcolor)
                return inventory
        elif confirmation == "n":
            bash("clear")
            return inventory
        else:
            print(colors.orange + "'Y' or 'N' plz" + colors.stopcolor)
            return inventory
class Player:
    def __init__(self, inventory, startitems, hydration=100, heat=100, saturation=100):
        self.inventory = inventory
        #for item in startitems:
        #    inventory.append(item)
        self.hydration=hydration
        self.heat=heat
        self.saturation=saturation
    def has(self, item):
        try:
            return self.inventory.count(item) > 0
        except AttributeError:
            print("AttributeError")
    def getwood(self, night, saturation, hydration, heat):
        if night:
            wood = random.randint(0,2)
            heat -= 10
            print(colors.orange + "Wood output reduced as it is night time and its cold." + colors.stopcolor)
        else:
            if "Axe" in self.inventory:
                wood = random.randint(3,7)
                print(colors.orange + "You chopped very efficiently with your axe! Odds of extra wood were increased." + colors.stopcolor)
            else:
                wood = random.randint(1,5)
        for i in range(wood):
            self.inventory.append("Wood")
        
        saturation -= 15
        hydration -= 15
        return wood, saturation, hydration, heat
    def makefire(self):
        pass
    def discover(self, scene, night):
        #cost
        self.hydration -= 10
        self.saturation -= 10
        #
        retlist = []
        if not night:
            for i in range(random.randint(0,2)):
                retlist.append(random.choice(scene.items_available))
        for item in retlist:
            self.inventory.append(item)
        return retlist
    def rest(self, night, shelter, inventory, saturation, hydration, heat):
        bash("clear")
        print(colors.orange + "You have used 5 hours to rest" + colors.stopcolor)
        hydration -= 5
        saturation -= 5
        if (shelter) or ("Sleeping Bag" in inventory and night):
            pass
        elif night and not "Sleeping Bag" in inventory:
            heat -= 30
        return saturation, hydration, heat
    def hunt(self):
        pass
    def walk(self, night, saturation, hydration, heat, found_village):
        bash("clear")
        #cost
        hydration -= 10
        saturation -= 10
        if not self.has("Clothing") and night:
            heat -= 20
        maxwalking = 12
        if self.has("Walking Stick"):
            maxwalking = 20
        else:
            maxwalking = 10
        if night and not self.has("Torch"):
            maxwalking = 5
        walked = random.randint(1,maxwalking)
        shelter = False
        found_village = random.choice([True, False, False, False, False])
        print(colors.orange + "You have used 2 hours to walk " + str(walked) + " km\n" + colors.stopcolor)
        return walked, saturation, hydration, heat, found_village, shelter
    def craft(self):
        pass
    
    def fish(self):
        pass
    
    
    #fish, drinkwater, craftitem
class Inventory:
    def __init__(self, items=[]):
        self.items = dict.fromkeys(items, 0)
    def searchitem(self, item):
        return item.count()
'''
class Inventory:
    def __init__(self, items=[]):
        self.items = dict.fromkeys(items, 0)
    def searchitem(self, item):
        #returns how many copies of item are held
        try:
            return self.items[item]
        except KeyError:
            #item is not a valid item
            return 0
    def replaceall(self, item, changeto):
        try:
            n = self.items[item]
            self.items[changeto]+=n
        except KeyError:
            #item or changeto is not a valid item
            pass
    def add(self, item, number=1):
        try:
            self.items[item]+=number
        except KeyError:
            #item is not a valid item
            pass
    #items
    #display?, removeitem, searchfood, usableitemsoutput?
'''
class Game:
    def __init__(self, scenes, all_items, startitems, randomstarting1, randomstarting2):
        self.time = Clock()
        #self.player = Player(Inventory(all_items),startitems)
        self.generaterandomstart(scenes, randomstarting1, randomstarting2)
    def generaterandomstart(self, scenes, randomstarting1, randomstarting2):
        self.dist = random.randint(150,200)
        self.scene = random.choice(scenes)
        #self.player.inventory.append(random.choice(randomstarting1))
        #self.player.inventory.append(random.choice(randomstarting2))
    #actions?
    #menu, intro, DisplayInventory?, craftinglist, usableitemsoutput?
#class Acion:
    #name, number?
    #act
#class Item:
    #name, recipe
    #__str__
#class UsableItem(Item):
    #
    #use
#class Food(Item): #or maybe inherit from UsableItem
    #
    #eat
#class Prey:
#    def __init__(self, name, damage):
#        self.name = name
#        self.damage = damage
#bear = Prey("Poisonous Scorpion", "major")