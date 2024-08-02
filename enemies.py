from random import randint
class Enemy:
    untouchable = False
    used_untouchable = False

    def __init__(self):
        self.name = 'Sheep'
        self.biome = 'spawn'
        self.hp = 100
        self.damage = 10
        self.ability = None

    def use_ability(self):
        if self.ability == 'Дизориентация':
            print('Отнимает 3 единицы энергии')
            # Шанс использования способности: 40%
        elif self.ability == 'Левитация':
            print('Поднимает персонажа в воздух и не дает использовать способность 1 ход, при этом моб ходит еще 1 раз')
            # Шанс использования способности: 25%
        elif self.ability == 'Морская волна':
            print('Крадет у персонажа 1 зелье хила до того момента, пока не будет мертво. Так же наносит 2ед. урона.')
            # Шанс использования способности: 8%
        else:
            print('Такой способности пока что нет')

    def E_attack(self, victum):
        if victum.untouchable == False:
            if victum.used_untouchable == False:
                print(f'Вы получили {self.damage} урона!')
                victum.hp -= self.damage
            elif victum.used_untouchable == True:
                print(f'Вы неудачно уклонились и получили {self.damage} урона!')
                victum.hp -= self.damage
        else:
            print(f'Вы уклонились от удара монстра!')
            victum.untouchable = False

    # def E_walk(self, arena):
    #     arena.E_current_cell
        

        

    def E_escape(self):
        print(f'{self.name} пытается уклониться!')
        self.used_untouchable = True
        if randint(0,1) == 1:
            self.untouchable = True
        
        

        


class Fortress_of_Oblivion_Enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.biome = 'Крепость Забвения'
        self.ability = 'Дизориентация'

class Floating_Fortress_enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.biome = 'Парящий замок'
        self.ability = 'Левитация'

class Black_Pearl_enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.biome = 'Черная жемчужина'
        self.ability = 'Морская волна'


    
ff = Black_Pearl_enemy()


