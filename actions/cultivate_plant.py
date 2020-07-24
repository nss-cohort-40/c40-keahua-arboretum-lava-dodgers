import os
from plants import *

def cultivate_plant(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")
    print("")
    
    plant = int(input("Choose plant to cultivate >> "))

    if plant == 1:
        new_plant = Mountain_Apple()
        biomes_available = []

        for biome in arboretum.mountains:
            biomes_available.append(biome)
        if biomes_available == []:
            print("There are no biomes available for this plant. Please annex the proper biome before attempting to cultivate!")
            input("Press enter to continue >> ")
            return
        else:
            for x in range(len(biomes_available)):
                print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]}")
        
        biome_choice = int(input("Choose a biome > ")) - 1
        biomes_available[biome_choice].add_plant(new_plant)
        print(biomes_available[biome_choice].plants)
        
    else: 
        print("Fuck off")
        input("Press enter to fuck off... ")