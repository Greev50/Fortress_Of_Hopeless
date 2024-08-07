from World_Map import *
from enemies import *


class Bestiary:
    def __init__(self):
        self.Dp_Of_Enemies = {'Пиявка': [False, False],
                              'Древесный страж' : [False, False]}
    
    def open_location(self, location_first, location_last):
        biomes[location_first[location_last]] = True
        print(f'Открыта новая локация: {location_last}')

    def discover_enemy(self, name):
        self.Dp_Of_Enemies[name][0] = True

    def discover_enemy_ability(self, name):
        self.Dp_Of_Enemies[name][1] = True

    def display_enemy_info(self, name):
        obj = [x for x in data_all_enemies if x().name == name]
        obj = obj[0]()

        print('===========================')
        print(f'Название: {obj.name}')
        print(f'Краткое описание: {obj.info}')

    def xx(self):
        print('хуй')

b = Bestiary()
