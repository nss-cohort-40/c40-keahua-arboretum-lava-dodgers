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
        print(f'{index + 1}. {biome.name.capitalize()} {str(biome.id)[:8]} {len(biome.animals)} animals')

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