from random import randint
from weapons import *

class Character:
    untouchable = False
    used_untouchable = False
    is_inv_opened = False
    'Ex: player1 = Character(100, 10, 3, None, [starter_sword])'

    def __init__(self, hp = 100, stamina = 10, heal = 3, class_bonus = None, inv = []):
        self.hp = hp
        self.stamina = stamina
        self.heal = heal
        self.emptyslots = 5 - len(inv)
        self.inv = inv # inv = {curr_weapon, slot_1, slot_2, slot_3}
        self.class_bonus = class_bonus
        self.distance = 0
        self.stamina = 10

    def can_reach_enemy(self, arena):
        # print(arena.P_current_cell - self.distance, arena.P_current_cell + self.distance+1)
        if arena.E_current_cell in range(arena.P_current_cell - self.distance, arena.P_current_cell + self.distance+1):
            return True
        return False

    def P_return_distance(self, arena):
        # return self.distance
        if arena.P_current_cell + self.distance < arena.cells:
            if arena.P_current_cell - self.distance > 0:
                return tuple(range(arena.P_current_cell - self.distance, arena.P_current_cell + self.distance+1))
            else:
                return tuple(range(1, arena.P_current_cell + self.distance+1))
        else:
            if arena.P_current_cell - self.distance > 0: 
                return tuple(range(arena.P_current_cell - self.distance, arena.cells+1))
            else:
                return tuple(range(1, arena.cells+1))


    def display_inventory(self):
        print('=============================================================')
        print('\t\t\tИнвентарь  | (1,2,3) - Осмотеть слот')
        print(f'Здоровье: {self.hp}\t\t\t   |  4 - Выйти из инвентаря\nВыносливость: {self.stamina}\t\t   -------------------------')
        print('\t\t\t=========')
        print(f'Текущее оружие: {self.inv[0].return_inv()}\nЗелья здоровья: {self.heal}')
        print(f'Рюкзак: {', '.join([x.return_inv() for x in self.inv[1:]])}')
        print('=============================================================')

    def inv_interact(self):
        self.is_inv_opened = True
        while self.is_inv_opened == True:
            self.display_inventory()
            print('Что бы мне сделать?')
            ans = str(input())
            if ans.lower() in ('сменить текущее оружие', 'изменить текущее оружие', 'сменю текущее оружие', 'изменю текущее оружие', 'поменять текущее оружие', 'поменяю текущее оружие', f'поменять {self.inv[0].return_inv}', f'поменяю {self.inv[0].return_inv}', 'взять другое оружие', 'возьму другое оружие', 'сменю свое оружие', 'сменить свое оружие', 'сменю оружие', 'сменить оружие', 'изменить оружие', 'сменить главное оружие', 'поменять главное оружие'): 
                self.change_curr_weapon()
            elif ans.lower() in ('удалить оружие', 'выкинуть оружие', 'выкину оружие', 'удалю оружие', 'выброшу оружие', 'выбросить оружие'):
                self.del_weapon()
            elif ans.lower() in ('осмотрю оружия', 'осмотреть оружия', 'что у меня за оружия?', 'посмотрю свои оружия', 'осмотрю все оружия', 'посмотрю все оружия', 'все оружия', 'оружия'):
                [x.display_info() for x in self.inv]
            elif ans.lower() in ('посмотрю на оружие', 'посмотрю оружие', 'посмотреть на оружие', 'посмотреть оружие', 'оружие', 'осмотреть оружие'):
                if len(self.inv) > 1:
                    ans = input('Какое оружие осмотреть?\n')       
                    if ans.isdigit():
                        ans = int(ans)
                        if ans == 0:
                            print('А у меня такого нет! Готов поклясться, ни у кого нет нулевого оружия)')
                            return
                        self.inv[ans].display_info()
                        ans1 = str(input('Сделать с ним что нибудь?\n'))
                        if ans1 in ('удалить оружие', 'выкинуть оружие', 'выкину оружие', 'удалю оружие', 'выброшу оружие', 'выбросить оружие'):
                            del self.inv[ans]
                        else:
                            print('Согласен, все же оно классное ;)')
                    else:
                        ans = ''.join(ans.split()[0]) + ' ' + ' '.join([x.capitalize() for x in ans.split()[1:]])
                        try:
                            ans_index = [x.return_inv() for x in self.inv].index(ans)
                        except ValueError:
                            print('Такого оружия у меня, кажется нет')
                            return
                        self.inv[ans_index].display_info()
                        ans1 = str(input('Сделать с ним что нибудь?\n'))
                        if ans1 in ('удалить оружие', 'выкинуть оружие', 'выкину оружие', 'удалю оружие', 'выброшу оружие', 'выбросить оружие'):
                            del self.inv[ans_index]
                        else:
                            print('Согласен, все же оно классное ;)')
                else:
                    print('Мне бы вначале найти другое оружие')
                    return

            elif ans.lower() in ('выйти', 'хочу выйти', 'закрою инвентарь', 'закрыть инвентарь', 'закрыть', 'закрою', 'инвентарь', 'выход', 'все', 'всё', 'выйду'):
                self.is_inv_opened = False
                print('Да, пожалуй, на этом все.')
            else:
                print('Опять что то в ухе жужжит, не расслышал. Попробуем еще раз!')

    def add_weapon(self, weapon):
        if self.inv:
            if self.emptyslots > 0:
                self.inv.append(weapon)
                print(choice(['Фух, еле влезло', 'Отлично!', 'Хаха, вот это мощь!']))
            else:
                print('Не влезает в рюкзак..')
        else:
            self.inv.append(weapon)
            self.distance = weapon.distance
            print('Хаха! Мое первое оружие! Я должен повесить его на стенке дома.')


    def del_weapon(self):
        if len(self.inv) > 1:
            ans = input('Какое оружие выкинуть?\n')       
            if ans.isdigit():
                ans = int(ans)
                if ans == 0:
                    print('Это какое такое нулевое?')
                    return
                print(f'Прощай, прекрасный {self.inv[ans].name}!')
                del self.inv[ans]
            else:
                ans = ''.join(ans.split()[0]) + ' ' + ' '.join([x.capitalize() for x in ans.split()[1:]])
                try:
                    ans_index = [x.return_inv() for x in self.inv].index(ans)
                except ValueError:
                    print('Я его уже где то выкинул')
                    return
                print(f'Прощай, прекрасный {self.inv[ans_index].name}!')
                del self.inv[ans_index]               
        else:
            print('Я не хочу выбрасывать свое единственное оружие!')
            return


    def change_curr_weapon(self): 
        if len(self.inv) > 1:
            ans = input('Хм.. Какое оружие взять?\n')       
            if ans.isdigit():
                ans = int(ans)
                if ans == 0:
                    print('Не бывает нулевого оружия!')
                    return
                curr_data = self.inv[0]
                self.inv[0] = self.inv[ans]
                self.distance = self.inv[ans].distance
                del self.inv[ans]
                self.inv.append(curr_data)
                print(f'{self.inv[0].return_inv()}! Оно подойдет')
            else:
                ans = ''.join(ans.split()[0]) + ' ' + ' '.join([x.capitalize() for x in ans.split()[1:]])
                try:
                    ans_index = [x.return_inv() for x in self.inv].index(ans)
                except ValueError:
                    print('Такого оружия у меня, кажется нет')
                    return
                curr_data = self.inv[0]
                self.inv[0] = self.inv[ans_index]
                del self.inv[ans_index]
                self.inv.append(curr_data)
                self.distance = self.inv[ans_index].distance
                print(f'{self.inv[0].return_inv()}. Оно подойдет!')
            self.display_inventory()
        else:
            print('Мне бы вначале найти другое оружие')
            return
    
    def P_use_heal(self):
        if self.stamina >= 6:
            if self.heal > 0:
                if self.hp + 50 <= 100:
                    self.hp += 50
                    self.stamina -= 6
                else:
                    self.hp = 100
                self.heal -= 1
                self.stamina -= 6
                print(f'Зелье лечения восстановило 50 здоровья.\nСейчас у вас {self.hp} здоровья!')
            else:
                print('Черт! Ни одного не осталось..')
        else:
            print('Чертов рюкзак! Где мое зелье здоровья, когда оно так нужно?!\nЛадно, к черту, и так справлюсь. Может позже смогу найти..')


    
    def P_attack(self, enemy, arena):
        if self.stamina >= 2:
            dmg = self.inv[0].total_damage()
            if self.can_reach_enemy(arena) == True:
                if enemy.untouchable == False:
                    if enemy.used_untouchable == False:
                        enemy.hp -= dmg
                        print(f'{enemy.name} получил {dmg} урона!')
                        self.stamina -= 2
                        
                    elif enemy.used_untouchable == True:
                        enemy.hp -= dmg
                        print(f'{enemy.name} неудачно уклонился и получил {dmg} урона!')
                        self.stamina -= 2
                    
                else:
                    self.untouchable = False
                    print (f'{enemy.name} уклонился от вашего удара')
                    self.stamina -= 2
            else:
                print('Боюсь, что я его не достану')         
        else:
            print('"Тяжелый вздох"\nМинутку.. Передохнуть..')
        
        
    def P_escape(self):
        if self.stamina >= 4:
            print('Ну чтож, уклониться так уклониться!')
            self.used_untouchable = True
            self.stamina -= 4
            if randint(0,1) == 1:
                self.untouchable = True   
        else:
            print('Сил маловато, кувырок получится слабый. Не буду рисковать')
            return
        

    def P_walk(self, arena):
        steps = input('Куда я пойду?\n')
        if len(steps.split()) == 2:
            direction = steps.split()[0]
            steps_num = int(steps.split()[1])
        else:
            direction = steps
            steps_num = int(input('На сколько шагов?\n'))

        if self.stamina >= steps_num*2:
            self.stamina -= steps_num*2
        else:
            print('Черт.. Совсем нет сил')
            
        tostar = arena.P_current_cell-1
        if direction in ('Влево','влево', 'В лево', 'в лево', 'В Лево', 'назад'):
            if arena.P_current_cell - steps_num > 0:
                if arena.P_current_cell - steps_num != arena.E_current_cell:
                    arena.P_current_cell -= steps_num
                    arena.curr_pos[tostar] = '*  '
                    arena.init_pos()
                else:
                    print('Враг может наброситься на меня.. Пожалуй, не буду подходить так близко')
            else:
                print('Там, кажется, стена.. ')
        elif direction.lower() in ('вправо', 'в право', 'направо', 'на право', 'вперед', 'вперёд'):
            if arena.P_current_cell + steps_num < arena.cells+1:
                if arena.P_current_cell + steps_num != arena.E_current_cell:
                    arena.P_current_cell += steps_num
                    arena.curr_pos[tostar] = '*  '
                    arena.init_pos()
                else:
                    print('Враг может наброситься на меня.. Пожалуй, не буду подходить так близко')
            else:
                print('Там, кажется, стена.. ')
        else:
            print('Куда куда?!?')

    def regen_stamina(self):
        self.stamina = 10

    def P_fight_mode(self, E, Arena):
        if self.stamina > 1:
            ans = str(input('Что же мне делать?\n'))
            if ans.lower() in ('идти', 'подойти', 'подойду', 'пойду', 'пойти', 'подойти ближе', 'подойду ближе', 'отойти', 'отойду',  'отойти подальше', 'отойду подальше', 'сблизиться', 'сближусь', 'приблизиться', 'приближусь'):
                self.P_walk(Arena)
            elif ans.lower() in ('атака', 'атакую', 'атаковать', 'еще атаковать', 'в атаку', 'в атаку!', 'в атаку!!', 'в атаку!!!', 'урааа', 'ударю', 'ударить', 'получай', 'убить', 'убью', 'четвертую', 'четвертовать', 'забить', 'забью', 'гасить', 'загасить', 'загашу', 'уничтожу', 'уничтожить', 'бить', 'ударить', 'бью', 'ударяю'):
                self.P_attack(E, Arena)
            elif ans.lower() in ('уклонюсь', 'уклониться', 'избежать атаки', 'избегу атаки', 'уклоняюсь', 'избегаю атаки', 'увернусь', 'увернуться'):
                self.P_escape()
            elif ans.lower() in ('восстановлю здоровье', 'восстановлюсь', 'восстановить здоровье', 'восстановиться', 'захиллюсь', 'захилюсь', 'захиллиться', 'захиллиться', 'зелье здоровья', 'зелье восстановления', 'использую зелье здоровья', 'использовать зелье здоровья', 'использую зелье восстановления', 'использую зелье восстановления', 'восстановить здоровье', 'восстановлю здоровье', 'опа таблеточка', 'зелье лечения', 'использую зелье лечения', 'использовать зелье лечения', 'хил', 'использую хил'):
                self.P_use_heal()
            elif ans.lower() in ('открою инвентарь', 'открыть инвентарь', 'инвентарь', 'использую инвентарь', 'где там мое второе оружие?', 'показать инвентарь', 'воспользуюсь инвентарем'):
                self.inv_interact()
            elif ans.lower() in ('сменить текущее оружие', 'изменить текущее оружие', 'сменю текущее оружие', 'изменю текущее оружие', 'поменять текущее оружие', 'поменяю текущее оружие', f'поменять {self.inv[0].return_inv}', f'поменяю {self.inv[0].return_inv}', 'взять другое оружие', 'возьму другое оружие', 'сменю свое оружие', 'сменить свое оружие', 'сменю оружие', 'сменить оружие', 'изменить оружие', 'сменить главное оружие', 'поменять главное оружие'):
                self.change_curr_weapon()
            elif ans.lower() in ('бежать', 'сбежать', 'сбегу', 'уйти', 'уйду', 'убежать', 'убегу', 'свалить', 'свалю', 'спрятаться', 'спрячусь', 'пощажу его', 'пощадить его', 'пощадить', 'пощажу', 'дарую ему жизнь'):
                Arena.isfight = False
                print('Да, пожалуй, так будет лучше..')
                # задержка
                lost_heal = randint(1, self.heal)
                self.heal -= lost_heal
                print(f'Убегая, я растерял {lost_heal} зелий здоровья, вот черт..')
            else:
                print('Опять что то в ухе жужжит, не расслышал. Попробуем еще раз!')
        else:
            print('Совсем.. Нет.. Сил..')

    
                

# player1 = Character(100, 10, 3, None, [TestGun, Random_Drop('epic', melee)]) 
# player1.inv_interact()  


# player1.display_inventory()
