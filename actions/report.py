import os
import copy
def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    show_biomes(arboretum.rivers)
    show_biomes(arboretum.grasslands)
    show_biomes(arboretum.swamps)
    show_biomes(arboretum.forests)
    show_biomes(arboretum.mountains)
    show_biomes(arboretum.coastlines)

    input("\n\nPress any key to continue...")


def show_biomes(biome_array):
    for index, biome in enumerate(biome_array):
        animal_string = get_biome_specifics_animals(biome_array, index)
        plant_string = get_biome_specifics_plants(biome_array, index)
        print(f"\n{biome.name} | [{str(biome.id)[:8]}]{animal_string}{plant_string}")
        for animal in biome.animals:
            print(f'    {animal.species} ({str(animal.id)[:8]})')
        for plant in biome.plants:
            print(f'    {plant.species} ({str(plant.id)[:8]})')

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