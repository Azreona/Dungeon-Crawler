import random
from items_list import items, recipes

items = {
    "Health Potion": {"type": "potion", "heal_amount": 20, "Price": 35},
    "Empty Vial": {"Type": "material","Price": 33 },
    "Wolf Fang": {"type": "material", "Price": 15}
}


def npc_merchant(hero):
    print("Welcome Traveler, come here and take a look!")
    stock = random.sample(list(items.items()), k=random.randint(1, len(items)))
    stock.extend([(recipe_name, {"type": "recipe", "Price": random.randint(50, 100)}) for recipe_name in recipes.keys()])
    
    
    print("items for sale:")
    for i, (item_name, item_data) in enumerate(stock, start=1):
        item_type = item_data.get("type","Unkown")
        print(f"{i}. {item_name} ({item_type}) - {item_data['Price']} coins")
        
        
    try:
        choice = int(input("Each item is marked with a number, please, pick a number: "))
        if choice == -1:
            print("Thank you traveler, I will be seeing you")
            return
        
        item_name, item_data = stock[choice]
        item_price = item_data["Price"]
        
        if hero.coins >= item_price:
            hero.coins -= item_price
            
            if item_data.get("type") == "recipe":
                hero.discovered_recipes.append(item_name)
                print(f"You have purchased the recipe for {item_name}!")            
            
            else:
                hero.add_to_inventory(item_name)
                print(f"You have bought {item_name} for {item_price} coins")
        else:
            print(f"You seem to be a little short there...")
    except (ValueError, IndexError):
        print("Invalid Choice. Please try again")
    

#def npc_
        
       
    