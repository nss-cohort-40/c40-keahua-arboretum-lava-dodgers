import os
from places import *

def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Mountain")
    print("6. Forest")

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River("River")
        arboretum.rivers.append(river)
    if choice == "2":
        swamp = Swamp("Swamp")
        arboretum.swamps.append(swamp)
    if choice == "3":
        coastline = Coastline("Coastline")
        arboretum.coastlines.append(coastline)
    if choice == "4":
        grassland = Grassland("Grassland")
        arboretum.grasslands.append(grassland)
    if choice == "5":
        mountain = Mountain("Mountain")
        arboretum.mountains.append(mountain)
    if choice == "6":
        forest = Forest("Forest")
        arboretum.forests.append(forest)
