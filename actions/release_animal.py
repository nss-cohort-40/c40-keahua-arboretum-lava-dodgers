import os
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


def choose_biome(animal, arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    biomes = []

    if animal.species == "Gold Dust Day Gecko":

        biomes.extend(arboretum.forests)

        release_animal(biomes, animal, arboretum)

    elif animal.species == "River Dolphin":

        biomes.extend(arboretum.rivers)

        release_animal(biomes, animal, arboretum)

    elif animal.species == "Nene Goose":

        biomes.extend(arboretum.grasslands)

        release_animal(biomes, animal, arboretum)

    elif animal.species == "Kīkākapu":

        biomes.extend(arboretum.swamps)
        biomes.extend(arboretum.rivers)

        release_animal(biomes, animal, arboretum)

    elif animal.species == "Pueo":

        biomes.extend(arboretum.grasslands)
        biomes.extend(arboretum.forests)

        release_animal(biomes, animal, arboretum)

    elif animal.species == "'Ulae":

        biomes.extend(arboretum.coastlines)

        release_animal(biomes, animal, arboretum)

    elif animal.species == "Ope'ape'a":

        biomes.extend(arboretum.forests)
        biomes.extend(arboretum.mountains)

        release_animal(biomes, animal, arboretum)

    elif animal.species == "Happy-Face Spider":

        biomes.extend(arboretum.swamps)

        release_animal(biomes, animal, arboretum)

def release_animal(biomes, animal, arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(biomes) > 0:
            try:
                for index, biome in enumerate(biomes):
                    print(f'{index + 1}. {biome.name.capitalize()} | {str(biome.id)[:8]} | {len(biome.animals)} animals')

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