from character import *
from weapons import *
from enemies import *
from fight import *


player1 = Character(100, 10, 3, None, [TestGun])
enemy1 = Black_Pearl_enemy()
a = Arena()


# player1.P_walk(a)
enemy1.E_walk(a, player1, False)

