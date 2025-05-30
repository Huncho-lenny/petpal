from lib.db.connection import CONN, CURSOR
from lib.models.owner import Owner
from lib.models.pet import Pet

Owner.CONN = CONN
Owner.CURSOR = CURSOR
Pet.CONN = CONN
Pet.CURSOR = CURSOR


def menu():
    print("\nPetPal Menu")
    print("1. Add Owner")
    print("2. Add Pet")
    print("3. Show Pets for an Owner")
    print("4. Exit")

def add_owner():
    name = input("Enter owner's name: ")
    owner = Owner(name)
    owner.save()
    print(f"Owner '{owner.name}' added with ID {owner.id}.")

def add_pet():
    name = input("Enter pet's name: ")
    pet_type = input("Enter pet type: ")
    owner_id = input("Enter owner ID: ")

    try:
        owner = Owner.find_by_id(int(owner_id))
    except ValueError:
        print("Invalid ID format.")
        return

    if not owner:
        print("Owner not found.")
        return
    
    pet = Pet(name=name, pet_type=pet_type, owner_id=owner.id)
    pet.save()
    print(f"Pet '{pet.name}' added for Owner '{owner.name}'.")

def show_pets_for_owner():
    owner_id = input("Enter owner ID: ")

    try:
        owner = Owner.find_by_id(int(owner_id))
    except ValueError:
        print("Invalid ID format.")
        return

    if not owner:
        print("Owner not found.")
        return

    pets = owner.pets()
    if pets:
        print(f"Pets for {owner.name}:")
        for pet in pets:
            print(f"- {pet.name} ({pet.pet_type})")
    else:
        print(f"{owner.name} has no pets yet.")

def run():
    while True:
        print("\nPetPal Menu")
        print("1. Add Owner")
        print("2. Add Pet")
        print("3. Show Pets for an Owner")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_owner()
        elif choice == "2":
            add_pet()
        elif choice == "3":
            show_pets_for_owner()
        elif choice == "4":
            print("Goodbye!")
            CONN.close()
            break
        else:
            print("Invalid choice.")

    CONN.close()    

if __name__ == "__main__":
    run()