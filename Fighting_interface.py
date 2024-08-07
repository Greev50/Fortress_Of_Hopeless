from character import *
from weapons import *
from enemies import *
from fight import *


player1 = Character()
for _ in range(3):
    player1.add_weapon(TestGun) 
# enemy1 = Cloud_Of_Soul_Pain()
dwn = Downstairs()
a = Arena(dwn)

# a.show_arena(player1, enemy1)
a.start_fight(player1)
# a.show_arena(player1, choice(dwn.enemies)())
