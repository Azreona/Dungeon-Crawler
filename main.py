from weapons_list import get_weapon_for_class
from combat_system import start_battle
from items_list import items
from weapons_list import status_effects
import items_list 
import Battle_arena
from enemies_list import spawn_random_monster_level_1, spawn_random_monster_level_2
import random
import npc


class StatusEffect:
    def __init__(self, name, attack_bonus=0, mana_drain=0, duration=None, effect_type="buff"):
        self.name = name
        self.attack_bonus = attack_bonus
        self.mana_drain = mana_drain
        self.duration = duration  # Duration in turns, None for permanent effects
        self.effect_type = effect_type  # Can be "buff", "debuff", etc.

    def apply_effect(self, hero):
        # Apply only the effects specified in the status effect instance
        if self.mana_drain == "all":
            hero.mana = 0
        elif self.mana_drain > 0:
            hero.mana = max(0, hero.mana - self.mana_drain)
        
        
        if hasattr(self, "attack_bonus") and self.attack_bonus:
           
            hero.temp_attack_bonus = getattr(hero, "temp_attack_bonus", 0) + self.attack_bonus


class Hero:
    def __init__(self, name, hero_class, hp, mana=100):
        # Initialize hero with name, class, HP, mana, and an inventory with the class-based weapon or spells
        self.name = name
        self.hero_class = hero_class
        self.hp = hp
        self.max_hp = hp  # Set max_hp based on initial HP
        self.mana = mana
        self.max_mana = mana  # Set max_mana based on initial Mana
        self.inventory = []
        self.discovered_recipes = []
        self.score = 0
        self.status_effects = []
        self.coins = 0 
        
        
        weapons_or_spells = get_weapon_for_class(hero_class)
        if weapons_or_spells:
            self.inventory.extend(weapons_or_spells) 

    def use_potion(self, potion_name):
        # Check if the potion is in inventory
        if potion_name in self.inventory:
            potion = items.get(potion_name)
            
            # Apply effects based on potion type
            if potion["type"] == "potion":
                if "heal_amount" in potion:
                    heal_amount = potion["heal_amount"]
                    self.hp = min(self.hp + heal_amount, self.max_hp)  # Heal but don't exceed max HP
                    print(f"{self.name} used a {potion_name} and healed {heal_amount} HP!")
                
                elif "mana_restore" in potion:
                    mana_restore = potion["mana_restore"]
                    self.mana = min(self.mana + mana_restore, self.max_mana)  # Restore mana but don't exceed max mana
                    print(f"{self.name} used a {potion_name} and restored {mana_restore} mana!")

                # Remove the used potion from inventory
                self.inventory.remove(potion_name)
            else:
                print(f"{potion_name} is not a usable potion.")
        else:
            print(f"{potion_name} is not in your inventory.")

    
    def show_inventory(self):
        
        print(f"{self.name} - {self.hero_class}")
        print(f"HP: {self.hp}/{self.max_hp}  Mana: {self.mana}/{self.max_mana}")
        print(f"Total Coins: {self.coins}")

        
        print("Inventory:")
            
        
        if self.inventory:
            for item in self.inventory:
                if isinstance(item, dict):
                    # Melee weapon with 'attack' attribute
                    if "attack" in item:
                        print(f"{item['name']} - Attack: {item['attack']}")
                    # Spell with 'damage' and 'mana_cost'
                    elif "damage" in item:
                        print(f"{item['name']} - Damage: {item['damage']}, Mana Cost: {item['mana_cost']}")
                    elif item.get("type") == "Recipe":
                        required_materials = ", ".join([f"{mat} x{qty}" for mat, qty in item.get("required", {}).items() ])
                        print(f"{item['name']} - Recipe: Requires {required_materials}")
                        
                elif isinstance(item, str) and item in items:
                    # Check if it's a potion or other type in the items dictionary
                    
                    item_details = items[item]
                    item_type = item.details.get("type", "Unkown")
                    if item_type == "potion":
                        effects = []
                        if "heal_amount" in item_details:
                            effects.append(f"Heals {item_details['heal_amount']} HP")
                        if "mana_restore" in item_details:
                            effects.append(f"Restores {item_details['mana_restore']} Mana")
                        print(f"{item} - {', '.join(effects)}")
                    else:
                        
                        print(f"{item} - Type: {item_details['type']}")
        else:
            print("Empty")
            
    def add_to_inventory(self, item):
        # Check if the item is currency; if so, add to coin count
        if isinstance(item, str) and item in items:
            item_details = items[item]
            if item_details.get("type") == "currency":
                self.coins += item_details.get("coins", 0)
                print(f"{item_details['coins']} coins added. Total Coins: {self.coins}")
            else:
                # Add other item types to the inventory
                self.inventory.append(item)
        elif isinstance(item, dict) and "coins" in item:
            self.coins += item["coins"]
            print(f"{item['coins']} coins added. Total Coins: {self.coins}")
        else:
            self.inventory.append(item)
    
    #def remove_from_inventory(self, item):
        #if isinstance(item, str) and item in Hero.inventory:
            
            
      
    def collect_loot(self, loot_items): 
        for item in loot_items:
            self.add_to_inventory(item)
            
    def crafting_function(self, item_name):
        
        recipe = items_list.recipes.get(item_name)  # Reference the recipes dictionary THIS IS THE ORIGINAL WORKING
        
        #recipe = hero.inventory.items_list.recipes.get(item_name)
        if not recipe:
            print(f"No recipe for {item_name}.")
            return

        # Check if hero has all required materials
        missing_materials = []
        for material, qty in recipe["required"].items():
            if self.inventory.count(material) < qty:
                missing_materials.append((material, qty - self.inventory.count(material)))

        if missing_materials:
            print(f"Cannot craft {item_name}. Missing materials:")
            for material, qty in missing_materials:
                print(f"- {material}: {qty} more needed")
            return

        # Remove materials and add crafted item
        for material, qty in recipe["required"].items():
            for _ in range(qty):
                self.inventory.remove(material)

        self.inventory.append(item_name)
        print(f"{item_name} crafted successfully and added to your inventory!")
    
    def add_discovered_recipes(self, recipe_name):
        if recipe_name not in self.discovered_recipes:
            self.inventory.append(recipe_name)
            print (f"{self.name} discovered the recipe for {recipe_name} ")
            
            
            
