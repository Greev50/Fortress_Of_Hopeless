from random import randint
class Character:
    untouchable = False
    used_untouchable = False
    'Ex: player1 = Character(100, 10, 3, None, [starter_sword])'

    def __init__(self, hp = 100, stamina = 10, heal = 3, class_bonus = None, inv = []):
        self.hp = hp
        self.stamina = stamina
        self.heal = heal
        self.emptyslots = 5 - len(inv)
        self.inv = inv # inv = {curr_weapon, slot_1, slot_2, slot_3}
        self.class_bonus = class_bonus


    def display_inventory(self):
        print('=============================================================')
        print('\t\t\tИнвентарь  | (1,2,3) - Осмотеть слот')
        print(f'Здоровье: {self.hp}\t\t\t   |  4 - Выйти из инвентаря\nВыносливость: {self.stamina}\t\t   -------------------------')
        print('\t\t\t=========')
        print(f'Текущее оружие: {self.inv[0].return_inv()}\nЗелья здоровья: {self.heal}')
        print(f'Рюкзак: {', '.join([x.return_inv() for x in self.inv[1:]])}')
        print('=============================================================')


    def add_weapon(self, weapon):
        if self.emptyslots > 0:
            self.inv.append(weapon)
            print('Фух, еле влезло') or print('Отлично!') or print('Хаха, вот это мощь!')
        else:
            print('Не влезает в рюкзак..')

    def del_weapon(self, index):
        del self.inv[index]

    def inv_interface(self, ans):
        if ans in (1,2,3):
            self.inv[1+ans].display_info()
            ans1 = int(input('\nЧто сделать с оружием? \n1 - Оно прекрасно, оставлю!\n2 - Выкинуть\n'))
            if ans1 == 2:
                # print(self.inv)
                print(f'{self.inv[1+ans].return_inv()} Выброшен')
                self.del_weapon(1+ans)
            else:
                return
        elif ans == 4:
            return
        else:
            print('Такого варианта нет')
    
    def P_use_heal(self, amount_of_heal):
        if amount_of_heal > 0:
            self.hp += 50
            self.heal -= 1
            print(f'Зелье лечения восстановило 50 здоровья.\nСейчас у вас {self.hp} здоровья!')
        else:
            print('Ах.. Ни одного не осталось..')
    
    def P_attack(self, enemy):
        # Надо делать print()
        dmg = self.inv[0].total_damage()
        if enemy.untouchable == False:
            if enemy.used_untouchable == False:
                enemy.hp -= dmg
                return (f'{enemy.name} получил {dmg} урона!')
                
            elif enemy.used_untouchable == True:
                enemy.hp -= dmg
                return (f'{enemy.name} неудачно уклонился и получил {dmg} урона!')
                
        else:
            self.untouchable = False
            return(f'{enemy.name} уклонился от вашего удара')
        
    def P_escape(self):
        print('Вы пытаетесь уклониться!')
        self.used_untouchable = True
        if randint(0,1) == 1:
            self.untouchable = True

    def P_walk(self, arena):
        steps = input('Куда я пойду?\n')
        direction = steps.split()[0]
        steps_num = int(steps.split()[1])
        tostar = arena.P_current_cell-1
        if direction in ('Влево','влево', 'В лево', 'в лево', 'В Лево' ):
            if arena.P_current_cell - steps_num > 0:
                if arena.P_current_cell - steps_num != arena.E_current_cell:
                    arena.P_current_cell -= steps_num
                    arena.curr_pos[tostar] = '*  '
                    arena.init_pos()
                    arena.show_arena()
                else:
                    print('Враг может наброситься на меня.. Пожалуй, не буду подходить так близко')
            else:
                print('Там, кажется, стена.. ')
        elif direction in ('Вправо','Вправо', 'В право', 'в право', 'В Право' ):
            if arena.P_current_cell + steps_num < arena.cells+1:
                if arena.P_current_cell + steps_num != arena.E_current_cell:
                    arena.P_current_cell += steps_num
                    arena.curr_pos[tostar] = '*  '
                    arena.init_pos()
                    arena.show_arena()
                else:
                    print('Враг может наброситься на меня.. Пожалуй, не буду подходить так близко')
            else:
                print('Там, кажется, стена.. ')
        else:
            print('Куда куда?!?')
                

            
    

# player1.add_weapon(Drop('epic', magic))
# player1.display_inventory()
