# Restaurant Menu Management

def add_item(menu, item):
    if item not in menu:
        menu.append(item)
    return menu

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"'{item}' not found in menu.")
    return menu

def check_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"


if __name__ == "__main__":
    initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
    add_item_name = "Tacos"
    remove_item_name = "Salad"
    check_item_name = "Pizza"

    updated_menu = add_item(initial_menu, add_item_name)
    updated_menu = remove_item(updated_menu, remove_item_name)
    print("Updated menu:", updated_menu)
    print("Availability:", check_item(updated_menu, check_item_name))
