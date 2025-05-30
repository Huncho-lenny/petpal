import sqlite3
from models.owner import Owner
from models.pet import Pet

CONN = sqlite3.connect('petpal.db', check_same_thread=False)
CURSOR = CONN.cursor()

def add_owner():
    name = input("Enter owner's name: ").strip()
    if not name:
        print("Error: Owner name cannot be empty!")
        return
        
    owner = Owner(name)
    try:
        owner.save(CURSOR)
        CONN.commit()
        print(f"Owner '{name}' added successfully!")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        CONN.rollback()

def add_pet():
    try:
        owner_id = int(input("Enter owner ID: "))
        owner = Owner.find_by_id(owner_id, CURSOR)
        if not owner:
            print(f"No owner found with ID {owner_id}")
            return
            
        name = input("Enter pet's name: ").strip()
        breed = input("Enter pet's breed: ").strip()
        age = int(input("Enter pet's age: "))
        
        if not name or not breed:
            print("Error: Name and breed cannot be empty!")
            return
            
        pet = Pet(name, breed, age, owner_id)
        pet.save(CURSOR)
        CONN.commit()
        print(f"Pet '{name}' added to owner '{owner.name}'!")
    except ValueError:
        print("Invalid input! Please enter numbers for ID and age.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        CONN.rollback()

def show_pets():
    try:
        owner_id = int(input("Enter owner ID: "))
        owner = Owner.find_by_id(owner_id, CURSOR)
        if not owner:
            print(f"No owner found with ID {owner_id}")
            return
            
        pets = Pet.get_by_owner(owner_id, CURSOR)
        if not pets:
            print(f"No pets found for owner '{owner.name}'")
            return
            
        print(f"\nPets for {owner.name}:")
        for pet in pets:
            print(f"  - {pet.name} ({pet.breed}), {pet.age} years old")
    except ValueError:
        print("Invalid input! Please enter a number for ID.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def run():
    print("Welcome to PetPal!")
    
    menu_options = {
        "1": ("Add Owner", add_owner),
        "2": ("Add Pet", add_pet),
        "3": ("Show Pets for Owner", show_pets),
        "4": ("Exit", None)
    }
    
    while True:
        print("\n" + "="*20)
        print("PetPal Menu")
        for key, (text, _) in menu_options.items():
            print(f"{key}. {text}")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "4":
            print("\nThank you for using PetPal! Goodbye!")
            break
            
        if choice in menu_options:
            menu_options[choice][1]()
        else:
            print("Invalid option. Please choose 1-4")

if __name__ == "__main__":
    try:
        run()
    finally:
        CONN.close()