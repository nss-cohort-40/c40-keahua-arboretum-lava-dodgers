import os
from animals import *

def choose_biome(animal, arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    biomes = []

    biomes.extend(arboretum.rivers)
    biomes.extend(arboretum.swamps)
    biomes.extend(arboretum.coastlines)
    biomes.extend(arboretum.grasslands)
    biomes.extend(arboretum.mountains)
    biomes.extend(arboretum.forests)

    for index, biome in enumerate(biomes):
        print(f'{index + 1}. {biome.name.capitalize()} {str(biome.id)[:8]} {len(biome.animals)} animals')

    print(f"Release {animal.species.lower()} into which biome?")
    choice = input(">")

    try:
        biomes[int(choice) - 1].add_animal(animal)
    except AttributeError:
        print("****       That number is not listed       ****")
        print("****   Please choose an available option   ****")
        input("Press any key to continue >>")
        choose_biome(animal, arboretum)
    except ValueError:
        input("Press any key to continue >>")

def release_animal(arboretum):
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

    if choice == "2":
        animal = RiverDolphin()

    if choice == "3":
        animal = NeneGoose()

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        animal = Pueo()

    if choice == "6":
        animal = Ulae()

    if choice == "7":
        animal == Opeapea()

    if choice == "8":
        animal = HappyFaceSpider()

    try:
        choose_biome(animal, arboretum)
    except AttributeError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("****            No biome chosen            ****")
        print("****   Please choose an available option   ****")
        input("Press any key to continue >>")
        release_animal(arboretum)