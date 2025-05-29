from models.owner import Owner
from models.pet import Pet

def create_owner(name):
    owner = Owner(name=name)
    owner.save()
    return owner

def create_pet(name, pet_type, age, owner_id):
    pet = Pet(name=name, pet_type=pet_type, age=age, owner_id=owner_id)
    pet.save()
    return pet

def list_owners():
    return Owner.get_all()

def list_pets():
    return Pet.get_all()

def find_owner_by_name(name):
    return Owner.find_by_name(name)

def get_owner_pets(owner_id):
    owner = Owner.find_by_id(owner_id)
    return owner.pets() if owner else []

def delete_pet(pet_id):
    pet = Pet.find_by_id(pet_id)
    if pet:
        pet.delete()
        return True
    return False
