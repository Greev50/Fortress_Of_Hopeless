from random import randint

def chooserarity(biome_max_rarity):
    rarities = {'common':0.500, 'rare' : 0.300 , 'epic' : 0.150 , 'legendary' : 0.050}
    max_colvo=0
    for el in rarities.items():
        el=list(el)
        max_colvo+=el[1]*1000
        if el[0]==biome_max_rarity:
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

