import random
import enemies_list


items = {
    
    #Coins
    "Small Coin Purse": {"type": "currency", "coins": 10},
    "Orcish Coin": {"type": "currency", "coins": 20},
    "Medium Coin Purse": {"type": "currency", "coins": 15},
    
    #Potions
    "Health Potion": {"type": "potion", "heal_amount": 20},
    
    #Material
    "Torn Cloth": {"type": "material", "value": 3},
    "Wolf Fang": {"type": "material", "value": 5},
    "Spider Silk": {"type": "material", "value": 8},
    
    #Crafting Material
    "Empty Vial": {"Type": "Crafting Material"},
    
    #Weapons
    
    #Junk
    "Rat Tail": {"type": "junk", "value": 1},
    "Bone Shard": {"type": "junk", "value": 2},
    "Rotten Flesh": {"type": "junk", "value": 1},
    
}

# Define different loot pools if needed for different monster levels
loot_pool_1 = ["Health Potion", "Rat Tail", "Bone Shard", "Small Coin Purse", "Torn Cloth", "Empty Vial"]
loot_pool_2 = ["Wolf Fang", "Orcish Coin", "Rotten Flesh", "Spider Silk", "Medium Coin Purse", "Empty Vial", ]



recipes = {
    "Mana Potion": {"type":"Recipe",  "required": {"Wolf Fang": 1, "Empty Vial": 1}},
    "Arcane Shield": {"type":"Recipe", "required": {"Spider Silk": 1, "Health Potion": 1 }}
    
    
}

def crafting_menu(hero):
    print("\nCrafting Menu")
    if not hero.discovered_recipes:
        print("You havent discovered any recipes yet.")
        return
    
    print("Available Recipes:")
    for recipes_name in hero.discovered_recipes:
        recipe = recipes.get(recipes_name)
        if recipe:
            required_materials = ", ".join([f"{mat} x{qty}" for mat, qty in recipe["required"].items()])
            print(f"- {recipes_name}: Requires {required_materials}")
    
    # Prompt player for crafting choice
    item_to_craft = input("Enter the item you want to craft or 'exit' to leave: ")
    if item_to_craft.lower() == "exit":
        print("Exiting crafting menu.")
        return

    # Delegate crafting to the hero's crafting function
    hero.crafting_function(item_to_craft)


import random

def get_random_combat_room():
    return random.choice(room_details ["combat_rooms"])

def get_random_merchant_room():
    return random.choice(room_details["merchant_rooms"])

def get_random_boss_room():
    return random.choice(room_details["boss_rooms"])




room_details = {
    "combat_rooms": [
        {
            "type": "combat",
            "description": "A dimly lit corridor with strange markings on the walls.",
            "enemy_pool": ["goblin", "wolf", "spider"]
        },
        {
            "type": "combat",
            "description": "An old armory with rusted weapons on the ground.",
            "enemy_pool": ["skeleton", "zombie"]
        }
    ],
    "merchant_rooms": [
        {
            "type": "merchant",
            "description": "A small shop lit by a single candle, filled with odd trinkets."
        }
    ],
    "boss_rooms": [
        {
            "type": "boss",
            "description": "A grand hall adorned with tapestries and a looming figure at the far end."
        }
    ]
}


