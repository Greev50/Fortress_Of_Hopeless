from random import randint, choice

class Enemy:
    untouchable = False
    used_untouchable = False

    def __init__(self):
        self.name = 'Sheep'
        self.biome = 'spawn'
        self.hp = 100
        self.damage = 10
        self.ability = 'Нет'
        self.distance = 0
        self.can_walk = True


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
        elif self.ability == 'Шлепок веткой':
            print('Подкашивает игрока и забирает 1 стамину')
            # Шанс использования способности: 40%
        elif self.ability == 'Проклятый клык':
            print('При использовании запрещает использовать игроку уклонение и зелья здоровья на время сражения с ней')
            # Шанс использования способности: 5%
        elif self.ability == 'Анти-Пацифист':
            print('При его убийстве повышается множитель чего то у босса. Либо увеличивается на 10% здоровье, либо на 5% урон, либо на 3% шанс использования способности')
            # Шанс использования способности: 100%
        elif self.ability == 'Неверный поворот':
            print('Чтоб пройти к боссу, надо будет победить на одного каменного стража больше')
            # Шанс использования способности: 3% Использует только 1 раз
        elif self.ability == 'Уклонение':
            print('Мышь уклоняется от удара и отнимает у игрока 10хп')
            # Шанс использования способности: 50%
        elif self.ability == 'Паучьи оковы':
            print('Оковывает руки и ноги игрока, из за чего у него остается только 8 энергии на бой. На весь бой, не раунд.')
            # Шанс использования способности: 20% Использует только 1 раз
        elif self.ability == 'Проклятая колонна':
            print('Ставит на поле колонну, войдя в которую, игрок получает смертельный удар от стража, наносящий 400 урона. Колонна держится 1 раунд')
            # Шанс использования способности: 10% 
        elif self.ability == 'Душевная Боль':
            print('Подойдя к игроку на расстояние 2 клеток, каждые 4 секунды отнимает 10хп') # Делать с помощью time
            # Шанс использования способности: 100% 
        elif self.ability == 'Каменная форма':
            print('Падает в каменную форму и восстанавливает себе жизни в количестве 30% от полученного в данном ходе урона')
            # Шанс использования способности: 15%
        elif self.ability == 'Трехглавый':
            print('Увеличивает свое хп втрое на 1 минуту, увеличивает дистанцию укуса вдвое')
            # Шанс использования способности: 6%    
            
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
            print(f'Хоба на! Видал, как могу? Вот это я акробат! Успешное уклонение даст мне преимущество перед врагом')
            victum.untouchable = False

    def E_walk(self, arena, player, go_to_or_run): # True = go to, False = run

        tostar = arena.E_current_cell-1  
        run_allowed_cells = tuple(set(range(1, arena.cells))-set(player.P_return_distance(arena)))
        go_to_allowed_cells = tuple(set(range(1, arena.cells))-set((tuple(run_allowed_cells), arena.P_current_cell)))

        could_attack = bool(randint(0,1))

        if go_to_or_run == True:
            if could_attack == True:
                while self.can_reach_player(arena) == False:
                    arena.E_current_cell = choice(go_to_allowed_cells)
                    arena.curr_pos[tostar] = '*  '
                    arena.init_pos()
                    tostar = arena.E_current_cell-1 
            else:
                arena.E_current_cell = choice(go_to_allowed_cells)
                arena.curr_pos[tostar] = '*  '
                arena.init_pos()

        else:
            arena.E_current_cell = choice(run_allowed_cells)
            arena.curr_pos[tostar] = '*  '
            arena.init_pos()


    def E_escape(self):
        print(f'{self.name} пытается уклониться!')
        self.used_untouchable = True
        if randint(0,1) == 1:
            self.untouchable = True
       
    def can_reach_player(self, arena):
        if arena.P_current_cell in range(arena.E_current_cell - self.distance, arena.E_current_cell + self.distance+1):
            return True
        return False
    

    def E_return_distance(self, arena):
        # return self.distance
        if arena.E_current_cell + self.distance < arena.cells:
            if arena.E_current_cell - self.distance > 0:
                return tuple(range(arena.E_current_cell - self.distance, arena.E_current_cell + self.distance+1))
            else:
                return tuple(range(1, arena.E_current_cell + self.distance+1))
        else:
            if arena.E_current_cell - self.distance > 0: 
                return tuple(range(arena.E_current_cell - self.distance, arena.cells+1))
            else:
                return tuple(range(1, arena.cells+1))
            
    def E_use_ability(self, arena, player):
        if self.ability == None:
            print(f'{self.name} странно взбрыкивает и трясет головой. Что за черт..?')
            # Пауза
            print('Фух, кажется, пронесло.')
            # Пауза
            print(f'О нет.. {self.name} бежит на меня!')
            while self.can_reach_player != True:
                self.E_walk(arena, player, True)
            self.E_attack(player)
            self.E_attack(player)
        else:
            self.ability_using()


# class Fortress_of_Oblivion_Enemy(Enemy):
#     def __init__(self):
#         super().__init__()
#         self.biome = 'Крепость Забвения'
#         self.ability = 'Дизориентация'

# class Floating_Fortress_enemy(Enemy):
#     def __init__(self):
#         super().__init__()
#         self.biome = 'Парящий замок'
#         self.ability = 'Левитация'

# class Black_Pearl_enemy(Enemy):
#     def __init__(self):
#         super().__init__()
#         self.biome = 'Черная жемчужина'
#         self.ability = 'Морская волна'


class Bloodsucker(Enemy): # Плавает во рву вокруг замка
    def __init__(self):
        super().__init__()
        self.name = 'Пиявка'

        self.biome = 'Подножие замка'
        self.hp = 40
        self.damage = 5
        self.distance = 1
        self.can_walk = True


