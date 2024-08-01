from weapons import *

class Character:
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
        print(f'Текущее оружие: {self.inv[0]}\nЗелья здоровья: {self.heal}')
        print(f'Рюкзак: {', '.join([x.return_inv() for x in self.inv[1:]])}')
        print('=============================================================')


    def add_weapon(self, weapon):
        if self.emptyslots > 0:
            self.inv.append(weapon)
            print('Фух, еле влезло')
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
    
    def get_damage(self, amount:int):
        self.hp -= amount
        print(f'Вы получили {amount} урона!')
    
    def use_heal(self, amount_of_heal):
        if amount_of_heal > 0:
            self.hp += 50
            self.heal -= 1
            print(f'Зелье лечения восстановило 50 здоровья.\nСейчас у вас {self.hp} здоровья!')
        else:
            print('Ах.. Ни одного не осталось..')
        
    
    
    


# player1 = Character(100, 10, 3, None, ['starter_sword'])
# player1.add_weapon(Drop('epic', magic))
# player1.display_inventory()