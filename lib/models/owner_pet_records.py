from lib.models.owner import Owner
from lib.models.pet import Pet
from lib.db.db import CONN, CURSOR

CURSOR.execute("DELETE FROM pets")
CURSOR.execute("DELETE FROM owners")
CONN.commit()

owner1 = Owner(name="Webster")
owner1.save()

owner2 = Owner(name="Sarah")
owner2.save()

owner3 = Owner(name="Jamal")
owner3.save()

owner4 = Owner(name="Nia")
owner4.save()

pet1 = Pet(name="Simba", species="dog", owner_id=owner1.id)
pet1.save()

pet2 = Pet(name="Whiskers", species="cat", owner_id=owner2.id)
pet2.save()

pet3 = Pet(name="Max", species="parrot", owner_id=owner3.id)
pet3.save()

pet4 = Pet(name="Bella", species="rabbit", owner_id=owner4.id)
pet4.save()

pet5 = Pet(name="Chapo", species="dog", owner_id=owner1.id)
pet5.save()

print("\nSample owners and pets added to the database.\n")

owners = Owner.get_all()
for owner in owners:
    print(f"Owner: {owner.name} (ID: {owner.id})")
    pets = owner.pets()
    if pets:
        for pet in pets:
            print(f"   {pet.name} the {pet.species}")
    else:
        print("   No pets found.")
    print("-" * 30)
