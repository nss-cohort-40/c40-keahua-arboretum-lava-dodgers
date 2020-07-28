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
        os.system('cls' if os.name == 'nt' else 'clear')
        n = 1
        for food in animal.prey:
            print(f"{n}. {food}")
            n+=1

    def feed_em(animal, prey):
        os.system('cls' if os.name == 'nt' else 'clear')
        n = 1
        for food in prey:
            if int(choice2) == n:
                animal.feed(food)
                choice3 = input("Press enter to return to the main menu...")
            n+=1

    if choice == "1":
        animal = GoldDustDayGecko()
        list_food(animal)
        prey = animal.prey
        choice2 = input(f"What's on the menu for the {animal.species} today? \n> ")
        feed_em(animal, prey)
        
    if choice == "2":
        animal = RiverDolphin()
        list_food(animal)
        prey = animal.prey
        choice2 = input(f"What's on the menu for the {animal.species} today? \n> ")
        feed_em(animal, prey)

    if choice == "3":
        animal = NeneGoose()
        list_food(animal)
        prey = animal.prey
        choice2 = input(f"What's on the menu for the {animal.species} today? \n> ")
        feed_em(animal, prey)

    if choice == "4":
        animal = Kikakapu()
        list_food(animal)
        prey = animal.prey
        choice2 = input(f"What's on the menu for the {animal.species} today? \n> ")
        feed_em(animal, prey)
        
    if choice == "5":
        animal = Pueo()
        list_food(animal)
        prey = animal.prey
        choice2 = input(f"What's on the menu for the {animal.species} today? \n> ")
        feed_em(animal, prey)

    if choice == "6":
        animal = Ulae()
        list_food(animal)
        prey = animal.prey
        choice2 = input(f"What's on the menu for the {animal.species} today? \n> ")
        feed_em(animal, prey)

    if choice == "7":
        animal = Opeapea()
        list_food(animal)
        prey = animal.prey
        choice2 = input(f"What's on the menu for the {animal.species} today? \n> ")
        feed_em(animal, prey)

    if choice == "8":
        animal = HappyFaceSpider()
        list_food(animal)
        prey = animal.prey
        choice2 = input(f"What's on the menu for the {animal.species} today? \n> ")
        feed_em(animal, prey)