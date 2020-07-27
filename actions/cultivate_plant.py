import os
from plants import *

def choose_plant():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")
    print("")
    
    plant = int(input("Choose plant to cultivate >> "))
    
    if plant == 1:
        return("Mountain Apple Tree")

    elif plant == 2:
        return("Silversword")

    elif plant == 3:
        return("Rainbow Eucalyptus Tree")
    
    elif plant == 4:
        return("Blue Jade Vine")

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("That number is not available. Please choose a plant from the list.")
        input("Press enter to return to the plant menu >>")
        return

def cultivate_plant(arboretum):
    plant = choose_plant()
    os.system('cls' if os.name == 'nt' else 'clear')

    #Cultivate Mountain Apple Tree
    if plant == "Mountain Apple Tree":
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
                print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]} | ({len(biomes_available[x].plants)}/4)")
        
        biome_choice = int(input("Choose a biome > ")) - 1

        if biome_choice + 1 > len(biomes_available):
            print("Please choose a biome number in the list.")
            input("Press enter to continue >>")
            return

        biomes_available[biome_choice - 1].add_plant(new_plant)       
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"The {plant} has successfully been cultivated!")
        input("Press enter to continue >>")

    #Cultivate Silversword
    if plant == "Silversword":
        new_plant = Silversword()
        biomes_available = []

        for biome in arboretum.grasslands:
            biomes_available.append(biome)
        if biomes_available == []:
            print("There are no biomes available for this plant. Please annex the proper biome before attempting to cultivate!")
            input("Press enter to continue >> ")
            return
        else:
            for x in range(len(biomes_available)):
                print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]} | ({len(biomes_available[x].plants)}/15)")
        
        biome_choice = int(input("Choose a biome > ")) - 1

        if biome_choice + 1 > len(biomes_available):
            print("Please choose a biome number in the list.")
            input("Press enter to continue >>")
            return

        biomes_available[biome_choice].add_plant(new_plant)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"The {plant} has successfully been cultivated!")
        input("Press enter to continue >>")

    #Cultivate Rainbow Eucalyptus Tree
    if plant == "Rainbow Eucalyptus Tree":
        new_plant = Rainbow_Eucalyptus()
        biomes_available = []

        for biome in arboretum.forests:
            biomes_available.append(biome)
        if biomes_available == []:
            print("There are no biomes available for this plant. Please annex the proper biome before attempting to cultivate!")
            input("Press enter to continue >> ")
            return
        else:
            for x in range(len(biomes_available)):
                print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]} ({len(biomes_available[x].plants)}/32)")
        
        biome_choice = int(input("Choose a biome > ")) - 1

        if biome_choice + 1 > len(biomes_available):
            print("Please choose a biome number in the list.")
            input("Press enter to continue >>")
            return

        biomes_available[biome_choice].add_plant(new_plant)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"The {plant} has successfully been cultivated!")
        input("Press enter to continue >>")
        
    #Cultivate Blue Jade Vine
    if plant == "Blue Jade Vine":
        new_plant = Blue_Jade()
        biomes_available = []

        for biome in arboretum.grasslands:
            biomes_available.append(biome)
        for biome in arboretum.swamps:
            biomes_available.append(biome)

        if biomes_available == []:
            print("There are no biomes available for this plant. Please annex the proper biome before attempting to cultivate!")
            input("Press enter to continue >> ")
            return

        else:
            for x in range(len(biomes_available)):
                if biomes_available[x].name == "Swamp":
                    print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]} ({len(biomes_available[x].plants)}/12)")
                else:
                    print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]} ({len(biomes_available[x].plants)}/15)")
        biome_choice = int(input("Choose a biome > ")) - 1

        if biome_choice + 1 > len(biomes_available):
            print("Please choose a biome number in the list.")
            input("Press enter to continue >>")
            return
            
        biomes_available[biome_choice].add_plant(new_plant)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"The {plant} has successfully been cultivated!")
        input("Press enter to continue >>")
        
    