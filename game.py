#import
from os import system as bash
import random, time, colors
from classes import Scene, Clock, Game, Village, Player#Inventory

#definitions
riverside = Scene("Riverside", ["Berries", "Mushrooms", "Tree Bark", "Plant Fibre", "Dead Grass", "hare flesh", "Bones", "Fishing Bait", "String"], True)
mountain_top = Scene("Top of the Mountain", ["Tree Bark", "Plant Fibre", "Dead Grass", "Bones", "Water Puddle", "Dead Birds", "Birds Nest", "String"])
forest = Scene("Middle of Forest", ["Berries", "Mushrooms", "Tree Bark", "Plant Fibre", "Dead Grass", "hare flesh", "Bones", "Water Puddle", "Fishing Bait", "Bird Nest", "String"])
desert = Scene("Desert", ["Cacti", "Dead Cacti Skin", "Tree Bark", "Stick", "Bones", "Dead Grass"], False)
mountain_side = Scene("Mountain Side", ["Tree Bark", "Plant Fibre", "Dead Grass", "Bones", "Water Puddle", "Dead Birds", "Fishing Bait", "Bird Nest"])
SCENES = [riverside, mountain_top, forest, desert, mountain_side]

all_items = ["Axe", "Fishing Bait", "Bandage", "Batteries", "Bear Flesh", "Berries", "Bird Nest", "Birds Nest", "Bone Knife", "Bones", "Bow Drill", "Camel Flesh", "Camp Set", "Cacti", "Cheetah Flesh", "Cloth", "Clothing", "Cooking Set", "Cow Flesh", "Dead Birds", "Dead Cacti Skin", "Dead Grass", "hare flesh", "Deer Flesh", "Empty Bottle", "Energy Bar", "Fish", "Fishing Rod", "Fox Flesh", "Full Bottle Of Clean Water", "Full Bottle Of Dirty Water", "Hygiene Kit", "Lion Flesh", "Magnesium Fire Starter", "Match", "Mushrooms", "Pig Flesh", "Plant Fibre", "Poisonous scorpion Flesh", "Rabbit Flesh", "Rabbit Skin", "scorpion Flesh", "Sleeping Bag", "Stick", "String", "Tea Leaves", "Tinder", "Toad Flesh", "Torch", "Tree Bark", "Vaseline", "Walking Stick", "Warming Pack", "Water Puddle", "Wolf Flesh", "Wood"]
startitems = ["Full Bottle of Dirty Water", "Full Bottle of Clean Water", "Full Bottle of Clean Water", "Energy Bar", "Bandage", "Walking Stick", "Match", "Match", "Match", "Tea Leaves", "Cooking Set", "Silver", "Silver", "Silver", "Clothing"]
randomstarting1 = ["Magnesium Fire Starter", "Warming Pack", "Sleeping Bag", "Axe", "Torch", "Fishing Rod"]
randomstarting2 = ["Batteries", "Vaseline", "Hygiene Kit", "String", "Camp Set", "Fishing Bait"]

game = Game(SCENES, all_items, startitems, randomstarting1, randomstarting2)
#functions
def Custom_Input():
    return input(colors.gray + ">>> " + colors.stopcolor).strip().lower()

def GenerateRandomScene():
    #randomly pick a scene, a starting item from each of 2 unique starting item lists, and an integer distance to home in [150km through 200km]
    global startitems
    global randomstarting1
    global randomstarting2
    scene = random.choice(SCENES)
    startitems.append(random.choice(randomstarting1))
    startitems.append(random.choice(randomstarting2))
    distance = random.randint(150, 250)
    return distance, scene, startitems

def GenerateRandomExplore(scene):
    #return 0, 1, or 2 random items of those available in this scene
    retlist = []
    for i in range(random.randint(0, 2)):
        retlist.append(random.choice(scene.items_available))
    return retlist

def GetWood(inventory):
    #returns number of wood gathered
    if "Axe" in inventory:
        minnum = 3
        maxnum = 7
    else:
        minnum = 1
        maxnum = 5
    return random.randint(minnum, maxnum)

