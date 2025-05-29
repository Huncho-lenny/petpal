from lib.db.connection import setup_db
from lib.models.owner import Owner
from lib.models.pet import Pet

def main():
    setup_db()
    print("Welcome to PetPal 🐾")

    owner_name = input("Enter your name: ")
    owner = Owner(owner_name)
    owner.save()
    print(f"Hello, {owner.name}! Your ID is {owner.id}")

    pet_name = input("Name your pet: ")
    pet_type = input("What type of pet is it? (dog, cat, bird, fish, lizard, hamster): ")
    
    try:
        pet = Pet(pet_name, pet_type)
        owner.add_pet(pet)
        print(f"{pet.name} the {pet.pet_type} has been added to your profile!")
    except ValueError as e:
        print(f"Oops! {e}")

    print("\nYour pets:")
    for pet in owner.pets():
        print(pet)

if __name__ == "__main__":
    main()
