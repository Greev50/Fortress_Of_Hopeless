from character import *
from weapons import *
from enemies import *
from fight import *


player1 = Character(100, 10, 3, None, [])
player1.add_weapon(TestGun)
enemy1 = Cursed_BloodHound()
a = Arena()

# a.show_arena(player1, enemy1)
a.start_fight(player1, enemy1)