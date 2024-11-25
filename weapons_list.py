import random
import combat_system

class MeleeWeaponLevel1:
  
    weapons_by_class = {
        "Paladin": {"name": "Sword", "attack_range": (5, 10)},
        "Barbarian": {"name": "Axe", "attack_range": (8, 12)},
        "Wizard": {"name": "Dagger", "attack_range": (3, 6)}
    }

    def __init__(self, hero_class):
        weapon = self.weapons_by_class.get(hero_class)
        if weapon:
            self.name = weapon["name"]
            self.attack_power = random.randint(*weapon["attack_range"])
        else:
            self.name = "Unarmed"
            self.attack_power = 1



spells = {
    "Wizard": [
        {"name": "Fire Blast", "damage": 15, "mana_cost": 10},
        {"name": "Arcane Bolt", "damage": 10, "mana_cost": 8}
    ],
    "Paladin": [
        {"name": "Holy Blast", "damage": 12, "mana_cost": 10},
        {"name": "Holy Heal", "heal_amount": 10, "mana_cost": 20},
        {"name": "Holy Spirit", "mana_cost": 100, "special_effect": "Holy Power"}
    ]
}

status_effects = {
    "Holy Power": {
        "name": "Holy Power",
        "status_message": "Blessed",
        "attack_bonus": 3,
        "mana_drain": "all",
        "duration": None,
        "effect_type": "buff"
    },
    "Arcane Shield": {
        "name": "Arcane Shield",
        "defense_bonus": 2,
        "mana_drain": 20,
        "duration": 3,
        "effect_type": "buff"
    }
    
}
    


def get_spells_for_class(hero_class):
    
    return spells.get(hero_class, [])



def get_weapon_for_class(hero_class):
    
    weapon = MeleeWeaponLevel1(hero_class)
    inventory = [{"name": weapon.name, "attack": weapon.attack_power}]
    
    
    inventory.extend(get_spells_for_class(hero_class))
    return inventory
