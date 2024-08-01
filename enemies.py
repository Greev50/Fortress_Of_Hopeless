class Enemy:
    def __init__(self):
        self.name = ''
        self.biome = ''
        self.hp = 100
        self.damage = 10
        self.ability = None

    # def __isub__(self, P_damage): # enemy-=damage
    #     self.hp -= P_damage 
    #     return self

class Fortress_of_Oblivion_Enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.biome = 'Крепость Забвения'
        self.ability = 'Дизориентация'

    def disorientation(self):
        name = 'Дизориентация'
        print('Отнимает 2 единицы энергии')
    
ff = Fortress_of_Oblivion_Enemy()

ff.disorientation()