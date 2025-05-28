from models.owner import Owner
from models.pet import Pet

def menu():
    print("\n--- PetPal CLI ---")
    print("1. Add Owner")
    print("2. Add Pet")
    print("3. View All Owners")
    print("4. View All Pets")
    print("5. See Pets by Owner")
    print("6. Exit")

def run():
    while True:
        menu()
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter owner's name: ")
            age = input("Enter owner's age: ")
            owner = Owner(name, age)
            owner.save()
            print(f"Owner {name} added.")

        elif choice == "2":
            name = input("Enter pet name: ")
            species = input("Enter species: ")
            owner_id = input("Enter owner ID: ")
            pet = Pet(name, species, int(owner_id))
            pet.save()
            print(f"Pet {name} added.")

        elif choice == "3":
            owners = Owner.get_all()
            print("\nAll Owners:")
            for o in owners:
                print(f"[{o.id}] {o.name} ({o.age})")

        elif choice == "4":
            pets = Pet.get_all()
            print("\nAll Pets:")
            for p in pets:
                print(f"[{p.id}] {p.name} the {p.species} (Owner ID: {p.owner_id})")

        elif choice == "5":
            owner_id = input("Enter owner ID to view their pets: ")
            owner = Owner.find_by_id(int(owner_id))
            if owner:
                pets = owner.pets()
                print(f"\nPets owned by {owner.name}:")
                for pet in pets:
                    print(f"- {pet.name} ({pet.species})")
            else:
                print("Owner not found.")

        elif choice == "6":
            print("Exiting PetPal.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    run()