def Fishing(inventory):
    #returns the fish that appeared
    bash("clear")
    fishes = ["guppy", "guppy", "guppy", "swordfish", "guppy", "goldfish", "goldfish"]
    if "Fishing Bait" in inventory:
        print("Do you want to use your fishing bait? \nIt will give you better odds of getting a bigger fish")
        print(colors.gray + "Y / N" + colors.stopcolor)
        confirmation = Custom_Input()
        if confirmation == "y":
            bash("clear")
            fishes.append("platinum arowana")
            fishes.append("platinum arowana")
            fishes.append("bass")
            fishes.append("bass")
            inventory.remove("Fishing Bait")
        if confirmation == "n":
            bash("clear")
        else:
            bash("clear")
            print(colors.orange + "'Y' or 'N' plz" + colors.stopcolor)

    hygiene = SearchItem("Hygiene Kit", inventory)
    if hygiene != 0:
        for i in range(2):
            fishes.append("bass")
            fishes.append("swordfish")
    appear = random.choice(fishes)
    return appear

def Hunting(scene, inventory):
    #returns the animal that appeared and whether or not you got injured
    hygiene = SearchItem("Hygiene Kit", inventory)
    prey = ["bear", "lion", "cheetah", "deer", "cow", "pig", "fox", "wolf", "rabbit", "toad", "", "", ""]

    if hygiene != 0:
        for i in range(2):
            prey.append("deer")
            prey.append("cow")
            prey.append("pig")
            prey.append("fox")
            prey.append("wolf")
            prey.append("rabbit")
            prey.append("toad")
    desertprey = ["camel", "", "", "", "", "scorpion", "poisonous scorpion"]
    if scene == "Desert":
        appear = random.choice(desertprey)
        if appear == "poisonous scorpion":
            return [appear, "major"]
        else:
            return [appear, "True"]
    else:
        appear = random.choice(prey)
        if appear in ["bear", "lion", "cheetah"]:
            success = random.choice(["True", "False", "False", "False"])
            if success == "False":
                injury = random.choice(["leg", "arm", "chest", "broken ribs", "broken leg", "neck", "major"])
                return [appear, injury]
            else:
                return [appear, success]
        else:
            return [appear, "True"]

def Menu(hydration, heat, watersource, dist, saturation, inventory):
    #Main Menu
    try:
        fishingrod = SearchItem("Fishing Rod", inventory)
    except:
        pass
    print(timer.report())
    time.sleep(0.01)
    print(colors.blue + "1. Chop Trees")
    time.sleep(0.01)
    print("2: Make Fire")
    time.sleep(0.01)
    print("3: Discover")
    time.sleep(0.01)
    print("4: Rest")
    time.sleep(0.01)
    print("5: Hunt")
    time.sleep(0.01)
    print("6: Walk Torwards Home")
    time.sleep(0.01)
    if found_village and not village_explored:
        time.sleep(0.01)
        print("There is a village nearby")
        time.sleep(0.01)
        print("6.1: Explore Village")
        time.sleep(0.01)
    if found_village and village_explored:
        time.sleep(0.01)
        print("You can now loot that village or trade with it")
        time.sleep(0.01)
        print("6.2: Loot Village")
        time.sleep(0.01)
        print("6.3: Trade With Village")
        time.sleep(0.01)
    print("7: Craft")
    time.sleep(0.01)
    print("8: View Inventory")
    time.sleep(0.01)
    print("9: Drink Water")
    time.sleep(0.01)
    print("10: Eat")
    time.sleep(0.01)
    print("11: Use Items") 
    time.sleep(0.01) 
    if not watersource:
        time.sleep(0.01)
        print("12. Build Shelter" + colors.stopcolor)
    else:
        time.sleep(0.01)
        print("12. Build Shelter")
    try:
        if watersource and fishingrod:
            time.sleep(0.01)
            print("There are Water Sources around You")
            time.sleep(0.01)
            print("13. Get Water")
            time.sleep(0.01)
            print("14. Catch Fish" + colors.stopcolor)
            time.sleep(0.01)
        elif watersource:
            print("There are Water Sources around You")
            time.sleep(0.01)
            print("13. Get Water" + colors.stopcolor)
            time.sleep(0.01)
    except:
        pass
    print(colors.green + "Hydration: "+str(hydration))
    time.sleep(0.01)
    print("Body Heat: "+ str(heat))
    time.sleep(0.01)
    print("Saturation: "+ str(saturation))
    time.sleep(0.01)
    print("Health: " + str(health))
    time.sleep(0.01)
    print(colors.purple + "Distance to Home: "+str(dist) + " km" + colors.stopcolor)
    time.sleep(0.01)
    return [input(colors.gray + "Action >>> " + colors.stopcolor),timer.isnight()]