class Wooden_Sentinel(Enemy): # Охраняет вход в замок. Корнями врос в землю рядом с подъемным мостом
    def __init__(self):
        super().__init__()
        self.name = 'Древесный страж'

        self.biome = 'Подножие замка'
        self.hp = 150
        self.damage = 20
        self.ability = 'Шлепок веткой'
        self.distance = 2
        self.can_walk = False

    def ability_using(self):
        print('Подкашивает игрока и забирает 1 стамину')
            # Шанс использования способности: 40%


class Draugr_Archer(Enemy):
     def __init__(self):
        super().__init__()
        self.name = 'Драугр - лучник'

        self.biome = 'Двор замка' # castle courtyard - название класса биома
        self.hp = 80
        self.damage = 25
        self.distance = 7
        self.can_walk = True

class Cursed_BloodHound(Enemy): # Несколько собак по очереди. range(2,4)
     def __init__(self):
        super().__init__()
        self.name = 'Проклятая Ищейка'

        self.biome = 'Двор замка' # castle courtyard - название класса биома
        self.hp = 40
        self.damage = 10
        self.ability = 'Проклятый клык'
        self.distance = 2
        self.can_walk = True

class Devils_Blessing(Enemy): # Фиолетовый светящийся огонек. 
     'При его появлении пишется сообщение: заблудшая душа, пощади, прошу.. '
     def __init__(self): # Приспешники - пешки дьявола
        super().__init__()
        self.name = 'Благословление дьявола'

        self.biome = 'Двор замка' # castle courtyard - название класса биома
        self.hp = 10
        self.damage = 0
        self.ability = 'Анти-Пацифист'
        self.distance = 10
        self.can_walk = False

class Guardian_Skeleton(Enemy):  
     def __init__(self):
        super().__init__()
        self.name = 'Скелет-Защитник'

        self.biome = 'Темные коридоры' # Darkest Dungeon, маленькая арена по размерам
        self.hp = 300
        self.damage = 30
        self.distance = 3
        self.can_walk = True

class Stone_Sentinel(Enemy):  # Выдвигается стена, преграждая путь, после смерти, если использовал способность, остается на месте, иначе падает. Бьет сплешом. 
     def __init__(self):
        super().__init__()
        self.name = 'Страж - стена'

        self.biome = 'Темные коридоры'
        self.hp = 500
        self.damage = 30
        self.ability = 'Неверный поворот'
        self.distance = 4
        self.can_walk = False

class Devils_Arachn(Enemy):  # Огромный паук со светящимися глазами, полностью черный, а на заде светящийся белый череп, покрытый кровь. жертв
    def __init__(self): # Питомец Дьявола
        super().__init__()
        self.name = 'Дьяволская Арахна'

        self.biome = 'Темные коридоры'
        self.hp = 300
        self.damage = 60
        self.ability = 'Паучьи оковы'
        self.distance = 2
        self.can_walk = True

class Bad_Dead_Bat(Enemy): 
    def __init__(self):
        super().__init__()
        self.name = 'Некро-Мышь'

        self.biome = 'Темные коридоры'
        self.hp = 30
        self.damage = 70
        self.ability = 'Уклонение'
        self.distance = 2
        self.can_walk = True

class Court_Gargoyle(Enemy): 
    def __init__(self):
        super().__init__()
        self.name = 'Придворная Гаргулья'

        self.biome = 'Тронный зал' # Большой по размерам
        self.hp = 700
        self.damage = 50
        self.ability = 'Каменная форма'
        self.distance = 4
        self.can_walk = True

class Cursed_Sentinel(Enemy): 
    def __init__(self):
        super().__init__()
        self.name = 'Проклятый страж'

        self.biome = 'Тронный зал' # Большой по размерам. Босс - Дьявол.
        self.hp = 1000
        self.damage = 100
        self.ability = 'Проклятая колонна'
        self.distance = 5
        self.can_walk = False

class Cloud_Of_Soul_Pain(Enemy): # При появлении по залу разносятся крики убитых
    def __init__(self): # идет по 2 блока каждый ход и дамажит по 1 урона, а если вплотную к игроку, то на 1
        super().__init__()
        self.name = 'Испарения Душевной Боли'

        self.biome = 'Тронный зал' # Большой по размерам. Босс - Дьявол.
        self.hp = 100
        self.damage = 1
        self.ability = 'Душевная Боль'
        self.distance = 1
        self.can_walk = True

class Devils_Demon(Enemy):  
    def __init__(self): # Правая рука Дьявола
        super().__init__()
        self.name = 'Советник Дьявола'

        self.biome = 'Тронный зал' # Большой по размерам. Босс - Дьявол.
        self.hp = 1300
        self.damage = 70
        self.distance = 6
        self.can_walk = True

class Cerberus(Enemy):
    def __init__(self): # Второй питомец Дьявола
        super().__init__()
        self.name = 'Цербер'

        self.biome = 'Тронный зал' # Большой по размерам. Босс - Дьявол.
        self.hp = 2000
        self.damage = 65
        self.ability = 'Трехглавый'
        self.distance = 3
        self.can_walk = True

downstairs = (Bloodsucker, Wooden_Sentinel)
fortress_courtyard = (Draugr_Archer, Cursed_BloodHound, Devils_Blessing)
darkest_dungeon = (Guardian_Skeleton, Stone_Sentinel, Devils_Arachn, Bad_Dead_Bat)
throne_room = (Court_Gargoyle, Cursed_Sentinel, Cloud_Of_Soul_Pain, Devils_Demon, Cerberus)