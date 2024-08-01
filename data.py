from random import randint

def chooserarity(self):
        prev = 0
        dropped_chance = randint(1, 100)
        for saved_chance in self.rarity:
            if dropped_chance in range(int(prev),int(self.rarity[saved_chance]*100)+int(prev)):                
                return saved_chance
            else:
                prev += self.rarity[saved_chance]*100