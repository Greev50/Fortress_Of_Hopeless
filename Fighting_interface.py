from character import *
from weapons import *
from enemies import *
from fight import *


player1 = Character(100, 10, 3, None, [TestGun])
enemy1 = Cursed_BloodHound()
a = Arena()

a.start_fight(player1, enemy1, a)