def Intro():
    #Introductory Scene
    distance, scene, inventory = GenerateRandomScene()
    #bash("clear")
    time.sleep(0.01)
    print(colors.gray + "This game is all about your survival techinques")
    time.sleep(0.01)
    print("Your character is trapped in/on a " + colors.orange + scene.name + colors.gray)
    time.sleep(0.01)
    print("The distance to home is " + colors.purple + str(distance)+ " km" + colors.stopcolor)
    time.sleep(0.01)
    print(colors.gray + "https://jaredvititoe.com/Games/text_adventure/text_adventure.html" + colors.stopcolor)
    time.sleep(0.01)
    print(colors.gray + "Click Link \u21D1 To Play On My Website!" + colors.stopcolor)
    return distance, scene, inventory

def Walk(dist, saturation, hydration, heat, inventory):
    #retruns how far you walked with and hydration and heat loss
    if "Walking Stick" in inventory:
        maxwalking = 20
    else:
        maxwalking = 12
    if timer.isnight() and ("Torch" not in inventory):
        maxwalking = 5

    walked = random.randint(5, maxwalking)
    dist -= walked
    hydration -= 10
    saturation -= 10
    if "Clothing" not in inventory and timer.isnight():
        heat -= 20
    global shelter, found_village
    shelter = False
    #found_village = random.choice([True, False, False, False, False])
    found_village = True
    return [walked, saturation, hydration, heat]

def DisplayInventory(inventory):
    #retruns inventory in a listed format
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
    print("\n")

def DrinkWater(inventory):
    #returns updated hydration value and edited inventory
    amtcount = []
    amtcountunique = []
    water = []
    for i in range(len(inventory)):
        if inventory[i] not in amtcountunique:
            amtcount.append([inventory[i], 1])
            amtcountunique.append(inventory[i])
        else:
            for x in amtcount:
                if inventory[i] == x[0]:
                    x[1] += 1
    for i in amtcount:
        if i[0] in ["Full Bottle of Clean Water", "Full Bottle of Dirty Water"]:
            water.append(i)
    if water[0][0] == "Full Bottle of Dirty Water":
        water[0], water[1] = water[1], water[0]
    bash("clear")
    print(colors.gray + "You have: ")
    if len(water) != 0:
        for i in range(len(water)):
            print(colors.orange + str(i+1) + ". " + str(water[i][1]) + " x " + str(water[i][0]) + colors.stopcolor)
        print(colors.gray + "Which water would you want to drink?" + colors.stopcolor)
        waters = Custom_Input()
        if waters == "1":
            if water[0][1] - 1 >= 0:
                inventory.remove("Full Bottle of Clean Water")
                inventory.append("Empty Bottle")
                return [50, inventory]
        elif waters[0] == "2":
                if water[1][1] - 1 >= 0:
                    inventory.remove("Full Bottle of Dirty Water")
                    inventory.append("Empty Bottle")
                    if random.randint(1, 10)  < random.randint(1, 10):
                        return [30, inventory]
                    else:
                        bash("clear")
                        print(colors.orange + "The water is contaminated. Hydration - 30!" + colors.stopcolor)
                        return [-30, inventory]
        else:
            print("No Clean Water or You Typed It In Wrong")
    else:
        print("You have no water supplies")

def CheckValidBody(x):
    #checks to see if a value is below zero and if it is then it will return 0 for that value
    if x < 0:
        x = 0
    return x

def SearchItem(item, inventory):
    #searches and counts items inside of inventory
    amtcount = []
    amtcountunique = []
    for i in inventory:
        if i not in amtcountunique:
            amtcount.append([i, 1])
            amtcountunique.append(i)
        else:
            for x in amtcount:
                if i == x[0]:
                    x[1] += 1
    for i in amtcount:
        if i[0] == item:
            amount = i[1]
    try:
        return amount
    except:
        return 0

