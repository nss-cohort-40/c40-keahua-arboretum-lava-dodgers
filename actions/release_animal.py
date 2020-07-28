import os
import copy
from animals import *

def choose_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    animal = None

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    
    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = GoldDustDayGecko()
        choose_biome(animal, arboretum)

    elif choice == "2":
        animal = RiverDolphin()
        choose_biome(animal, arboretum)

    elif choice == "3":
        animal = NeneGoose()
        choose_biome(animal, arboretum)

    elif choice == "4":
        animal = Kikakapu()
        choose_biome(animal, arboretum)

    elif choice == "5":
        animal = Pueo()
        choose_biome(animal, arboretum)

    elif choice == "6":
        animal = Ulae()
        choose_biome(animal, arboretum)

    elif choice == "7":
        animal = Opeapea()
        choose_biome(animal, arboretum)

    elif choice == "8":
        animal = HappyFaceSpider()
        choose_biome(animal, arboretum)



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

def choose_biome(animal, arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    biomes = []

    if animal.species == "Gold Dust Day Gecko":
        for biome in arboretum.forests:
            if len(biome.animals) < 20:
                biomes.append(biome)

        release_animal(biomes, animal, arboretum)

    elif animal.species == "River Dolphin":
        for biome in arboretum.rivers:
            if len(biome.animals) < 12:
                biomes.append(biome)
        release_animal(biomes, animal, arboretum)

    elif animal.species == "Nene Goose":
        for biome in arboretum.grasslands:
            if len(biome.animals) < 22:
                biomes.append(biome)
        release_animal(biomes, animal, arboretum)

    elif animal.species == "Kīkākapu":
        for biome in arboretum.swamps:
            if len(biome.animals) < 8:
                biomes.append(biome)
        for biome in arboretum.rivers:
            if len(biome.animals) < 12:
                biomes.append(biome)
        release_animal(biomes, animal, arboretum)

    elif animal.species == "Pueo":
        for biome in arboretum.grasslands:
            if len(biome.animals) < 22:
                biomes.append(biome)
        for biome in arboretum.forests:
            if len(biome.animals) < 20:
                biomes.append(biome)
        release_animal(biomes, animal, arboretum)

    elif animal.species == "'Ulae":
        for biome in arboretum.coastlines:
            if len(biome.animals) < 15:
                biomes.append(biome)
        release_animal(biomes, animal, arboretum)

    elif animal.species == "Ope'ape'a":
        for biome in arboretum.forests:
            if len(biome.animals) < 22:
                biomes.append(biome)
        for biome in arboretum.mountains:
            if len(biome.animals) < 6:
                biomes.append(biome)
        release_animal(biomes, animal, arboretum)

    elif animal.species == "Happy-Face Spider":
        for biome in arboretum.swamps:
            if len(biome.animals) < 8:
                biomes.append(biome)
        release_animal(biomes, animal, arboretum)

def release_animal(biomes, animal, arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(biomes) > 0:
            try:
                for index, biome in enumerate(biomes):
                    animal_string = get_biome_specifics_animals(biomes, index)
                    plant_string = get_biome_specifics_plants(biomes, index)
                    
                    if biome.name == "Coastline":
                        print(f'{index + 1}. {biome.name.capitalize()} | {str(biome.id)[:8]}{animal_string}{plant_string} | {len(biome.animals)} / 15')
                    
                    elif biome.name == "Forest":
                        print(f'{index + 1}. {biome.name.capitalize()} | {str(biome.id)[:8]}{animal_string}{plant_string} | {len(biome.animals)} / 20')
                    
                    elif biome.name == "Grassland":
                        print(f'{index + 1}. {biome.name.capitalize()} | {str(biome.id)[:8]}{animal_string}{plant_string} | {len(biome.animals)} / 22')

                print(f"Release {animal.species.lower()} into which biome?")

                choice = input(">")

                if int(choice) > 0:
                    biomes[int(choice) - 1].add_animal(animal)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Animal successfully released!")
                    input("Press any key to continue >>")
                else:
                    raise ValueError

            except IndexError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("****          Choice unavailable           ****")
                print("****    Please choose available option     ****")
                input("Press any key to continue >>")
                choose_biome(animal, arboretum)

            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("****          Choice unavailable           ****")
                print("****    Please choose available option     ****")
                input("Press any key to continue >>")
                choose_biome(animal, arboretum)
    else:
            print("******   No eligible biomes available   ******")
            print("****     Please annex eligible biome      ****")
            input('Press any key to continue >>')
