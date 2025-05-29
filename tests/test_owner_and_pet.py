import pytest
from lib.models.owner import Owner
from lib.models.pet import Pet
from lib.db.connection import setup_db, CURSOR

@pytest.fixture(autouse=True)
def setup():
    setup_db()
    yield
    CURSOR.execute("DELETE FROM owners")
    CURSOR.execute("DELETE FROM pets")

def test_owner_can_save_and_retrieve():
    owner = Owner("Test Owner")
    owner.save()

    found = Owner.find_by_id(owner.id)
    assert found.name == "Test Owner"

def test_owner_adds_pet():
    owner = Owner("Sarah")
    owner.save()

    pet = Pet("Benny", "cat")
    owner.add_pet(pet)

    assert pet.owner_id == owner.id
    assert pet in owner.pets()

def test_pet_type_validation():
    with pytest.raises(ValueError):
        Pet("Rex", "dragon")

def test_pet_owner_lookup():
    owner = Owner("John")
    owner.save()

    pet = Pet("Sparky", "dog", owner.id)
    pet.save()

    assert pet.owner().name == "John"