def ReplaceItem(item, changeto, inventory):
    #replaces an item into another
    inventoryx = list(inventory)
    for i in range(inventoryx.count(item)):
        inventoryx.remove(item)
        inventoryx.append(changeto)
    return inventoryx

def SearchFood(inventory):
    #returns updated inventory and energy value to be added to saturation
    food = ["berries",
            "mushrooms",
            "bear flesh",
            "lion flesh",
            "cheetah flesh",
            "deer flesh",
            "cow flesh",
            "pig flesh",
            "fox flesh",
            "wolf flesh",
            "rabbit flesh",
            "toad flesh",
            "camel flesh",
            "scorpion flesh",
            "poisonous scorpion flesh",
            "hare flesh",
            "bass",
            "goldfish",
            "guppy",
            "swordfish",
            "platinum arowana"]
    energy = [15, 15, 40, 70, 70, 40, 50, 40, 20, 20, 40, 20, 40, 20, 20, 30, 40, 20, 10, 50, 100]
    ownedfood = []
    for i in inventory:
        if i in food:
            ownedfood.append(i)
    if len(ownedfood) == 0:
        print(colors.orange + "You do not have any food" + colors.stopcolor)
    else:
        DisplayInventory(ownedfood)
        print(colors.gray + "What do you want to eat? Please use " + colors.orange + "full name." + colors.stopcolor)
        consume = Custom_Input()
        if consume in ownedfood:
            bash("clear")
            owned = True
        else:
            bash("clear")
            owned = False
        if not owned:
            bash("clear")
            print("You do not have this food")
        else:
            inventory.remove(consume)
            
            if consume == "Rabbit Flesh":
                inventory.append("Rabbit Skin")
            for i in range(len(food)):
                if food[i] == consume:
                    energy = energy[i]
                    print(colors.orange + "Food + " + str(energy) + colors.stopcolor)

            return [inventory, energy]

def CraftingList():
    #list of craftable items
    bash("clear")
    print(colors.orange + ">>> Crafting List <<<" + colors.stopcolor)
    print(colors.orange + "1. Tinder: " + colors.gray + "1 x Wood > " + colors.orange + "3 x Tinder" + colors.stopcolor)
    print(colors.orange + "2. String: " + colors.gray + "1 x Plant Fibre > " + colors.orange + " x String" + colors.stopcolor)
    print(colors.orange + "3. String: " + colors.gray + "1 x Dead Grass > " + colors.orange + "1 x String" + colors.stopcolor)
    print(colors.orange + "4. String: " + colors.gray + "1 x Cloth > " + colors.orange + "2 x String" + colors.stopcolor)
    print(colors.orange + "5. Cloth: " + colors.gray + "1 x Clothing > " + colors.orange + "3 x Cloth ***Tearing Clothes will increase the rate of heat loss during night!" + colors.stopcolor)
    print(colors.orange + "6. Bow Drill: " + colors.gray + "1 x String, 2 x Wood > " + colors.orange + "1 x Bow Drill" + colors.stopcolor)
    print(colors.orange + "7. Bone Knife: " + colors.gray + "1 x Bone, 1 x String > " + colors.orange + "1 x Bone Knife" + colors.stopcolor)
    print(colors.orange + "8. Bandage: " + colors.gray + "1 x Cloth > " + colors.orange + "3 x Bandage" + colors.stopcolor)
    print(colors.orange + "9. Torch: " + colors.gray + "1 x Wood, 1 x String, 1 x Vaseline, 1 x Tree Bark > " + colors.orange + "1 x Torch" + colors.stopcolor)
    print(colors.orange + "10. Fishing Rod: " + colors.gray + "1 x Wood, 1 x String, 1 x Bone Knife > " + colors.orange + "1 x Fishing Rod" + colors.stopcolor)
    print(colors.orange + "11. Water Bottle: " + colors.gray + "1 x Rabbit Skin > " + colors.orange + "1 x Water Bottle" + colors.stopcolor + "\n")
    print(colors.blue + "Orange is what you are crafting, Gray is what you need to craft it. If you wish to exit press 0." + colors.stopcolor)
    print("\n" + colors.blue + "Please type a number." + colors.stopcolor + "\n")
    return Custom_Input()

