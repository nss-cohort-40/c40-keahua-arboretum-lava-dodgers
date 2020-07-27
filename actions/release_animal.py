import copy
from animals import *

def choose_biome(animal, arboretum):
    biomes = []

    biomes.extend(arboretum.rivers)
    biomes.extend(arboretum.swamps)
    biomes.extend(arboretum.coastlines)
    biomes.extend(arboretum.grasslands)
    biomes.extend(arboretum.mountains)
    biomes.extend(arboretum.forests)

    for index, biome in enumerate(biomes):
        animals_string = get_biome_specifics_animals(biomes, index)
        plants_string = get_biome_specifics_plants(biomes, index)
        print(f'{index + 1}. {biome.name.capitalize()}{animals_string}{plants_string} | {str(biome.id)[:8]} | {len(biome.animals)} animals')

    print(f"Release {animal.species.lower()} into which biome?")
    choice = input(">")

    try:
        biomes[int(choice) - 1].add_animal(animal)
    except IndexError:
        print("****       That number is not listed       ****")
        print("****   Please choose an available option   ****")
        choose_biome(animal, arboretum)

def release_animal(arboretum):

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

    try:
        if choice == "1":
            animal = GoldDustDayGecko()

        if choice == "2":
            animal = RiverDolphin()

        if choice == "3":
            animal = NeneGoose()

        if choice == "4":
            animal = Kikakapu()

        if choice == "5":
            animal = Ulae()

        if choice == "6":
            animal = Opeapea()

        if choice == "8":
            animal = HappyFaceSpider()

        choose_biome(animal, arboretum)

    except AttributeError:
        print("****       That number is not listed       ****")
        print("****   Please choose an available option   ****")
        release_animal(arboretum)


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