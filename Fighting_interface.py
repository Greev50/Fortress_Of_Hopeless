from character import *
from weapons import *
from enemies import *
from fight import *


player1 = Character(100, 10, 3, None, [TestGun])
enemy1 = Black_Pearl_enemy()
a = Arena()

a.show_arena()

for i in range(9):
    player1.P_walk(a, f'Вправо 1')
