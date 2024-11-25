import random

class monster_level_1:
    monster_types_1 =  ["Plague Beetle" , "Dust Imp", "Skeleton Minion" , "Forest Rat"]
    
    loot_pool_1 = ["Health Potion", "Rat Tail", "Bone Shard", "Small Coin Purse", "Torn Cloth"]
    
    
    def __init__(self, name=None):
        if name is None:
            name = random.choice(list(self.monster_types_1))
            self.name = name
            
        self.hp = random.randint(4 , 13)
        self.attack_power = random.randint(3 , 15)
        self.loot = random.sample(self.loot_pool_1, k=random.randint(1, 2))
        self.score = random.randint(1 , 7)



class monster_level_2: 
    monster_types_2 = ["Vicious Wolf" , "Orc Grunt" , "Zombie Peasant" , "Darkwood Spider"]
    
    loot_pool_2 = ["Wolf Fang", "Orcish Coin", "Rotten Flesh", "Spider Silk", "Medium Coin Purse"]
    
    def __init__(self, name=None):
        if name is None:
            name = random.choice(list(self.monster_types_2))
            self.name = name
            
        self.hp = random.randint(20 , 35)
        self.attack_power = random.randint(10 , 18)
        self.loot = random.sample(self.loot_pool_2, k=random.randint(1, 3))
        self.score = random.randint(8 , 15)

        


def spawn_random_monster_level_1():
    monster_class = random.choice([monster_level_1])
    return monster_class()

monster = spawn_random_monster_level_1()