import random


items = {
    "Health Potion": {"type": "potion", "heal_amount": 20},
    "Rat Tail": {"type": "junk", "value": 1},
    "Bone Shard": {"type": "junk", "value": 2},
    "Small Coin Purse": {"type": "currency", "coins": 10},
    "Torn Cloth": {"type": "material", "value": 3},
    "Wolf Fang": {"type": "material", "value": 5},
    "Orcish Coin": {"type": "currency", "coins": 20},
    "Rotten Flesh": {"type": "junk", "value": 1},
    "Spider Silk": {"type": "material", "value": 8},
    "Medium Coin Purse": {"type": "currency", "coins": 15},
    "Empty Vial": {"Type": "Crafting Material"},
    
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





