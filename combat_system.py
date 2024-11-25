import random
from enemies_list import spawn_random_monster_level_1
from enemies_list import spawn_random_monster_level_1



def player_turn(hero, enemy):
    print("\nYour turn:")
    action = input("Do you want to attack with 'melee' or 'spell'? ").lower()

    if action == "melee":
       
        weapon = next((item for item in hero.inventory if "attack" in item), None)
        if weapon:
            attack_roll = random.randint(1, 20)
            
            if hero.hero_class == "Barbarian":
                required_roll = 12
            elif hero.hero_class == "Paladin":
                required_roll = 8
            elif hero.hero_class == "Wizard":
                required_roll = 10
            else:
                required_roll = 8    
                       
            print(f"You rolled a {attack_roll}. (Need {required_roll} or higher)")
            if attack_roll >= required_roll:
                print(f"Your {weapon['name']} hits for {weapon['attack']} damage!")
                enemy.hp -= weapon["attack"]
            else:
                print("Your attack missed!")
        else:
            print("You have no melee weapon!")

    elif action == "spell":
        
        spells = [item for item in hero.inventory if "mana_cost" in item]
        if not spells:
            print("No spells found!")
            return
        
        # Choose a spell to cast
        for i, spell in enumerate(spells):
            # Display damage or healing based on spell type
            if "damage" in spell:
                print(f"{i + 1}. {spell['name']} - Damage: {spell['damage']}, Mana Cost: {spell['mana_cost']}")
            elif "heal_amount" in spell:
                print(f"{i + 1}. {spell['name']} - Heals: {spell['heal_amount']}, Mana Cost: {spell['mana_cost']}")
            elif "special_effect" in spell:
                print(f"{i + 1}. {spell['name']} - Buff: Blesses you!")
                

        try:
            spell_choice = int(input("Choose a spell by number: ")) - 1
            if 0 <= spell_choice < len(spells):
                spell = spells[spell_choice]
                if hero.mana >= spell["mana_cost"]:
                    hero.mana -= spell["mana_cost"]
                    if "damage" in spell:
                        print(f"You cast {spell['name']} for {spell['damage']} damage!")
                        enemy.hp -= spell["damage"]
                    elif "heal_amount" in spell:
                        print(f"You cast {spell['name']} and heal for {spell['heal_amount']} HP!")
                        hero.hp = min(hero.hp + spell["heal_amount"], hero.max_hp)
                    elif "special_effect" in spell:
                        print(f"You cast {spell['name']} and a sense of {spell.get('status_message', 'power')} fills you.")

                else:
                    print("Not enough mana to cast this spell.")
            else:
                print("Invalid spell choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def enemy_turn(hero, enemy):
    print("\nEnemy's turn!")
    # Enemy attacks with random damage within its attack range
    enemy_damage = random.randint(enemy.attack_power - 2, enemy.attack_power + 2)
    print(f"The {enemy.name} attacks for {enemy_damage} damage!")
    hero.hp -= enemy_damage

def check_victory(hero, enemy):
    if hero.hp <= 0:
        print(f"{hero.name} has been defeated!")
        return True
    elif enemy.hp <= 0:
        print(f"The {enemy.name} has been defeated!")
        if enemy.name in enemy.monster_types_1:
            hero.score += random.randint(32, 100)
        
        if enemy.loot:
             print("You've found the following loot:")
        for item in enemy.loot:
                print(f"- {item}")
                hero.collect_loot(enemy.loot)
        
        else:
            print("No loot found this time.")
        return True
           
    return False


def start_battle(hero, enemy):
    print(f"A wild {enemy.name} appears!")
    
    # Battle loop
    while hero.hp > 0 and enemy.hp > 0:
        player_turn(hero, enemy)
        if check_victory(hero, enemy):
            break
        
        enemy_turn(hero, enemy)
        if check_victory(hero, enemy):
            break
        
        # Show current stats after each round
        print(f"\n{hero.name} - HP: {hero.hp}/{hero.max_hp}, Mana: {hero.mana}/{hero.max_mana}")
        print(f"{enemy.name} - HP: {enemy.hp}")

# Example setup
# Make sure your hero class has `max_hp` and `max_mana` attributes and initialize hero accordingly
# hero = Hero(name="Aragon", hero_class="Paladin", hp=150, mana=100)
# start_battle(hero)