def CraftItem(inventory, required_materials, crafted):
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

def MakeFire(inventory):
    #returns body heat value to be added as well as edited inventory and whether or not the fire lighted
    fire_lighted2 = FireLightingMethod(inventory)
    if fire_lighted2:
        bash("clear")
        print(colors.orange + "Fire Lighted!")
        print("Body Heat + 30!" + colors.stopcolor)
        return [30, inventory, True]
    else:
        bash("clear")
        print(colors.orange + "Fire Failed To Light")
        return [0, inventory, False]

def FireLightingMethod(inventory):
    
    lightingitems = ["Bow Drill", "Match", "Magnesium Fire Starter", "Batteries"]
    ownedlighting = []
    for i in inventory:
        if i in lightingitems:
            ownedlighting.append(i)
    bash("clear")
    print(colors.gray + "You have these lighting items:")
    DisplayInventory(ownedlighting)
    print(colors.gray + "Which one do you want to use to light? " + colors.orange + "Please use full name." + colors.stopcolor)
    tolight = Custom_Input()
    tolight = tolight.title()
    for i in ownedlighting:
        if tolight == i:
            removeitem = i
            inventory.remove(removeitem)
            fire_lighted = True            
            break
        elif tolight != i:
            fire_lighted = False
    if not ownedlighting:
        fire_lighted = False
        print("No Available Items To Light Fire")
    """
    for i in inventory:
        if i == "Tinder":
            if tolight == "match":
                inventory.remove(removeitem)
                inventory.remove("Tinder")
            else:
                inventory.remove("Tinder")
                """
    return fire_lighted

def UseableItemsOutput(inventory):
    try:
        useableitems = ["Tea Leaves", "Warming Pack", "Energy Bar", "Bandage"]
        useableowned = []
        for i in inventory:
            if i in useableitems:
                useableowned.append(i)
        if len(useableowned) != 0:
            DisplayInventory(useableowned)
            print(colors.gray + ">>> Which one do you want to use? <<<" + colors.stopcolor)
            print(colors.gray + ">>> Please type in the " + colors.blue + "full item name" + colors.gray + " <<<" + colors.stopcolor)
            use = input(colors.gray + ">>>" + colors.stopcolor)
            use = use.title().strip()
            for i in useableowned:
                if use == i:
                    inventory.remove(i)
                    return[inventory, i]
        else:
            print("You do not own any useable items")
            return inventory
    except(TypeError, AttributeError):
            bash("clear")
            print(colors.orange + "⚠ This is not a valid input ⚠")
            return inventory

def UsedItem(hydration, heat, saturation, health, useitem):
    useableitems = ["Tea Leaves", "Warming Pack", "Energy Bar", "Bandage"]
    if useitem not in useableitems:
        raise ValueError
        print("item to use is not in the Useable Items List!")
    else:
        if useitem == useableitems[0]:
            hydration += 100
            bash("clear")
            print(colors.orange + "Hydration + 100" + colors.stopcolor)
            
        elif useitem == useableitems[1]:
            heat += 100
            bash("clear")
            print(colors.orange + "Heat + 100" + colors.stopcolor)
        elif useitem == useableitems[2]:
            saturation += 100
            bash("clear")
            print(colors.orange + "Saturation + 100" + colors.stopcolor)
        
        elif useitem == useableitems[3]:
            health += 25
            bash("clear")
            print(colors.orange + "Health + 25" + colors.stopcolor)

        return [hydration, heat, saturation, health]


