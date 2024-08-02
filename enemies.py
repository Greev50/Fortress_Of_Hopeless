from random import randint, choice

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

    def E_walk(self, arena, player, direction):
        True_cord = None

        tostar = arena.E_current_cell-1
        
        
         

        if direction == True: # Вправо
            steps_num_True = (choice(range(arena.E_current_cell+1, arena.cells+1)) - arena.E_current_cell)
            while True_cord != True:                   
                if arena.E_current_cell + steps_num_True < arena.cells+1:
                    if arena.E_current_cell + steps_num_True != arena.P_current_cell:
                        arena.E_current_cell += steps_num_True
                        arena.curr_pos[tostar] = '*  '
                        print(arena.curr_pos)
                        arena.init_pos()
                        arena.show_arena()
                        True_cord = True
                    else:
                        True_cord = False
                        steps_num_False -= 1
                else:
                    True_cord = False
                    steps_num_True -= 1
        else:           
            steps_num_False = arena.E_current_cell - choice(range(1, arena.E_current_cell+1))
            while True_cord != True:                   
                if arena.E_current_cell - steps_num_False > 0:
                    if arena.E_current_cell - steps_num_False != arena.P_current_cell:
                        arena.E_current_cell -= steps_num_False
                        arena.curr_pos[tostar] = '*  '
                        arena.init_pos()
                        arena.show_arena()
                        True_cord = True
                    else:
                        True_cord = False
                        steps_num_False += 1
                else:
                    True_cord = False
                    steps_num_False += 1
                    print('2', steps_num_False)
    

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


