import os
import copy
from plants import *

def choose_plant():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")
    print("")
    try:
        plant = int(input("Choose plant to cultivate >> "))
    
    except ValueError:
        print("The input must be a number from the list.")
        input("Press enter to continue >>")
        return
    
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
                animals_in_biome_string = get_biome_specifics_animals(biomes_available, x)
                plants_in_biome_string = get_biome_specifics_plants(biomes_available, x)
                print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]}{plants_in_biome_string}{animals_in_biome_string} | ({len(biomes_available[x].plants)}/4)")
        
        
        try:
            biome_choice = int(input("Choose a biome > ")) - 1

        except ValueError:
            print("The input must be a number.")
            input("Press enter to continue >>")
            return
        

        try:
            if biome_choice >= 0:
                biomes_available[biome_choice].add_plant(new_plant)       
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"The {plant} has successfully been cultivated!")
                input("Press enter to continue >>")
            else:
                raise IndexError

        except IndexError:
            print("The number must be in the list.")
            input("Press enter to continue >>")
            return

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
                animals_in_biome_string = get_biome_specifics_animals(biomes_available, x)
                plants_in_biome_string = get_biome_specifics_plants(biomes_available, x)
                print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]}{plants_in_biome_string}{animals_in_biome_string} | ({len(biomes_available[x].plants)}/15)")
        

        try:
            biome_choice = int(input("Choose a biome > "))- 1

        except ValueError:
            print("The input must be a number.")
            input("Press enter to continue >>")
            return

        try:
            if biome_choice >= 0:
                biomes_available[biome_choice].add_plant(new_plant)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"The {plant} has successfully been cultivated!")
                input("Press enter to continue >>")
            else:
                raise IndexError

        except IndexError:
            print("The number must be in the list.")
            input("Press enter to continue >>")
            return


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
                animals_in_biome_string = get_biome_specifics_animals(biomes_available, x)
                plants_in_biome_string = get_biome_specifics_plants(biomes_available, x)
                print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]}{plants_in_biome_string}{animals_in_biome_string} | ({len(biomes_available[x].plants)}/32)")
        
        try:
            biome_choice = int(input("Choose a biome > "))- 1

        except ValueError:
            print("The input must be a number.")
            input("Press enter to continue >>")
            return
        
        try:
            if biome_choice >= 0:
                biomes_available[biome_choice ].add_plant(new_plant)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"The {plant} has successfully been cultivated!")
                input("Press enter to continue >>")
            else:
                raise IndexError
        except IndexError:
            print("The number must be in the list.")
            input("Press enter to continue >>")
            return
        
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
                plants_in_biome_string = get_biome_specifics_plants(biomes_available, x)
                animals_in_biome_string = get_biome_specifics_animals(biomes_available, x)
                if biomes_available[x].name == "Swamp":
                    print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]}{plants_in_biome_string}{animals_in_biome_string} | ({len(biomes_available[x].plants)}/12)")
                else:
                    print(f"{x+1}. {biomes_available[x]} | {str(biomes_available[x].id)[:8]}{plants_in_biome_string}{animals_in_biome_string} | ({len(biomes_available[x].plants)}/15)")

        try:
            biome_choice = int(input("Choose a biome > ")) - 1
        except ValueError:
            print("The input must be a number.")
            input("Press enter to continue >>")
            return
        try:
            if biome_choice >= 0:
                biomes_available[biome_choice].add_plant(new_plant)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"The {plant} has successfully been cultivated!")
                input("Press enter to continue >>")
            else:
                raise IndexError
        except IndexError:
            print("The number must be in the list.")
            input("Press enter to continue >>")
            return

    
def get_biome_specifics_plants(biomes_available, x):
    plants_in_biome = []
    for plant in biomes_available[x].plants:
        test_plants_in_biome = copy.deepcopy(plants_in_biome)
        for item in plants_in_biome:
            if item[0] == plant.species:
                item.append(plant.species)
        if test_plants_in_biome == plants_in_biome:
            plants_in_biome.append([plant.species])
    plants_in_biome_string = ""
    for plant_list in plants_in_biome:
        if plants_in_biome_string == "":
            plants_in_biome_string = f" | ({len(plant_list)} {plant_list[0]}"
        else:
            plants_in_biome_string = plants_in_biome_string + f", {len(plant_list)} {plant_list[0]}"
    if plants_in_biome_string != "":
        plants_in_biome_string = plants_in_biome_string + ")"
    return plants_in_biome_string


def get_biome_specifics_animals(biomes_available, x):
    plants_in_biome = []
    for plant in biomes_available[x].animals:
        test_plants_in_biome = copy.deepcopy(plants_in_biome)
        for item in plants_in_biome:
            if item[0] == plant.species:
                item.append(plant.species)
        if test_plants_in_biome == plants_in_biome:
            plants_in_biome.append([plant.species])
    plants_in_biome_string = ""
    for plant_list in plants_in_biome:
        if plants_in_biome_string == "":
            plants_in_biome_string = f" | ({len(plant_list)} {plant_list[0]}"
        else:
            plants_in_biome_string = plants_in_biome_string + f", {len(plant_list)} {plant_list[0]}"
    if plants_in_biome_string != "":
        plants_in_biome_string = plants_in_biome_string + ")"
    return plants_in_biome_string
