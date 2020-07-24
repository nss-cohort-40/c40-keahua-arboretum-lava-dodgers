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
        list_food(GoldDustDayGecko)
    if choice == "2":
        list_food(RiverDolphin)
    if choice == "3":
        list_food(NeneGoose)
    if choice == "4":
        list_food(Kikakapu)
    if choice == "5":
        list_food(Pueo)
    if choice == "6":
        list_food(Ulae)
    if choice == "7":
        list_food(Opeapea)
    if choice == "8":
        list_food(HappyFaceSpider)
