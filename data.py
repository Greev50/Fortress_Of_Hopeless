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

# if arena.E_current_cell - steps_num_False > 0:
#     # print(f'{arena.E_current_cell} - {steps_num_False} = {arena.E_current_cell - steps_num_False}')
#     if arena.E_current_cell - steps_num_False != arena.P_current_cell:
#         arena.E_current_cell -= steps_num_False
#         arena.curr_pos[tostar] = '*  '
#         arena.init_pos()
#         arena.show_arena()
#         True_cord = True
#     else:
#         True_cord = False
#         steps_num_False += 1
# else:
#     True_cord = False
#     steps_num_False += 1
#     print('2', steps_num_False)


# if self.inv:
#     ans = input('Какое оружие выкинуть?\n')       
#     if ans.isdigit():
#         ans = int(ans)
#         print(f'Прощай, прекрасный {self.inv[ans].name}!')
#         del self.inv[ans]
#     else:
#         ans = ''.join(ans.split()[0]) + ' ' + ' '.join([x.capitalize() for x in ans.split()[1:]])
#         if ans not in self.inv:
#             print('Мне бы его найти вначале')
#         ans_index = [x.return_inv() for x in self.inv].index(ans)
#         print(f'Прощай, прекрасный {self.inv[ans].name}!')
#         del self.inv[ans_index]
# else:
#     print('Я не хочу выбрасывать свое единственное оружие!')