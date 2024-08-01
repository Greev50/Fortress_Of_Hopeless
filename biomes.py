from weapons import *
class Biome:
    def __init__(self):
        self.name = ''
        self.enemies = []
        self.type = ''
        self.amount_of_mobs_to_next_stage = 0

class Fortress(Biome):
    def __init__(self):
        self.name = 'Крепость забвения'
        self.enemies = ['*','*','*']
        self.type = melee
        self.amount_of_mobs_to_next_stage = 5
        self.current_stage = 1


    def next_stage(self):
        pass


    