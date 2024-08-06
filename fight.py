from termcolor import colored
from random import choice
from weapons import *
from biomes import *

class Arena:
    isfight = False

    def __init__(self, Biome):
        self.biome = Biome
        self.cells = self.biome.arena_size
        self.location_name = self.biome.name

        self.P_current_cell = 1
        self.E_current_cell = self.cells  
        self.curr_pos = []
        self.curr_pos.extend(['*  ']*(self.cells))

        self.curr_pos[self.P_current_cell-1] = 'P  '
        self.curr_pos[self.E_current_cell-1] = 'E  '

    def init_pos(self):
        self.curr_pos[self.P_current_cell-1] = 'P  '
        self.curr_pos[self.E_current_cell-1] = 'E  '

        
    def show_arena(self,player, enemy): 
        P_Stamina = [0,0,
                     0,0,
                     0,0,
                     0,0,
                     0,0]
        
        for i in range(player.stamina):
            P_Stamina[i] = '*'      

        if self.cells > 14:
            print('==='*self.cells + f'  |{P_Stamina[0]}  {P_Stamina[1]}|  Информация:')
            l = len(f'{player.hp} HP'+' '*(self.cells-len(str(player.hp)+' HP')) + f'== {self.location_name} ==')
            print(f'{player.hp} HP'+' '*(self.cells-len(str(player.hp)+' HP')-1) + f'== {self.location_name} =='+ ' '*(self.cells*3-(l+len(str(enemy.hp)+' HP'))+1) + f'{enemy.hp} HP' + f'  |{P_Stamina[2]}  {P_Stamina[3]}|  \n' + ' '*(self.cells*3) + f'  |{P_Stamina[4]}  {P_Stamina[5]}|  Противник: {enemy.name}\n'+''.join(self.curr_pos)+f'  |{P_Stamina[6]}  {P_Stamina[7]}|  Радиус атаки противника: {enemy.distance}')# 
        else:
            print('==='*self.cells + f'  |{P_Stamina[0]}  {P_Stamina[1]}|  ЛОКАЦИЯ: {self.location_name}')
            l = len(f'{player.hp} HP'+' '*(self.cells-len(str(player.hp)+' HP')))
            print(f'{player.hp} HP'+' '*(self.cells-len(str(player.hp)+' HP'))+ ' '*(self.cells*3-(l+len(str(enemy.hp)+' HP'))) + f'{enemy.hp} HP' + f'  |{P_Stamina[2]}  {P_Stamina[3]}|\n' + ' '*(self.cells*3) + f'  |{P_Stamina[4]}  {P_Stamina[5]}|  Противник: {enemy.name}\n'+''.join(self.curr_pos)+f'  |{P_Stamina[6]}  {P_Stamina[7]}|  Радиус атаки противника: {enemy.distance}')# 


        colors = {'P' : 'light_cyan',
                  'E' : 'light_magenta',
                  'can' : 'light_green',
                  'E_can' : 'light_red'}
        
        can_attack_enemy = False
        
        color_interface = ['== ']*self.cells

        for index in player.P_return_distance(self):
            if index == self.E_current_cell:
                can_attack_enemy = True
                
            color_interface[index-1] = colored('== ', colors['can'])
       
        color_interface[self.P_current_cell-1] = colored('== ', colors['P'])

        if can_attack_enemy == False:
            color_interface[self.E_current_cell-1] = colored('== ', colors['E']) 
        else:
            color_interface[self.E_current_cell-1] = colored('== ', colors['E_can'], attrs=['bold'])

        [print(x, end = '') for x in color_interface]
        print(f'  |{P_Stamina[8]}  {P_Stamina[9]}|  Способность: {enemy.ability}')

    def Drop_Choice(self, player):
        drop_items = ('money', 'weapon', 'heal_potion')
        interacted = False

        if self.biome.max_rarity == 'common':
            pluscoins = randint(1, 25)
            player.balance += pluscoins
            self.interacted = True
            print(f'{pluscoins} монет. Неплохо')


        elif self.biome.max_rarity == 'rare':
            choice_of_drop = choice(drop_items[:2])
            while interacted == False:
                if choice_of_drop == 'money':
                    pluscoins = randint(25, 40)
                    player.balance += pluscoins
                    self.interacted = True
                    print(f'{pluscoins} монет. Неплохо')
                elif choice_of_drop == 'weapon':
                    data = Random_Drop(self.location_name.max_rarity, self.biome.type)
                    ans = str(input('Что же мне с ним сделать?'))
                    if ans.lower() in ('забрать', 'взять', 'оставить себе', 'заберу', 'возьму', 'оставлю себе', 'подобрать', 'подберу', 'подобрать оружие', 'подберу оружие', 'хочу', 'получу', 'получить'):
                        player.add_weapon(data)
                        self.interacted = True
                    elif ans.lower() in ('выбросить', 'оставить', 'выкинуть', 'не брать', 'выброшу', 'оставлю', 'выкину', 'не возьму', 'не беру'):
                        print('Пока пока, оружие!')
                        self.interacted = True
                    else:
                        print('Сомневаюсь, что смогу это сделать. Может что то другое?')


        elif self.biome.max_rarity == 'epic':
            choice_of_drop = choice(drop_items[:3])
            while interacted == False:
                if choice_of_drop == 'money':
                    pluscoins = randint(40, 80)
                    player.balance += pluscoins
                    self.interacted = True
                    print(f'{pluscoins} монет. Неплохо')
                elif choice_of_drop == 'weapon':
                    data = Random_Drop(self.location_name.max_rarity, self.biome.type)
                    ans = str(input('Что же мне с ним сделать?'))
                    if ans.lower() in ('забрать', 'взять', 'оставить себе', 'заберу', 'возьму', 'оставлю себе', 'подобрать', 'подберу', 'подобрать оружие', 'подберу оружие', 'хочу', 'получу', 'получить'):
                        player.add_weapon(data)
                        self.interacted = True
                    elif ans.lower() in ('выбросить', 'оставить', 'выкинуть', 'не брать', 'выброшу', 'оставлю', 'выкину', 'не возьму', 'не беру'):
                        print('Пока пока, оружие!')
                        self.interacted = True
                    else:
                        print('Сомневаюсь, что смогу это сделать. Может что то другое?')
                elif choice_of_drop == 'heal_potion':
                    player.heal += 1
                    print('Зелье восстановления! Отлично')
        
        elif self.biome.max_rarity == 'legendary':
            choice_of_drop = choice(drop_items[:3])
            while interacted == False:
                if choice_of_drop == 'money':
                    pluscoins = randint(80, 140)
                    player.balance += pluscoins
                    self.interacted = True
                    print(f'{pluscoins} монет. Неплохо')
                elif choice_of_drop == 'weapon':
                    data = Random_Drop(self.location_name.max_rarity, self.biome.type)
                    ans = str(input('Что же мне с ним сделать?'))
                    if ans.lower() in ('забрать', 'взять', 'оставить себе', 'заберу', 'возьму', 'оставлю себе', 'подобрать', 'подберу', 'подобрать оружие', 'подберу оружие', 'хочу', 'получу', 'получить'):
                        player.add_weapon(data)
                        self.interacted = True
                    elif ans.lower() in ('выбросить', 'оставить', 'выкинуть', 'не брать', 'выброшу', 'оставлю', 'выкину', 'не возьму', 'не беру'):
                        print('Пока пока, оружие!')
                        self.interacted = True
                    else:
                        print('Сомневаюсь, что смогу это сделать. Может что то другое?')
                elif choice_of_drop == 'heal_potion':
                    player.heal += 2
                    print('2 зелья восстановления! Ну вообще шедевр!')       

    def start_fight(self, P):
        self.isfight = True

        E = choice(self.biome.enemies)()

        print(f'Черт, кажется меня заметили! {E.name} направляется ко мне..') 

        while self.isfight == True:
            self.show_arena(P, E)
            if E.hp > 0:
                if P.stamina > 0:
                    P.P_fight_mode(E, self)
                else:
                    print('Фух..')
                    # Пауза
                    E.E_attack(P)


                    P.regen_stamina()
            else:
                P.regen_stamina()
                self.isfight = False
                print(choice(('Это было тяжко..', f'Да уж, {E.name} - серьезный противник! В следующий раз надо быть с ним осторожнее', f'Кажется, мне надо отдохнуть.. \n{E.name} повержен!')))
                # Пауза
                print('Посмотрим, что выпало с этого чудища')
                # Задержка
                self.Drop_Choice(P)
                