import os
def build_facility_report(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    for river in arboretum.rivers:
        print(f'\nRiver [{str(river.id)[:8]}]')
        for animal in river.animals:
            print(f'    {animal.species} ({str(animal.id)[:8]})')
        for plant in river.plants:
            print(f'    {plant.species} ({str(plant.id)[:8]})')
    for swamp in arboretum.swamps:
        print(f'\nSwamp [{str(swamp.id)[:8]}]')
        for animal in swamp.animals:
            print(f'    {animal.species} ({str(animal.id)[:8]})')
        for plant in swamp.plants:
            print(f'    {plant.species} ({str(plant.id)[:8]})')
    for grassland in arboretum.grasslands:
        print(f'\nGrassland [{str(grassland.id)[:8]}]')
        for animal in grassland.animals:
            print(f'    {animal.species} ({str(animal.id)[:8]})')
        for plant in grassland.plants:
            print(f'    {plant.species} ({str(plant.id)[:8]})')
    for coastline in arboretum.coastlines:
        print(f'\nCoastline [{str(coastline.id)[:8]}]')
        for animal in coastline.animals:
            print(f'    {animal.species} ({str(animal.id)[:8]})')
        for plant in coastline.plants:
            print(f'    {plant.species} ({str(plant.id)[:8]})')
    for mountain in arboretum.mountains:
        print(f'\nMountain [{str(mountain.id)[:8]}]')
        for animal in mountain.animals:
            print(f'    {animal.species} ({str(animal.id)[:8]})')
        for plant in mountain.plants:
            print(f'    {plant.species} ({str(plant.id)[:8]})')
    for forest in arboretum.forests:
        print(f'\nForest [{str(forest.id)[:8]}]')
        for animal in forest.animals:
            print(f'    {animal.species} ({str(animal.id)[:8]})')
        for plant in forest.plants:
            print(f'    {plant.species} ({str(plant.id)[:8]})')

    input("\n\nPress any key to continue...")