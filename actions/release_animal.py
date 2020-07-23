from animals import *

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

    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {str(river.id)[:8]} {len(river.animals)} animals')

    for index, swamp in enumerate(arboretum.swamps):
        print(f'{index + 2}. Swamp {str(swamp.id)[:8]} {len(swamp.animals)} animals')

    for index, coastline in enumerate(arboretum.coastlines):
        print(f'{index + 3}. Coastline {str(coastline.id)[:8]} {len(coastline.animals)} animals')

    for index, grassland in enumerate(arboretum.grasslands):
        print(f'{index + 4}. Grassland {str(grassland.id)[:8]} {len(grassland.animals)} animals')

    for index, mountain in enumerate(arboretum.mountains):
        print(f'{index + 5}. Mountain {str(mountain.id)[:8]} {len(mountain.animals)} animals')
        
    for index, forest in enumerate(arboretum.forests):
        print(f'{index + 6}. Forest {str(forest.id)[:8]} {len(forest.animals)} animals')

    print(f"Release {animal.species.lower()} into which biome?")
    choice = input(">")
    
    arboretum.rivers[int(choice) - 1].animals.append(animal)


