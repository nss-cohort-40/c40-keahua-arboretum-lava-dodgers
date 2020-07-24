from animals import *
import os

def feed_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal > ")

    def list_food(animal):
        print(animal)
        n = 1
        for food in animal.prey:
            print(f"{n}. {food}")
            n+=1

    if choice == "1":
        animal = GoldDustDayGecko()
        list_food(animal)
    if choice == "2":
        animal = RiverDolphin()
        list_food(animal)
    if choice == "3":
        animal = NeneGoose()
        list_food(animal)
    if choice == "4":
        animal = Kikakapu()
        list_food(animal)
    if choice == "5":
        animal = Pueo()
        list_food(animal)
    if choice == "6":
        animal = Ulae()
        list_food(animal)
    if choice == "7":
        animal = Opeapea()
        list_food(animal)
    if choice == "8":
        animal = HappyFaceSpider()
        list_food(animal)
