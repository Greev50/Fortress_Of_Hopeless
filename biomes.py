from weapons import *
from enemies import *

class Biome:
    def __init__(self):
        self.name = None
        self.enemies = []
        self.arena_size = None
        self.type = None
        self.max_rarity = None
        self.is_bestiary_full = None
        self.can_spawn_boss = False

    def choose_enemy(self):
        return self.choice(self.enemies)
        

class Downstairs(Biome): # Крепость заблудших
    def __init__(self):
        self.name = 'Подножие замка'
        self.enemies = downstairs
        self.arena_size = 20
        self.type = melee
        self.max_rarity = 'common'
        self.is_bestiary_full = False

class Fortress_Courtyard(Biome): 
    def __init__(self):
        self.name = 'Двор Замка'
        self.enemies = fortress_courtyard
        self.arena_size = 14
        self.type = melee
        self.max_rarity = 'rare'
        self.is_bestiary_full = False

class Darkest_Dungeon(Biome):
    def __init__(self):
        self.name = 'Темные Коридоры'
        self.enemies = darkest_dungeon
        self.arena_size = 6
        self.type = melee
        self.rarity = 'epic'
        self.is_bestiary_full = False  

class Throne_Room(Biome):
    def __init__(self):
        self.name = 'Тронный Зал'
        self.enemies = downstairs
        self.arena_size = 16
        self.type = melee
        self.rarity = 'legendary'
        self.is_bestiary_full = False  
        self.can_spawn_boss = False # Переделывается на True после заполнения бестиария