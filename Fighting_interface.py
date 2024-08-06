from character import *
from weapons import *
from enemies import *
from fight import *


player1 = Character(100, 10, 3, None, [])
player1.add_weapon(TestGun) 
dwn = Downstairs()
a = Arena(dwn)

# a.show_arena(player1, enemy1)
a.start_fight(player1)
# a.show_arena(player1, enemy1)
# 