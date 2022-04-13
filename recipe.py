# Input : Inventory inc. urgency
# Uses : Database of recipes  
# Output : Best matching recipes 

recipes = {
    'Banana Bread':
    {
        'butter': 140, 
        'caster-sugar': 140, 
        'eggs': 2, 
        'sr-flour':140,
        'baking-powder': 1, 
        'bananas': 2, 
        'icing-sugar': 50
    },

    'Creamy Mushroom Pasta': 
    {
        'olive oil': 2, 
        'butter': 25, 
        'onion': 1, 
        'chestnut mushrooms': 250, 
        'garlic': 1, 
        'white wine': 100, 
        'double cream': 200, 
        'lemons': 1, 
        'parmesan': 200,
        'pasta': 300,
        'parsley': 1
    }, 

    'Leek and Potato Soup': 
    {
        'butter': 50, 
        'potatoes': 450, 
        'onion': 1, 
        'leeks': 450, 
        'stock': 1200, 
        'cream': 150, 
        'milk': 125
    }
}

inventory = {
    'butter': 140, 
    'caster-sugar': 140, 
    'eggs': 2, 
    'sr-flour':140,
    'baking-powder': 1, 
    'bananas': 2, 
    'icing-sugar': 50
}

for item in recipes: 
    list = recipes[item]
    shared_items = {k: list[k] for k in list if k in inventory and list[k] == inventory[k]}
    print(shared_items)

# print("recipes[0]", recipes[1]) 
# shared_items = {k: recipes[k] for k in recipes if k in inventory and recipes[k] == inventory[k]}
# print(shared_items)