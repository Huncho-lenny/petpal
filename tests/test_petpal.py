import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.owner import Owner
from models.pet import Pet

def test_add_pet_to_owner():
    owner = Owner(name="Ms. Janet")
    owner.save()

    pet = Pet(name="Whiskers", pet_type="Cat", age=2, owner_id=owner.id)
    pet.save()

    pets = owner.pets()
    assert len(pets) == 1
    assert pets[0].name == "Whiskers"
    assert pets[0].pet_type == "Cat"
    assert pets[0].owner_id == owner.id

def test_get_sorted_pets():
    owner = Owner(name="Drake")
    owner.save()

    Pet(name="Zara", pet_type="Bird", age=1, owner_id=owner.id).save()
    Pet(name="Arlo", pet_type="Dog", age=3, owner_id=owner.id).save()
    Pet(name="Milo", pet_type="Cat", age=2, owner_id=owner.id).save()

    sorted_pets = owner.get_sorted_pets()
    sorted_names = [pet.name for pet in sorted_pets]

    assert sorted_names == ["Arlo", "Milo", "Zara"]