def character_action():

    while True:
        print("\nWhat would you like to do?")
        print("1. Look around")
        print("2. Engage")
        print("3. Check inventory")
        print("4. Use a potion")
        print("5. Craft Items")
        #print("6. Admin Options")
        print("0. Exit the arena")
        
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"You look around:{room_details['Description']}")
            if room_details['type'] == "combat":
                print(f" There are {len(room_details['enemies'])} enemies in the room.")
                for enemy in room_details["enemies"]:
                    print(f"- {enemy.name} (HO: {enemy.hp})")
            elif room_details("type") == "merchant":
                print("You spot a merchant in the corner, reay to trade.")
            elif room_details("type") == "boss":
                print("This room houses a formidable foe. Prepare yourself")
            else:
                print("The Room appears to be empty")
        
        
        elif choice == "2":
            # Engage with the room content
            if room_details["type"] == "combat":
                print("You prepare for battle!")
                for enemy in room_details["enemies"]:
                    start_battle(hero, enemy)
            elif room_details["type"] == "merchant":
                print("You approach the merchant to see their wares.")
                npc.npc_merchant(hero)
            elif room_details["type"] == "boss":
                print("You face the boss in a challenging fight!")
                # Add boss battle logic here
            else:
                print("Nothing to engage with here.")
            break  # Exit the room loop after engaging
        
        elif choice == "3":
            print("\nInventory:")
            hero.show_inventory()
        
        elif choice == "4":
          
            potion_name = input("Enter the name of the potion you want to use: ")
            hero.use_potion(potion_name)  # Use potion if available
            
        elif choice == "5":
            items.list.crafting_menu(hero)
            
        elif choice == "0":
            Battle_arena.admin_actions(hero)


        elif choice == "7":
            print("Exiting the arena. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
      

def create_hero():
    # Get hero name from the user
    name = input("Enter your hero's name: ")

    # Define valid hero classes and their corresponding HP
    class_hp = {
        "Paladin": 150,
        "Barbarian": 200,
        "Wizard": 100
    }

    
    hero_class = None
    while hero_class not in class_hp:
        hero_class = input(f"Choose your class ({', '.join(class_hp.keys())}): ")
        if hero_class not in class_hp:
            print(f"Invalid class. Please choose from {', '.join(class_hp.keys())}.")

    # Automatically assign HP based on the chosen class
    hp = class_hp[hero_class]

    # Create the hero using the inputs
    hero = Hero(name, hero_class, hp,)

    return hero

def generate_room(room_number):
    if room_number % 10 == 0 :
        return 
        print (f"You shiver in Fear as {boss["type"]} enters the dungeon")
        print (f"{boss[description]}")
    elif random.random() < 0.2:
        return
        npc_merchant()
    else: 
        enemy_count = random.randint(1, 3)
        enemies = [spawn_random_monster_level_1() for _ in range(enemy_count)]
        return {"type": "combat", "description": f"Combat Room {room_number}", "enemies": enemies}
    
    
def start_game():
       
    