#Variables
dist, scene, copy_me_inventory = Intro()
timer = Clock()
village_names = ["Clumkundo", "Intik", "Cesi", "Twimkug", "Galfall", "Dipo"]
village_items = ["Batteries", "Warming Pack",  "Match", "Match", "Full Bottle of Clean Water", "Full Bottle of Clean Water", "Fishing Bait","Silver","Silver","Silver"]
random_village_items = random.sample(village_items, 2)
villageinstance = Village(copy_me_inventory, random.choice(village_names), True, random.randint(3,500), random_village_items[0], random_village_items[1])
village_names.remove(villageinstance.name)
hydration = 100
heat = 100
saturation = 100
health = 100
shelter = False
found_village = False
village_explored = False
inventory = copy_me_inventory
while dist > 0:
    if hydration > 0 and heat > 0 and saturation > 0:
        player = Player(inventory, startitems)
        action = Menu(hydration, heat, scene.water, dist, saturation, inventory)
        action = action[0]
        if action == "1":
            bash("clear")
            timer.add(1)
            woody = player.getwood(timer.isnight(), saturation, hydration, heat)
            print(colors.orange + "" + str(woody[0]) + " log(s) are obtained" + colors.stopcolor)
            print(colors.orange + "You used 1 hour to collect some logs" + colors.stopcolor)
            saturation = woody[1]
            hydration = woody[2]
            heat = woody[3]
            saturation = CheckValidBody(saturation)
            hydration = CheckValidBody(hydration)
            heat = CheckValidBody(heat)
        elif action == "2":
            fire = MakeFire(inventory)
            inventory = fire[1]
            heat += fire[0]
            if fire[2]:
                inventory = ReplaceItem("Full Bottle of Dirty Water", "Full Bottle of Clean Water", inventory)
                print(colors.orange + "Water Purified!" + colors.stopcolor)
        elif action == "3":
            if timer.isnight() == False:
                discover = GenerateRandomExplore(scene)
            else:
                discover = ["Nothing"]
            discover_str = ""
            if discover != []:
                for i in discover:
                    discover_str += i + ", "
                    inventory.append(i)
                bash("clear")
                if timer.isnight():
                    print(colors.orange+ "It is really dark outside, very difficult to see anything.")
                print(colors.orange + discover_str + "is/are obtained" + colors.stopcolor)
            else:
                bash("clear")
                print(colors.orange + "Nothing is found" + colors.stopcolor)
            timer.add(1)
            hydration -= 10
            saturation -= 10
            hydration = CheckValidBody(hydration)
            print(colors.orange + "You have used 1 hour to explore around you" + colors.stopcolor)
        elif action == "4":
            rested = player.rest(timer.isnight(), shelter, inventory, saturation, hydration, heat)
            timer.add(5)
            saturation = rested[0]
            hydration = rested[1]
            heat = rested[2]
            saturation = CheckValidBody(saturation)
            hydration = CheckValidBody(hydration)
            heat = CheckValidBody(heat)
        elif action == "5":
            captured = Hunting(scene, inventory)
            timer.add(1)
            if captured[1] == "True" and captured[0] != "poisonous scorpion":
                if captured[0]:
                    bash("clear")
                    print(colors.orange + "You saw a "+(captured[0]).capitalize()+" and you captured it" + colors.stopcolor)
                    inventory.append((captured[0])+" flesh")
                    print(colors.orange + "You have used 1 hour to hunt" + colors.stopcolor)
                    hydration -= 15
                    saturation -= 15
                    hydration = CheckValidBody(hydration)
                    saturation = CheckValidBody(saturation)
                    heat += 2
                    heat = CheckValidBody(heat)
                else:
                    bash("clear")
                    print(colors.orange + "You didn't see anything" + colors.stopcolor)
            elif captured[1] == "False":
                bash("clear")
                print(colors.orange + "You saw a "+(captured[0]).capitalize()+" and it escaped... bad luck!" + colors.stopcolor)
            else:
                bash("clear")
                print(colors.orange + "You saw a "+(captured[0]).capitalize()+" and it attacked you, causing a "+captured[1]+" injury!")
                if captured[1] in ["broken ribs", "major", "neck"]:
                    print(colors.red + "Health - 50")
                    health -= 50
                    CheckValidBody(health)
                else:
                    print(colors.red + "Health - 30")
                    health -= 30
                    CheckValidBody(health)
        elif action == "6":
            #walked = Walk(dist, saturation, hydration, heat, inventory)
            walked = player.walk(timer.isnight(), saturation, hydration, heat, found_village)
            timer.add(2)
            dist -= walked[0]
            saturation = walked[1]
            hydration = walked[2]
            heat = walked[3]
            found_village = walked[4]
            saturation = CheckValidBody(saturation)
            hydration = CheckValidBody(hydration)     
            heat = CheckValidBody(heat)
            scene.water = random.choice([True, False])
        elif action == "6.1":
            bash("clear")
            if found_village and not village_explored:
                print(colors.orange + "You have explored " + villageinstance.name + " with a population of " + str(villageinstance.population) + " people.")
                print(colors.orange + "There are now new options with that village!")
                village_explored = True
            else:
                print(colors.orange + "⚠ This is not a valid input!⚠")
        elif action == "6.2":
            bash("clear")
            if found_village and village_explored:
                inventory = villageinstance.Loot(inventory)
                village_explored = False
                found_village = False
            else:  
                print(colors.orange + "⚠ This is not a valid input!⚠")
        elif action == "6.3":
            bash("clear")
            if found_village and village_explored:
                #trade
                villageinstance.Add_Silver(inventory.count("Silver"))
                villageinstance.TradeList(inventory)
            trade_input = Custom_Input()
            village_explored = False
            found_village = False
            if trade_input == "1":
                inventory = CraftItem(inventory, ["Silver","Silver"], ["Bow Drill", "1"])
            elif trade_input == "2":
                inventory = CraftItem(inventory, ["Silver"], ["Bandage", "2"])
            elif trade_input == "3":
                inventory = CraftItem(inventory, ["Silver", "Silver", "Silver"], ["Bone Knife", "1"])
            elif trade_input == "4":
                inventory = CraftItem(inventory, ["Silver", "Silver"], ["Water Bottle", "1"])
            else:
                bash("clear")
                village_explored = True
                found_village = True
                print(colors.orange + "⚠ This is not a valid input!⚠")
        elif action == "7":
            craft = CraftingList()
            if craft == "0":
                bash("clear")
            elif craft == "1":
                inventory = CraftItem(inventory, ["Wood"], ["Tinder", "3"])
            elif craft == "2":
                inventory = CraftItem(inventory, ["Plant Fibre"], ["String", "2"])
            elif craft == "3":
                inventory = CraftItem(inventory, ["Dead Grass"], ["String", "1"])
            elif craft == "4":
                inventory = CraftItem(inventory, ["Cloth"], ["String", "3"])
            elif craft == "5":
                inventory = CraftItem(inventory, ["Clothing"], ["Cloth", "3"])
            elif craft == "6":
                inventory = CraftItem(inventory, ["String", "Wood", "Wood"], ["Bow Drill", "1"])
            elif craft == "7":
                inventory = CraftItem(inventory, ["Bones", "String"], ["Bone Knife", "1"])
            elif craft == "8":
                inventory = CraftItem(inventory, ["Cloth"], ["Bandage", "3"])
            elif craft == "9":
                inventory = CraftItem(inventory, ["Wood", "Vaseline", "String", "Tree Bark"], ["Torch", "1"])
            elif craft == "10":
                inventory = CraftItem(inventory, ["Wood", "String", "Bone Knife"], ["Fishing Rod", "1"])
            elif craft == "11":
                inventory = CraftItem(inventory, ["Rabbit Skin"], ["Water Bottle", "1"])
            else:
                bash("clear")
                print(colors.orange + "⚠ This is not a valid input!⚠")
        elif action == "8":
            DisplayInventory(inventory)
        elif action == "9":
            try:
                water = DrinkWater(inventory)
                hydration += water[0]
                bash("clear")
                print(colors.orange + "Hydration + " + str(water[0]))
                hydration = CheckValidBody(hydration)
                inventory = water[1]
            except:
                bash("clear")
                print(colors.orange + "No Water")
        elif action == "10":
            bash("clear")
            print(colors.orange + "Energy Bars are in Use Items Section." + colors.stopcolor)
            food = SearchFood(inventory)
            try:
                inventory = food[0]
                saturation += food[1]
                CheckValidBody(saturation)
            except:
                pass
        elif action == "11":
            try:
                check = UseableItemsOutput(inventory)
                inventory = check[0]
                used = check[1]
                useitem = UsedItem(hydration, heat, saturation, health, used)
                hydration = useitem[0]
                heat = useitem[1]
                saturation = useitem[2]
                health = useitem[3]
            except(TypeError):
                bash("clear")
                print(colors.orange + "⚠ This is not a valid input!⚠")
        elif action == "12":
            if "Camp Set" in inventory:
                timer.add(1)
                shelter = True
                bash("clear")
                print(colors.gray + "Remember shelter does not go with you when you walk torwards home." + colors.stopcolor)
                print(colors.orange + "Shelter has been Built, Rest would not decrease heat." + colors.stopcolor)
                print(colors.orange + "That took 1 hour" + colors.stopcolor)
            elif "Camp Set" not in inventory:
                if "Wood" in inventory:
                    timer.add(4)
                    ReplaceItem(None, "Wood", inventory)
                    shelter = True
                    bash("clear")
                    print(colors.gray + "Remember shelter does not go with you when you walk torwards home." + colors.stopcolor)
                    print(colors.gray + "Shelter has been Built, Rest would not decrease heat." + colors.stopcolor)
                    print(colors.orange + "That took 4 hours" + colors.stopcolor)
                    print(colors.orange + "Wood - 1" + colors.stopcolor)
                elif "Wood" not in inventory:
                    bash("clear")
                    print(colors.orange + "You need 1 Wood in order to build Shelter since you dont have a 'Camp Set'!")
            hydration -= 5
            saturation -= 5
            hydration = CheckValidBody(hydration)
            saturation = CheckValidBody(saturation)
        elif action == "13":
            if scene.water:
                emptybottles = SearchItem("Empty Bottle", inventory)
                if emptybottles == 0:
                    bash("clear")
                    print(colors.orange + "You do not have empty bottles" + colors.stopcolor)
                else:
                    inventory = ReplaceItem("Empty Bottle", "Full Bottle of Dirty Water", inventory)
                    bash("clear")
                    print(colors.orange + str(emptybottles) + " x Empty Bottles have been filled up to " + str(emptybottles) + " x Full Bottle of Dirty Water" + colors.stopcolor)
            else:
                bash("clear")
                print(colors.orange + "⚠ This is not a valid input!⚠")
        elif action == "14":
            fishingrod = SearchItem("Fishing Rod", inventory)                   
            if scene.water and fishingrod:
                captured = Fishing(inventory)
                timer.add(2)
                bite = random.choice([True, True, False])
                if captured != "platinum arowana" and bite:
                    print(colors.orange + "You saw a "+(captured).capitalize()+" and you captured it" + colors.stopcolor)
                    inventory.append(captured)
                    print(colors.orange + "You have used 2 hours to fish" + colors.stopcolor)
                    hydration -= 10
                    hydration = CheckValidBody(hydration)
                    saturation -= 5
                    saturation = CheckValidBody(saturation)
                    heat += 2
                    heat = CheckValidBody(heat)
                if captured == "platinum arowana" and bite:
                    print(colors.orange + "YOU CAPTURED THE RARE PLATINUM AROWANA!!!")
                    inventory.append(captured)
                    print(colors.orange + "You have used 2 hours to fish" + colors.stopcolor)
                    hydration -= 10
                    hydration = CheckValidBody(hydration)
                    heat += 2
                    heat = CheckValidBody(heat)
                if captured and not bite:
                    print(colors.orange + "You saw a "+(captured).capitalize()+" and it escaped... bad luck!")
            else:
                bash("clear")
                print(colors.orange + "⚠ This is not a valid input!⚠")
        else:
                bash("clear")
                print(colors.orange + "⚠ This is not a valid input!⚠")
    else:
        if hydration <= 0:
            print(colors.red + "You died of thirst")
        elif heat <= 0:
            print(colors.red + "You died of hypothermia")
        elif saturation <= 0:
            print(colors.red + "You have starved to death")
        elif health <= 0:
            print(colors.red + "You died of lack of health")
        print("You had "+ str(dist) +" km to go")
        print("GAME OVER..." + colors.stopcolor)
        time.sleep(10)
        quit()
if dist <= 0 and hydration > 0 and heat > 0 and saturation > 0 and health > 0:
    print(colors.blue + "WELL DONE!\nYOU SURVIVED!!!!!")