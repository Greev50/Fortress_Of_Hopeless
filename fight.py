class Arena:
    isfight = False

    def __init__(self, field_len = 10, name = 'spawn'):
        self.cells = field_len
        self.location_name = name

        self.P_current_cell = 1 #!
        self.E_current_cell = self.cells #1
        self.curr_pos = []
        self.curr_pos.extend(['*  ']*(self.cells))

        self.curr_pos[self.P_current_cell-1] = 'P  '
        self.curr_pos[self.E_current_cell-1] = 'E  '

    def init_pos(self):
        self.curr_pos[self.P_current_cell-1] = 'P  '
        self.curr_pos[self.E_current_cell-1] = 'E  '

        
    def show_arena(self):

        print('==='*self.cells)
        print(' '*(self.cells) + f'== {self.location_name} ==\n\n'+''.join(self.curr_pos))
        print('== '*self.cells) 

    def start_fight(self, P, E, Arena):
        self.isfight = True
        print(f'Черт, кажется меня заметили! {E.name} направляется ко мне..')        
        while self.isfight == True:
            self.show_arena()
            P.P_fight_mode(E, Arena)
            

