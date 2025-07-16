##Using functions, come up with a simple menu 
#def menu
menu = {
    "Breakfast": {
        1: {"name": "Pancakes", "price": 1000},
        2: {"name": "Tossed bread", "price": 8000},
        3: {"name": "Coffee", "price": 20000}
    },
    "Lunch": {
        1: {"name": "Beef", "price": 20000},
        2: {"name": "Chicken", "price": 20000},
        3: {"name": "G.nuts", "price": 8000}
    },
    "Dinner": {
        1: {"name": "Fries", "price": 10000},
        2: {"name": "Salad", "price": 4000},
        3: {"name": "Coffee", "price": 20000}
    }
}

def display_categories():
    print("\n=== Meal Categories ===")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("0. Checkout and Exit")

def display_menu(category):
    print(f"\n--- {category} Menu ---")
    for key, item in menu[category].items():
        print(f"{key}. {item['name']} - ${item['price']:.2f}")
    print("0. Back to Categories")

def main():
    total = 0.0
    while True:
        display_categories()
        choice = input("Select a category (0 to exit): ")

        if choice == '0':
            break
        elif choice == '1':
            category = "Breakfast"
        elif choice == '2':
            category = "Lunch"
        elif choice == '3':
            category = "Dinner"
        else:
            print("Invalid choice. Try again.")
            continue

        while True:
            display_menu(category)
            try:
                item_choice = int(input(f"Select an item from {category} (0 to go back): "))
                if item_choice == 0:
                    break
                elif item_choice in menu[category]:
                    item = menu[category][item_choice]
                    total += item['price']
                    print(f"Added {item['name']} - ${item['price']:.2f}")
                else:
                    print("Invalid item. Try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    print(f"\nTotal amount due: ${total:.2f}")
    print("Thank you for visiting!")
if "name"== "_main_":
 main()


