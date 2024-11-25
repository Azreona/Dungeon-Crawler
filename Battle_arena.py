import random
from main import Hero, create_hero
import main
from combat_system import start_battle, player_turn, enemy_turn, check_victory
from enemies_list import spawn_random_monster_level_1
from items_list import items
from items_list import crafting_menu
import npc


def admin_actions(hero):
    """Admin menu to spawn items, coins, or trigger functions for testing."""
    while True:
        print("\nAdmin Actions:")
        print("1. Add Coins")
        print("2. Add Items to Inventory")
        print("3. Trigger Status Effects")
        print("4. Return to Arena")
        
        choice = input("Choose an admin action: ")
        if choice == "1":
            try:
                amount = int(input("Enter the number of coins to add: "))
                hero.coins += amount
                print(f"{amount} coins added. Total coins: {hero.coins}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "2":
            print("Available Items:")
            for item in items.keys():
                print(f"- {item}")
            item_name = input("Enter the name of the item to add: ")
            if item_name in items:
                hero.add_to_inventory(item_name)
                print(f"{item_name} added to inventory.")
            else:
                print("Item not found.")
        elif choice == "3":
            print("Available Status Effects:")
            for effect_name in status_effects.keys():
                print(f"- {effect_name}")
            effect_name = input("Enter the status effect to apply: ")
            if effect_name in status_effects:
                effect = StatusEffect(**status_effects[effect_name])
                effect.apply_effect(hero)
                print(f"{effect_name} applied.")
            else:
                print("Status effect not found.")
        elif choice == "4":
            print("Returning to arena...")
            break
        else:
            print("Invalid choice. Please try again.")

def battle_arena():
    print("Welcome to the Battle Arena Sandbox!")
    hero = create_hero()
    print("\nYour hero has been created!")
    hero.show_inventory()

    while True:
        print("\nWhat would you like to do?")
        print("1. Enter a battle")
        print("2. Spawn a Merchant")
        print("3. Check inventory")
        print("4. Use a potion")
        print("5. Craft Materials")
        print("6. Admin Options")
        print("7. Exit the arena")
        choice = input("Choose an option: ")

        if choice == "1":
            # Start a battle with a randomly spawned level 1 monster
            enemy = spawn_random_monster_level_1()
            #print(f"\nA wild {enemy.name} has appeared!")
            
            # Start the battle loop
            start_battle(hero, enemy)
            
            # After the battle, if the hero survives, collect loot
            if hero.hp > 0:
                print("\nBattle complete!")
                hero.show_inventory()  # Show updated inventory
               
            else:
                print(f"{hero.name} has fallen in battle. Game over!")
                print (f" Score: {hero.score}")
                break
        
        elif choice == "2":
            npc.npc_merchant(hero)
        
        elif choice == "3":
            # Display hero's inventory separately
            print("\nInventory:")
            hero.show_inventory()
        
        elif choice == "4":
            # Prompt for potion usage
            potion_name = input("Enter the name of the potion you want to use: ")
            hero.use_potion(potion_name)  # Use potion if available
            
        elif choice == "5":
            crafting_menu(hero)
            
        elif choice == "6":
            admin_actions(hero)


        elif choice == "7":
            print("Exiting the arena. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

# Run the battle arena sandbox
battle_arena()
