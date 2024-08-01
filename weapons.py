from random import randint, choice

def chooserarity(max_biome_rarity):
    rarities = {'common':0.500, 'rare' : 0.300 , 'epic' : 0.150 , 'legendary' : 0.050}
    max_colvo=0
    for el in rarities.items():
        el=list(el)
        max_colvo+=el[1]*1000
        if el[0]==max_biome_rarity:
            break

    max_colvo=int(max_colvo)
    prev = 0
    curr_chance = randint(1, max_colvo)
    res=None
    for saved_chance in rarities:
        if curr_chance in range(int(prev),int(rarities[saved_chance]*1000)+int(prev)):
            res = saved_chance
            break
        else:
            prev += rarities[saved_chance]*1000
    return res         

class Weapon:
    def __init__(self, rarity='common', damage=0, attack_speed=0, crit_chance=0, distance=0, name = 'Weapon'):
        self.damage = damage
        self.attack_speed = attack_speed
        self.crit_chance = crit_chance
        self.rarity = rarity
        self.distance = distance
        self.name = name

    def total_damage(self):
        raritymultiply = {'common' : 1, 'rare' : 2, 'epic' : 3, 'legendary' : 4}
        if randint(1, 100) <= int(self.crit_chance*100) == True:
            return self.damage * raritymultiply[self.rarity] * self.attack_speed * 2
        else:
            return self.damage * raritymultiply[self.rarity] * self.attack_speed
        
    def display_info(self):
        raritymultiply = {'common' : 1, 'rare' : 2, 'epic' : 3, 'legendary' : 4}
        print(f'===========================================\n\t\t=== {self.name} ===\nРедкость: {self.rarity}\n\nУрон: {self.damage*raritymultiply[self.rarity]}\nУдаров за ход: {self.attack_speed}\nШанс крита: {self.crit_chance}\n===========================================')
    
    def return_inv(self):
        return f'{self.rarity} {self.name}'
        
# --------------------------------------------------------------------------------------

class Melee(Weapon):
    def __init__(self):
        super().__init__()
        self.distance = 3


class Sword(Melee):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Меч'

        self.damage = randint(8, 12)
        self.attack_speed = 2
        self.crit_chance = 0.5
        self.rarity = rarity

class Two_Armed_Sword(Melee):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Двуручный Меч'

        self.damage = randint(17, 23)
        self.attack_speed = 1
        self.crit_chance = 0.2
        self.rarity = rarity

class Dagger(Melee):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Клинок'

        self.damage = randint(5, 10)
        self.attack_speed = 3
        self.crit_chance = 0.6
        self.rarity = rarity

class Touch_Arts(Melee): # *
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Искусство пальцев'

        self.damage = randint(3, 30)
        self.attack_speed = randint(2, 5)
        self.crit_chance = 0.7
        self.rarity = rarity

# --------------------------------------------------------------------------------------

class Gun(Weapon):
    def __init__(self):
        super().__init__()
        self.distance = 8

class Pistol(Gun):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Пистолет'

        self.damage = randint(6, 10)
        self.attack_speed = 3
        self.crit_chance = 0.3
        self.rarity = rarity

class Bow(Gun):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Лук'

        self.damage = randint(9, 16)
        self.attack_speed = 2
        self.crit_chance = 0.5
        self.rarity = rarity

class CrossBow(Gun):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Арбалет'

        self.damage = randint(14, 20)
        self.attack_speed = 1
        self.crit_chance = 0.2
        self.rarity = rarity

class Throwing_Knife(Gun): # *
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Метательный нож'

        self.damage = randint(1, 7)
        self.attack_speed = randint(1, 7)
        self.crit_chance = 0.08
        self.rarity = rarity

# --------------------------------------------------------------------------------------

class Magic(Weapon):
    def __init__(self):
        super().__init__()
        self.distance = 6

class Wand(Magic):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Посох'

        self.damage = randint(8,13)
        self.attack_speed = 2
        self.crit_chance = 0.3
        self.rarity = rarity

class Magic_Orb(Magic):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Магическая Сфера'

        self.damage = randint(10, 14)
        self.attack_speed = 3
        self.crit_chance = 0.3
        self.rarity = rarity

class Rune(Magic): # *
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Руна'

        self.damage = randint(1, 30)
        self.attack_speed = 1
        self.crit_chance = 0.5
        self.rarity = rarity

melee = (Sword, Two_Armed_Sword, Dagger, Touch_Arts)
guns = (Bow, CrossBow, Pistol, Throwing_Knife)
magic = (Wand, Magic_Orb, Rune)

def Drop(max_biome_rarity, type_of_weapon):
    data = choice(type_of_weapon)
    weapon = data(chooserarity(max_biome_rarity))
    weapon.display_info()

    return weapon