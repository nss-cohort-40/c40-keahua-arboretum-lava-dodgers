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
        river = River("river")
        arboretum.rivers.append(river)
    if choice == "2":
        swamp = Swamp("swamp")
        arboretum.swamps.append(swamp)
    if choice == "3":
        coastline = Coastline("coastline")
        arboretum.coastlines.append(coastline)
    if choice == "4":
        grassland = Grassland("grassland")
        arboretum.grasslands.append(grassland)
    if choice == "5":
        mountain = Mountain("mountain")
        arboretum.mountains.append(mountain)
    if choice == "6":
        forest = Forest("forest")
        arboretum.forests.append(forest)
