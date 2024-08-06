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

    raritymultiply = {'common' : 1, 'rare' : 1.2, 'epic' : 1.5, 'legendary' : 2, 'relic' : 1}

    def __init__(self, rarity='common', damage=0, attack_speed=0, crit_chance=0, distance=0, name = 'Weapon', crit_multyply = 1):
        self.damage = damage
        self.attack_speed = attack_speed
        self.crit_chance = crit_chance
        self.rarity = rarity
        self.distance = distance
        self.name = name
        self.crit_multiply = crit_multyply
        

    def total_damage(self):
        
        if randint(1, 100) <= int(self.crit_chance*100) == True:
            print('Критический удар!')
            return int(self.damage * self.raritymultiply[self.rarity] * self.attack_speed * self.crit_multiply)
        else:
            return int(self.damage * self.raritymultiply[self.rarity] * self.attack_speed)
        
    def display_info(self):
        print(f'===========================================\n\t\t=== {self.name} ===\nРедкость: {self.rarity}\n\nУрон: {int(self.damage * self.raritymultiply[self.rarity] * self.attack_speed)}\nУдаров за ход: {self.attack_speed}\nШанс крита: {self.crit_chance}\nКрит. Множитель: {self.crit_multiply}\n===========================================')
    
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
        self.crit_multiply = choice((1, 1.1, 1.2, 1.3, 1.4))

class Two_Armed_Sword(Melee):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Двуручный Меч'

        self.damage = randint(17, 23)
        self.attack_speed = 1
        self.crit_chance = 0.2
        self.rarity = rarity
        self.crit_multiply = choice((1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8))

class Dagger(Melee):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Клинок'

        self.damage = randint(5, 10)
        self.attack_speed = 3
        self.crit_chance = 0.6
        self.rarity = rarity
        self.crit_multiply = choice((1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2))

class Touch_Arts(Melee): # *
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Искусство Пальцев'

        self.damage = randint(3, 30)
        self.attack_speed = randint(2, 5)
        self.crit_chance = 0.7
        self.rarity = rarity
        self.crit_multiply = choice((1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2))

class Heart_Of_Devil(Melee): # Дроп с босса, моргенштерн
    def __init__(self):
        super().__init__()

        self.name = 'Сердце Дьявола'

        self.damage = randint(66, 666)
        self.attack_speed = randint(1, 6)
        self.crit_chance = 0.6
        self.rarity = 'Relic'
        self.crit_multiply = choice((1.5, 1.6, 1.7, 1.8, 1.9, 2))
    
    def bloodbath(self):
        print('При убийстве вырывает сердце у моба и прибавляет к своему урону 20% от урона моба на 10 минут. Наносит 666 урона. time()')
        # Цена: 10 и 1 ход


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
        self.crit_multiply = choice((1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6))

class Bow(Gun):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Лук'

        self.damage = randint(9, 16)
        self.attack_speed = 2
        self.crit_chance = 0.5
        self.rarity = rarity
        self.crit_multiply = choice((1, 1.1, 1.2))

class CrossBow(Gun):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Арбалет'

        self.damage = randint(14, 20)
        self.attack_speed = 1
        self.crit_chance = 0.2
        self.rarity = rarity
        self.crit_multiply = choice((1, 1.1, 1.2, 1.3, 1.4))

class Throwing_Knife(Gun): # *
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Метательный нож'

        self.damage = randint(1, 7)
        self.attack_speed = randint(1, 7)
        self.crit_chance = 0.08
        self.rarity = rarity
        self.crit_multiply = choice((1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7))

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
        self.crit_multiply = choice((1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7))

class Magic_Orb(Magic):
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Магическая Сфера'

        self.damage = randint(10, 14)
        self.attack_speed = 3
        self.crit_chance = 0.3
        self.rarity = rarity
        self.crit_multiply = choice((1, 1.1, 1.2, 1.3))

class Rune(Magic): # *
    def __init__(self, rarity):
        super().__init__()

        self.name = 'Руна'

        self.damage = randint(1, 30)
        self.attack_speed = 1
        self.crit_chance = 0.5
        self.rarity = rarity
        self.crit_multiply = choice((1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2))

melee = (Sword, Two_Armed_Sword, Dagger, Touch_Arts)
guns = (Bow, CrossBow, Pistol, Throwing_Knife)
magic = (Wand, Magic_Orb, Rune)

def Random_Drop(max_biome_rarity, type_of_weapon):
    data = choice(type_of_weapon)
    weapon = data(chooserarity(max_biome_rarity))
    weapon.display_info()

    return weapon

def MeleeDrop(max_biome_rarity):
    weapon = choice(melee)(chooserarity(max_biome_rarity))
    weapon.display_info()

    return weapon

def GunDrop(max_biome_rarity):
    weapon = choice(guns)(chooserarity(max_biome_rarity))
    weapon.display_info()

    return weapon

def MagicDrop(max_biome_rarity):
    weapon = choice(magic)(chooserarity(max_biome_rarity))
    weapon.display_info()

    return weapon

TestGun = Sword('rare')
