from termcolor import colored

class Arena:
    isfight = False

    def __init__(self, field_len = 10, name = 'Темные коридоры'):
        self.cells = field_len
        self.location_name = name

        self.P_current_cell = 1
        self.E_current_cell = self.cells  
        self.curr_pos = []
        self.curr_pos.extend(['*  ']*(self.cells))

        self.curr_pos[self.P_current_cell-1] = 'P  '
        self.curr_pos[self.E_current_cell-1] = 'E  '

    def init_pos(self):
        self.curr_pos[self.P_current_cell-1] = 'P  '
        self.curr_pos[self.E_current_cell-1] = 'E  '

        
    def show_arena(self,player,enemy): 
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
        

    def start_fight(self, P, E):
        self.isfight = True
        print(f'Черт, кажется меня заметили! {E.name} направляется ко мне..')        
        while self.isfight == True:
            self.show_arena(P,E)
            if P.stamina > 0:
                P.P_fight_mode(E, self)
            else:
                print('Враг атакует')
                P.regen_stamina()
