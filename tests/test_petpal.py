import pytest
from lib.models.owner import Owner
from lib.models.pet import Pet

def test_owner_has_name():
    owner = Owner("Webster")
    assert owner.name == "Webster"

def test_add_pet_to_owner():
    owner = Owner("Webster")
    owner.save()
    
    pet = Pet(name="Buddy", pet_type="dog", owner_id=owner.id)
    pet.save()

    assert pet.owner_id == owner.id
    assert pet.name == "Buddy"
