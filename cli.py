from lib.models.owner import Owner
from lib.models.pet import Pet

def menu():
    print("\n1. Add Owner")
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
    
    owner = Owner.find_by_id(int(owner_id))
    if not owner:
        print("Owner not found.")
        return
    
    pet = Pet(name=name, pet_type=pet_type, owner_id=owner.id)
    pet.save()
    print(f"Pet '{pet.name}' added for Owner '{owner.name}'.")

def show_pets_for_owner():
    owner_id = input("Enter owner ID: ")
    owner = Owner.find_by_id(int(owner_id))
    
    if not owner:
        print("Owner not found.")
        return

    pets = owner.pets()
    print(f"Pets for {owner.name}:")
    for pet in pets:
        print(f"- {pet.name} ({pet.pet_type})")

def run():
    while True:
        menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_owner()
        elif choice == "2":
            add_pet()
        elif choice == "3":
            show_pets_for_owner()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run()
